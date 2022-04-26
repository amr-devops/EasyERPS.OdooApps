# -*- coding: utf-8 -*-
{
    'name': "POS auto print kitchen receipt",
    'support': "support@easyerps.com",
    'license': "LGPL-3",
    'summary': """
        Auto print kitchen receipt after validate
        """,
    'author': "EasyERPS",
    'website': "https://easyerps.com",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Point of Sale',
    'version': '14.0.1',
    # any module necessary for this one to work correctly
    'depends': ['base', 'point_of_sale', 'pos_restaurant'],
    # always loaded
    'data': [
        'views/templates.xml',
    ],
    
}
