# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class Company(models.Model):
    _name = 'company'
    _description = 'company for developers'

    _order = "id"

    name = fields.Char('Name', required=True)
    _sql_constraints = [
        (
            'unique_name',
            'unique(name)',
            'Name must be unique',
        ),
    ]
    address = fields.Text(string="Address")
    developer_ids = fields.One2many('developer', 'parent_id', string='Developers')

