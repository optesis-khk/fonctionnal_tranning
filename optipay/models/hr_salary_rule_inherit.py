# -*- coding: utf-8 -*-
# by khk
from odoo import fields, models


class HrSalaryRuleInherit(models.Model):
    _inherit = 'hr.salary.rule'

    is_prorata = fields.Boolean(string='Prorata', default=True,
                                help="Used to check if we apply prorata")
