# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields,models,api

class StockPickVolume(models.Model):
    _inherit = "stock.picking"
    
    pick_volume = fields.Float(string="Volume" , compute="_compute_volume")
 
    # For compute Total volume of all products in batch
    @api.depends('move_ids')
    def _compute_volume(self):
        for record in self:
            record.pick_volume = sum(line.product_id.volume * line.quantity for line in record.move_ids)
