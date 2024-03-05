# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields,models,api

class StockTransport(models.Model):
    _name = "fleet.vehicle.model.category"
    _inherit = "fleet.vehicle.model.category"
    
    max_weight = fields.Integer('Max weight(kg)', default=1000)
    max_volume = fields.Integer('Max volume(m³)', default=1000)
    
    _sql_constraints = [
        ('check_max_weight_positive', 'CHECK(max_weight > 0)', 'Max Weight must be greater than 0!'),
        ('check_max_weight_positive', 'CHECK(max_volume > 0)', 'Max volume must be greater than 0!')
    ]
    
    # compute name of category
    @api.depends('name','max_weight','max_volume')
    def _compute_display_name(self):
        for record in self:
            record.display_name = f"{record.name}/({record.max_weight}kg,{record.max_volume}m³)"
