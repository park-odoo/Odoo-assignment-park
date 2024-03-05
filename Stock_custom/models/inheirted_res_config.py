# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields,models,api

class StockTransportSetting(models.TransientModel):
    _inherit = 'res.config.settings'
    
    module_Stock_transport = fields.Boolean("Dispatch Management System")
   