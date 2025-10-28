# -*- coding: utf-8 -*-
{
    'name': "costumer_queue_extend",

    'summary': """
        costumer_queue_extend Module for Odoo""",

    'description': """
        Costumer Queue Extend Module
    """,

    'author': "Alessandro",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'version': '16.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'customer_queue'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        #'views/costumer_queue_extend_views.xml',
        'views/counter_views.xml',
    ],
    
    'installable': True,
    'application': False,
    
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
