# -*- coding: utf-8 -*-
{
    'name': "bjit_project_member",

    'summary': """
        Project Customization""",

    'description': """
        Customizing Project Module
    """,

    'author': "Shahriar",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Services/Project',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'project', 'hr', 'custom_employee'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/inherited_views.xml',
        'views/project_member_views.xml',
        'views/project_monthly_invoice_views.xml',
        # 'views/inherited_employee_views.xml',
    ],

    "assets": {
        "web.assets_backend": [
            "bjit_project_member/static/src/css/my_class.css"
        ]
           }

}
