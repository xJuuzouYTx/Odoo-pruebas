# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError
import logging
_logger = logging.getLogger(__name__)

    
class AccountMoveReversalInherit(models.TransientModel):
    _inherit = 'account.move.reversal'

    # Campos del modelo heredado
    @api.model
    def create(self, vals):
        _logger.info("********************************", self)
        # Ejecute la acción deseada antes de crear el nuevo registro
        #result = super(AccountMoveReversalInherit, self).create(vals)
        
        raise UserError("Error al crear")
        # Ejecute la acción deseada después de crear el nuevo registro
        return result