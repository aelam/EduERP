# -*- coding: utf-8 -*-
{
    'name': "open_academy",

    'summary': """
        教育行业erp""",

    'description': """
        教育行业erp模块
    """,

    'author': "Open Academy",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    # 'depends': ['base'],
    'depends': ['board', 'document', 'hr', 'web', 'website'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/templates.xml',
        'views/market_view.xml',
        'views/contact_view.xml',
        'views/contact_view_assign.xml',
        'views/menu_items.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'installable': True,
    'application': True,
    'auto_install': False,
}