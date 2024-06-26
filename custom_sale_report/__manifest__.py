{
    'name': 'Customized SaleOrder Report',
    'version': '1.0',
    'summary': 'Customize sale order report to include customer reference',
    'description': """
    This module customizes the sale order report to include a new field `customer_reference`.
    """,
    'author': 'Varsha',
    'category': 'Uncategorized',
    'version': '16.0.1.0.0',
    "license": "LGPL-3",
    'depends': ['sale_management'],
    'data': [
        'report/sale_order_report_template.xml',
        'views/sale_order_views.xml',
    ],
    'installable': True,
    'application': False,
}
