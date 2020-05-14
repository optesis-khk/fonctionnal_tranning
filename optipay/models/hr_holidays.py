from odoo import models, api, _
from odoo.exceptions import UserError
import math
from datetime import date


class hr_holidays(models.Model):
    _inherit = "hr.leave.allocation"

    @api.multi
    def action_approve(self):
        # if validation_type == 'both': this method is the first approval approval
        # if validation_type != 'both': this method calls action_validate() below
        if any(holiday.state != 'confirm' for holiday in self):
            raise UserError(_('Leave request must be confirmed ("To Approve") in order to approve it.'))

        # if the type of leave is leave we update the contract
        if self.holiday_status_id.time_type == 'leave':
            for contract in self.env['hr.contract'].search([('employee_id', '=', self.employee_id.id)]):
                if contract:
                    new_val = contract.nbj_aquis + self.number_of_days_display
                    contract.write({'nbj_aquis': new_val})

        current_employee = self.env['hr.employee'].search([('user_id', '=', self.env.uid)], limit=1)
        self.filtered(lambda hol: hol.validation_type == 'both').write(
            {'state': 'validate1', 'first_approver_id': current_employee.id})
        self.filtered(lambda hol: not hol.validation_type == 'both').action_validate()
        self.activity_update()
        return True

    def action_refuse(self):
        """remove allocate day from contract"""
        if self.holiday_status_id.time_type == 'leave':
            for contract in self.env['hr.contract'].search([('employee_id', '=', self.employee_id.id)]):
                if contract:
                    new_val = contract.nbj_aquis - self.number_of_days_display
                    contract.write({'nbj_aquis': new_val})
        return super(hr_holidays, self).action_refuse()


class hrLeave(models.Model):
    _inherit = "hr.leave"

    @api.multi
    def action_approve(self):
        # if validation_type == 'both': this method is the first approval approval
        # if validation_type != 'both': this method calls action_validate() below
        if any(holiday.state != 'confirm' for holiday in self):
            raise UserError(_('Leave request must be confirmed ("To Approve") in order to approve it.'))

        for contract in self.env['hr.contract'].search([('employee_id', '=', self.employee_id.id)]):
            if contract:
                new_val = contract.nbj_pris + self.number_of_days_display
                contract.write({'nbj_pris': new_val})

        current_employee = self.env['hr.employee'].search([('user_id', '=', self.env.uid)], limit=1)
        self.filtered(lambda hol: hol.validation_type == 'both').write({'state': 'validate1', 'first_approver_id': current_employee.id})
        self.filtered(lambda hol: not hol.validation_type == 'both').action_validate()
        self.activity_update()
        return True


    def action_refuse(self):
        """remove allocate day """
        for contract in self.env['hr.contract'].search([('employee_id', '=', self.employee_id.id)]):
            if contract and self.state == 'validate':
                new_val = contract.nbj_pris - self.number_of_days_display
                contract.write({'nbj_pris': new_val})
        return super(hrLeave, self).action_refuse()

    #def _get_number_of_days(self, date_from, date_to, employee_id):
    #    """ Returns a float equals to the timedelta between two dates given as string."""
    #    #if employee_id:
    #    #    employee = self.env['hr.employee'].browse(employee_id)
    #    #    return employee.get_work_days_data(date_from, date_to)['days']
	#	
    #    #time_delta = date_to - date_from
    #    #return math.ceil(time_delta.days + float(time_delta.seconds) / 86400)
    #    delta = date_to - date_from
    #    return delta.days

