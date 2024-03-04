# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Stock_Transport',
    'version': '1.1.21',
    'category': 'Transport',
    'author': 'odoo',
    'depends': ['stock_picking_batch','fleet','stock','stock_delivery'],
    'summary': 'This is Stock Transport services which is use for Transfer stock ine place to another',
    'auto_install': True,
    'installable': True,
    'license': 'LGPL-3',
    'data':[
        'view/inherit_fleet_category.xml',
        'view/inherited_stock_picking_batch.xml',
        'view/inherited_transfers_volume.xml'
    ]
}
