# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields,models,api

class StockTransportBatch(models.Model):
    _inherit= "stock.picking.batch"
   
    Dock = fields.Many2one('stock.dock')
    vehicle = fields.Many2one('fleet.vehicle' , placeholder="Third Party Provider" ,string="Vehicle")
    vehicle_category = fields.Many2one('fleet.vehicle.model.category', stirng= "Vehicle Category" ,placeholder="semi-truck")
    weight = fields.Integer("weight" ,compute="_compute_weight")
    volume = fields.Integer("volume", default=0)
        
    @api.depends('vehicle_category')
    def _compute_weight(self):
        for record in self:
            total_weight = 0.0
            avg_weight = 0.0
            if record.vehicle_category:
                max_weight = record.vehicle_category.max_weight
                print("Max Weight:", max_weight) 

                for pick in record:
                    for line in pick.move_line_ids:
                        total_weight += line.product_id.weight * line.quantity
                if max_weight > 0:
                    avg_weight = (total_weight / max_weight) * 100
                else:
                    avg_weight = 0.0
                    
                record.weight = avg_weight
            else:
                record.weight = 0.0

    