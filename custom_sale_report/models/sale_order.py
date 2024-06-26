from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    customer_reference = fields.Char(string="Customer Reference NO.")

