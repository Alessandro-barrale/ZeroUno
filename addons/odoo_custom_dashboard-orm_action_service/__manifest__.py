# -*- coding: utf-8 -*-
{
    "name": "Owl ",
    "version": "16.0.1.0.0",
    "summary": "OWL ",
    "sequence": -1,
    "description": """OWL  Custom Dashboard""",
    "category": "OWL",
    "depends": ["base", "web", "sale", "board", 'customer_queue'],
    "data": [
        "views/sales_dashboard.xml",
        "views/sales_orders.xml",
    ],
    "demo": [],
    "installable": True,
    "application": True,
    "assets": {
        "web.assets_backend": [
            "odoo_custom_dashboard-orm_action_service/static/src/components/**/*.js",
            "odoo_custom_dashboard-orm_action_service/static/src/components/**/*.xml",
            "odoo_custom_dashboard-orm_action_service/static/src/components/**/*.scss",
        ],
    },
}
