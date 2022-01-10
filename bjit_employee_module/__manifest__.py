# -*- coding: utf-8 -*-
{
    'name': "bjit_employee_module",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "BJIT",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',

        # 'views/templates.xml',
        'views/erp_employee_inherit_views.xml',
        'views/other_project_history_view.xml',
        'views/employee_type_view.xml',
        'views/employee_view_inherit.xml'
    ],

}
