from odoo import models, fields

class Book(models.Model):
    _name = 'library.book'
    _description = 'Library Book'

    name = fields.Char(string='Name', required=True)
    author = fields.Char(string='Author')
    publication_date = fields.Date(string='Publication Date')
    state = fields.Selection(
        [
            ("draft", "New"),
            ("submit", "Submitted"),
        ],
        string="Status",
        default="draft",
    )

    def submit(self):
        self.state = 'submit'