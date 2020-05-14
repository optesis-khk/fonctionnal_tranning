# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import except_orm, Warning, RedirectWarning
from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta

import logging

_logger = logging.getLogger(__name__)


class hr_payslip(models.Model):
    _inherit = "hr.payslip"

    @api.multi
    def compute_total_paid_loan(self):
        total = 0.00
        for line in self.loan_ids:
            if line.paid == True:
                total += line.paid_amount
        self.total_loan_amount_paid = total

    loan_ids = fields.One2many('hr.loan.line', 'payroll_id', string="Prêts", readonly=True)
    total_loan_amount_paid = fields.Float(string="Total Prêt", compute='compute_total_paid_loan', readonly=True)

    # the following code is handled in optipay module
    # @api.multi
    # def compute_sheet(self):
    #    for payslip in self:
    #        loan_line_obj = self.env['hr.loan.line']
    #        loan_ids = loan_line_obj.search(
    #            [('employee_id', '=', payslip.employee_id.id), ('paid_date', '>=', payslip.date_from),
    #             ('paid_date', '<=', payslip.date_to), ('loan_id.state', 'in', ['approve_1', 'approve'])])
    #        # loan_ids.write({'paid': True})
    #        payslip.loan_ids = loan_ids
    #    super(hr_payslip, self).compute_sheet()

    @api.model
    def action_payslip_done(self):
        for line in self.loan_ids:
            if line.paid is not True:
                line.action_paid_amount()
        super(hr_payslip, self).action_payslip_done()
