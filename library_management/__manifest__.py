# -*- coding: utf-8 -*-
{
    'name': 'Library Management',
    'version': '1.0',
    'summary': 'Manage library books',
    'description': 'A module to manage library books',
    'category': 'Library',
    'author': "Varsha",
    'website': "https://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '16.0.1.0.0',
    'depends': ['base'],
    "license": "LGPL-3",
    'data': [
        'security/ir.model.access.csv',
        'views/library_book.xml',
        "views/menu.xml",
    ],
     'installable': True,
    'application': False,
}
