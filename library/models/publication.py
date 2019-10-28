from odoo import api, fields, models


class Publication(models.Model):

    _name = 'library.publication'

    _publication_formats_ = [('book', 'Book'), ('magazine', 'Magazine'),
                             ('digital', 'Digital'),
                             ('bibliorato', 'Bibliorato'),
                             ('manual', 'Manual'), ('work', 'Work'),
                             ('other', 'Other')]

    _bookcases_ = [('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')]

    @api.constrains('stock_number')
    def _check_stock_number(self):
        if len(str(self.stock_number)) != 4:
            return False
        return True

    name = fields.Char(required=True, string='Title')

    stock_number = fields.Integer()

    publication_format = fields.Selection(selection=_publication_formats_)

    author_ids = fields.Many2many(comodel_name='library.author')

    editorial_id = fields.Many2one(comodel_name='library.editorial')

    tome = fields.Char()

    edition = fields.Integer()

    edition_year = fields.Char(size=4)

    bookcase = fields.Selection(selection=_bookcases_)

    shelf = fields.Integer(size=2)

    position = fields.Integer(size=2)

    comments = fields.Text()

    employee_id = fields.Many2one(comodel_name='tmc.hr.employee',
                                  string='Responsible')

    office_id = fields.Many2one(comodel_name='tmc.hr.office',
                                related='employee_id.office_id',
                                readonly=True)

    active = fields.Boolean(default=True)
