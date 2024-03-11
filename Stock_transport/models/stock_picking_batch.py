# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields,models,api
from dateutil.relativedelta import relativedelta

class StockTransportBatch(models.Model):
    _inherit= "stock.picking.batch"
   
    dock_id = fields.Many2one('stock.dock', string="Dock")
    vehicle_id = fields.Many2one('fleet.vehicle',string="Vehicle")
    vehicle_category_id = fields.Many2one('fleet.vehicle.model.category', string= "Vehicle Category")
    weight = fields.Float("Weight",compute="_compute_weight_volume" ,store=True)
    volume = fields.Float("Volume", compute="_compute_weight_volume" , store =True)
    starting_date = fields.Date(default=fields.date.today())
    stoping_date = fields.Date(default=fields.date.today()+relativedelta(days=1))
    total_weight = fields.Float(string="Total Weight",compute="_compute_total_weight_volume")
    total_volume = fields.Float(string="total Volume",compute="_compute_total_weight_volume")
    
    @api.depends('name','total_weight','total_volume','vehicle_id')
    def _compute_display_name(self):
        for record in self:
            record.display_name = f"{record.name}/({record.total_weight:.2f}kg,{record.total_volume:.2f}m³) {record.vehicle_id.driver_id.name or ' '}"
 
    # For total weight of all warehouse and its all products
    @api.depends("move_ids","vehicle_category_id","picking_ids","picking_ids.move_ids.product_id.weight")
    def _compute_weight_volume(self):
        max_weight = self.vehicle_category_id.max_weight
        max_volume = self.vehicle_category_id.max_volume
        if max_weight:
            self.weight = (sum(product.product_id.weight * product.quantity for record in self for product in record.move_ids) / max_weight * 100)
        if max_volume:
            self.volume = (sum(product.pick_volume for record in self for product in record.picking_ids) / max_volume * 100)
            
    # For total volume of all warehouse and its all products
    @api.depends("move_ids","picking_ids","picking_ids.move_ids.product_id.weight")
    def _compute_total_weight_volume(self):
        self.total_weight = sum(product.product_id.weight * product.quantity for record in self for product in record.move_ids)
        self.total_volume = sum(product.pick_volume for record in self for product in record.picking_ids)
