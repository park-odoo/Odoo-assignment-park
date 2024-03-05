# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields,models,api

class StockTransportDock(models.Model):
    _name = "stock.dock"
    _description= "This for Diffrent Docks"
   
    name = fields.Char(string="Dock")
    
    _sql_constraints = [
        ('unique_id', 'UNIQUE(name)', 'Dock must be unique!')
    ]