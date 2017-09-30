# -*- coding: utf-8 -*-
{
    'name': "crm_sage_simsoft",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Omayma baklouti",   
    'website': "http://www.yourcompany.com",
	'sequence': 5,

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sales_team' , 'crm' ,  'web_kanban_gauge' , 'gamification','sale' , 'sale_crm' ,'product'],

    # always loadedbbn
    'data': [
        # 'security/ir.model.access.csv',
        'views/devis_sage.xml',   
        'views/views.xml',   
        'views/partner_views.xml',   
        'views/product_views.xml',   
        'wizard/wizard_devis.xml',   
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
	'installable': True,
	'application': True,
	'auto_install': False,
	'web_preload': True,
}