# -*- coding: utf-8 -*-
{
    'name': "bjit_eaf",

    'summary': "",

    'description': "",

    'author': "My Company",
    'website': "",


    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'project'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/project_eaf.xml',
        'views/inherit_view_project.xml',
        'views/project_closure.xml',
    ]

}
