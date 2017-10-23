# -*- coding: utf-8 -*-
{
    'name': "Edu Institution Teaching",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Education',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['edu_institution_hr'],

    'security': [
        'security/ir_rule.xml',
        'security/ir.model.access.csv',
        'security/course_product_security.xml',
    ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/course_product_view.xml',
        'views/time_slot_view.xml',
        'views/menu_items.xml',

        'data/course_products.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
        
    ],

    'installable': True,
    'application': True,
    'auto_install': False,

}