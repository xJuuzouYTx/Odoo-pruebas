# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError


class AccountMoveReversalInherit(models.TransientModel):
    _inherit = 'account.move.reversal'
    
    
    def create(self, vals):
        raise UserError("Error al crear")