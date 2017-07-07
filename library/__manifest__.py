# -*- coding: utf-8 -*-

{
    'name': 'TMC Biblioteca',
    'summary': 'Odoo module for TMC internal library management',
    'version': '10.0.1.0.0',
    'website': 'https://www.tmcrosario.gob.ar',
    'author': 'Tribunal Municipal de Cuentas - Municipalidad de Rosario',
    'license': 'AGPL-3',
    'depends': [u'tmc'],
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/publication.xml',
        'views/authors.xml',
        'views/editorial.xml',
        'views/menu.xml'
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'qweb': [],
}
