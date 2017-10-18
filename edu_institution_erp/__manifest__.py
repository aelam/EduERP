# -*- coding: utf-8 -*-
{
    'name': "Edu Institution ERP",

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
    'category': 'Education',
    'version': '0.1',

    # any module necessary for this one to work correctly
    # 'depends': ['base'],
    'depends': ['edu_institution_sales', 'edu_institution_hr', 'edu_institution_teaching','edu_institution_finance'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/templates.xml',
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