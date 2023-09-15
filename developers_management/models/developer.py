# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class Developer(models.Model):
    _name = 'developer'
    _description = 'developers management'

    _order = "id"

    name = fields.Char('Name', required=True)
    _sql_constraints = [
        (
            'unique_name',
            'unique(name)',
            'Name must be unique',
        ),
    ]
    type = fields.Selection(
        string="Type",
        selection=[
            ("front-end", "Front-end"),
            ("backend", "Backend"),
            ("fullstack", "Fullstack"),
            ("out-stuff", "Out-stuff"),
        ],
    )
    global_identification = fields.Char(
        string="global identification",
        compute="_compute_global_identification",
    )
    phone = fields.Char(
        string="Phone",
        help="Not display if type = 'out-stuff'",
        readonly=True,
        states={"out-stuff": [("readonly", False)]},
    )
    email = fields.Char(string="Email")
    address = fields.Text(string="Address")
    birthday = fields.Date(string="Birthday")
    job_position = fields.Char(string="Job position")
    parent_id = fields.Many2one('company', string='Related Company', index=True)

    @api.depends("name", "type")
    def _compute_global_identification(self):
        for developer in self:
            developer.global_identification = f"{developer.name}-{developer.type}"