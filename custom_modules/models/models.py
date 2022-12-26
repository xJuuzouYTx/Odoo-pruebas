# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError
import json 

import logging
_logger = logging.getLogger(__name__)

    
class AccountMoveReversalInherit(models.TransientModel):
    _inherit = 'account.move.reversal'

    # Campos del modelo heredado
    @api.model
    def create(self, vals):
        #_logger.debug("********************************")
        # Ejecute la acción deseada antes de crear el nuevo registro
        #result = super(AccountMoveReversalInherit, self).create(vals)
        
        raise UserError(json.dumps(vals))
        # Ejecute la acción deseada después de crear el nuevo registro
        return result