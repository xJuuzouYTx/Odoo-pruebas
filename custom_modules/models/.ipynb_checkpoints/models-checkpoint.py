# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AccountMoveReversalInherit(models.TransientModel):
    _inherit = 'account.move.reversal'
    
    
    def create(self, vals):
        raise "Error al crear"