# -*- coding: utf-8 -*-
{
    'name': "twinscafe",

    'summary': """
        odoo module for twinscafe""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'report_xlsx'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/menu.xml',
        'views/kelompokmenu_view.xml',
        'views/menucafe_view.xml',
        'views/person_view.xml',
        'views/barista_view.xml',
        'views/chef_view.xml',
        'views/cashier_view.xml',
        'views/waiters_view.xml',
        'views/officeboy_view.xml',
        'views/konsumen_view.xml',
        'views/supplier_view.xml',
        'views/direksi_view.xml',
        'views/penjualan_view.xml',
        'report/report.xml',
        'report/print_faktur_penjualan.xml',
        'wizard/menucafedatang_wizard_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
