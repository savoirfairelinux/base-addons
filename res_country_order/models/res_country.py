# -*- coding: utf-8 -*-
# © 2017 Savoir-faire Linux
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
from odoo import fields, models


class Country(models.Model):
    _inherit = 'res.country'
    _order = 'seq asc, name'

    seq = fields.Integer(
        string='Sequence',
    )
