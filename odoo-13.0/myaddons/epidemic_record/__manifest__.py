# -*- coding: utf-8 -*-
{
    'name': "疫情记录",

    'summary': """
        疫情记录""",

    'description': """
        描述疫情记录
    """,

    'author': "Allen",
    'website': "http://www.allen.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views\epidemic_record_view.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
}
