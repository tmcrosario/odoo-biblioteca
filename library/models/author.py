# -*- coding: utf-8 -*-

from odoo import fields, models


class Author(models.Model):

    _name = 'library.author'

    name = fields.Char(
        required=True
    )

    publication_ids = fields.Many2many(
        comodel_name='library.publication'
    )
