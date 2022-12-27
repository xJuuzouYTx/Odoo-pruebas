# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError
from odoo.tools.translate import _
import json

import logging
_logger = logging.getLogger(__name__)


class AccountMoveReversalInherit(models.TransientModel):
    _inherit = 'account.move.reversal'

    def reverse_moves(self):
        self.ensure_one()
        moves = self.move_ids

        # Create default values.
        default_values_list = []
        for move in moves:
            default_values_list.append(self._prepare_default_reversal(move))

        batches = [
            [self.env['account.move'], [], True],   # Moves to be cancelled by the reverses.
            [self.env['account.move'], [], False],  # Others.
        ]
        for move, default_vals in zip(moves, default_values_list):
            is_auto_post = bool(default_vals.get('auto_post'))
            is_cancel_needed = not is_auto_post and self.refund_method in ('cancel', 'modify')
            batch_index = 0 if is_cancel_needed else 1
            batches[batch_index][0] |= move
            batches[batch_index][1].append(default_vals)

        # Handle reverse method.
        moves_to_redirect = self.env['account.move']
        for moves, default_values_list, is_cancel_needed in batches:
            new_moves = moves._reverse_moves(default_values_list, cancel=is_cancel_needed)

            if self.refund_method == 'modify':
                moves_vals_list = []
                for move in moves.with_context(include_business_fields=True):
                    moves_vals_list.append(move.copy_data({'date': self.date if self.date_mode == 'custom' else move.date})[0])
                new_moves = self.env['account.move'].create(moves_vals_list)

            moves_to_redirect |= new_moves

        self.new_move_ids = moves_to_redirect

        for line in range(len(self.new_move_ids.line_ids)):
            record =  self.env['custom_modules.account.redirect'].search([('account_origin_id.id','=',self.new_move_ids.line_ids[line].account_id.id)])
            _logger.info(record)
            #odoo.addons.custom_modules.models.models: custom_modules.account.redirect(2,)
            self.new_move_ids.line_ids[line].account_id = self.env('account.account').search([('code','=',record.code if record.id else self.new_move_ids.line_ids.account_id.code)]).id
            _logger.info("******", record)

        # Create action.
        action = {
            'name': _('Reverse Moves'),
            'type': 'ir.actions.act_window',
            'res_model': 'account.move',
        }

        if len(moves_to_redirect) == 1:
            action.update({
                'view_mode': 'form',
                'res_id': moves_to_redirect.id,
                'context': {'default_move_type':  moves_to_redirect.move_type},
            })
        else:
            action.update({
                'view_mode': 'tree,form',
                'domain': [('id', 'in', moves_to_redirect.ids)],
            })
            if len(set(moves_to_redirect.mapped('move_type'))) == 1:
                action['context'] = {'default_move_type':  moves_to_redirect.mapped('move_type').pop()}
        return action
    
class AccountRedirect(models.Model):
    _name = 'custom_modules.account.redirect'

    account_origin_id = fields.Many2one('account.account', string='Cuenta de origen')
    account_destination_id = fields.Many2one('account.account', string='Cuenta de destino')

