# -*- coding: utf-8 -*-
{
    'name': "delta_inventory",

    'sequence': 1,

    'summary': "",

    'description': "",

    'author': "BJIT Limited",
    'website': "http://https://bjitgroup.com/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Application/Inventory Management',
    'version': 'alpha 0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr', 'website'],

    # always loaded
    'data': [
        'security/delta_security.xml',
        'security/ir.model.access.csv',

        'views/menu.xml',
        'views/product_view.xml',
        'views/transfer_iview.xml',
        'views/stockm_view.xml',
        'views/product_status.xml',
        'views/ref_transfer.xml',
        'views/warehouse_view.xml',

        'reports/report.xml',
        'reports/transfer_report.xml',
        # 'reports/warehouse_report.xml',

        'views/product_web.xml'








    ],

    'installable': True,
    'application': True,
    'auto_install': False,

}
