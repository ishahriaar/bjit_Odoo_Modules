{
    'name': "bjit_module",
    'sequence': 1,

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


        'views/functions.xml',
        'views/fun_add.xml',
        'views/inherit_view_project.xml',

        'views/project_module.xml',
        'views/module_name.xml',
        'views/technology_view.xml',
        'views/tech_add.xml',
        'views/inherit_view_project.xml',
        'views/project_techno_view.xml'

    ],

    "assets": {
        "web.assets_backend": [
            "project_module/static/src/css/my_custom.css"
        ]
           }


}
