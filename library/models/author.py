from odoo import fields, models


class Author(models.Model):

    _name = 'library.author'
    _description = 'Author'

    name = fields.Char(required=True)

    publication_ids = fields.Many2many(comodel_name='library.publication')
