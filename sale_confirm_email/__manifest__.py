{
    'name': 'Sale confirm email',
    'version': '1.0',
    'summary': 'Customize sale order confirmation',
    'description': """
    This module customizes the sale order confirmation.
    """,
    'author': 'Varsha',
    'category': 'Uncategorized',
    'version': '16.0.1.0.0',
    "license": "LGPL-3",
    'depends': ['base','sale_management','base_automation'],
    'data': [
        'data/sale_server_action.xml',
        'data/sale_order_email_template.xml',
    ],
    'installable': True,
    'application': False,
}
