# -*- coding: utf-8 -*-
{
    'name': "Custom QR",

    'summary': """
        Costum QR Code test""",

    'description': """
        Test Custom QR module for odoo.
    """,

    'author': "Alessandro",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Tools',
    'version': '16.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'web', 'website', 'hr', 'portal', 'sale' ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/qr_ticket_template.xml',
        'views/qr_ticket_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    
    'application': True,
}
