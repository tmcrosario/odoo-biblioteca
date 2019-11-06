from odoo import fields, models


class Editorial(models.Model):

    _name = 'library.editorial'
    _description = 'Editorial'

    name = fields.Char(required=True)
