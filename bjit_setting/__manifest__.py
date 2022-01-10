# -*- coding: utf-8 -*-
{
    'name': "bjit_setting",

    'summary': "",

    'description': "",

    'author': "",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'module',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'project', 'hr'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',

        'views/bjitset_views.xml',
        'views/id_sequence.xml',
        'views/settings_inherit.xml'
    ],

}
