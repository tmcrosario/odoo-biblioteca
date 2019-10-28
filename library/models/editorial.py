from odoo import fields, models


class Editorial(models.Model):

    _name = 'library.editorial'

    name = fields.Char(required=True)
