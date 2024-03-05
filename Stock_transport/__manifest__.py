# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Stock_Transport',
    'version': '1.1.21',
    'category': 'Transport',
    'author': 'odoo',
    'depends': ['stock_picking_batch','fleet'],
    'summary': 'This is Stock Transport services which is use for Transfer stock ine place to another',
    'auto_install': True,
    'installable': True,
    'license': 'LGPL-3',
    'data':[
        'security/ir.model.access.csv',
        
        'view/fleet_category_view.xml',
        'view/stock_picking_inherit_view.xml',
        'view/stock_picking_batch_view.xml',
        'view/stock_picking_action_view.xml'
    ]
}
