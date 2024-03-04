# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields,models,api

class StockTransport(models.Model):
    _name = "fleet.vehicle.model.category"
    _inherit = "fleet.vehicle.model.category"
    
    max_weight = fields.Integer('Max_weight', default=0)
    max_volume = fields.Integer('Max_volume', default=0)
    # display_name = fields.Char('name', copute='_compute_display_name')
    
    @api.depends('name','max_weight','max_volume')
    def _compute_display_name(self):
        for record in self:
            
            record.display_name = f"{record.name}/({record.max_weight}kg,{record.max_volume}m³)"