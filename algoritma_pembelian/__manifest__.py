# -*- coding: utf-8 -*-
{
    'name': "Modul Custom Penjualan",
    'version': "13.0.1.0.0",
    'category': "purchase",
    'summary': """
        Modul Custom Penjualan""",
    'description': """
        Ini adalah Modul Custom Penjualan
    """,
    'author': "My Company",
    'website': "https://www.yourcompany.com",
    'depends': ['web','base','product'],
    'data': [
        'security/ir.model.access.csv',
        'views/algoritma_pembelian_view.xml',
        'views/algoritma_pembelian_action.xml',
        'views/algoritma_pembelian_menuitem.xml'
    ],
    'installable':True,
    'application':True,
    'license':"OEEL-1",
}
