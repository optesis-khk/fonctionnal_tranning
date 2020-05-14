import time
from datetime import datetime, date, time as t
from odoo import models, fields, api, _
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT

class HrContractBonus(models.Model):
    _inherit = 'hr.contract'

    @api.onchange('bonus.amount')
    def get_bonus_amount(self):
        current_datetime = datetime.now()
        for contract in self:
            bonus_amount = 0
            for bonus in contract.bonus:
                x = datetime.strptime(str(bonus.date_from), '%Y-%m-%d')
                y = datetime.strptime(str(bonus.date_to), '%Y-%m-%d')
                if x <= current_datetime <= y:
                    bonus_amount = bonus_amount + bonus.amount
                contract.total_bonus = bonus_amount

    total_bonus = fields.Float(string="Total Bonus", compute=get_bonus_amount)
    bonus = fields.One2many('hr.employee.bonus', 'contract_id', string="Bonus",
                            domain=[('state', '=', 'active')])
    nb_days = fields.Float(string="Anciennete", compute="_get_duration")
    cumul_jour = fields.Float("Cumul jours anterieur")
    cumul_conges = fields.Float("Cumul conges anterieur")
    nbj_aquis = fields.Float("Nombre de jour aquis", store=True)
    convention_id = fields.Many2one('line.optesis.convention', 'Categorie')
    nbj_pris = fields.Float("Nombre de jour pris", default="0")
    cumul_mensuel = fields.Float("Cumul mensuel conges")
    last_date = fields.Date("derniere date")
    alloc_conges = fields.Float("Allocation conges", compute="_get_alloc")
    motif = fields.Selection([('demission', 'Démission'), ('fin', 'Fin de contrat'), ('retraite', 'Retraite'),
                              ('licenciement', 'Licenciement'), ('deces', 'Décès'),
                              ('depart_nogicie', 'Départ négocié')], string='Motif de sortie')
    dateAnciennete = fields.Date("Date d'ancienneté", default=lambda self: fields.Date.to_string(date.today()))
    typeContract = fields.Selection([('cdi', 'CDI'), ('cdd', 'CDD'), ('others', 'Autres')], string="Type de contract")
    nbj_sup = fields.Float("Nombre de jour supplementaire")
    year_extra_day_anciennete = fields.Integer()
    nbj_alloue = fields.Float(string="Nombre de jour alloue", default="2.0")
    nbj_travail = fields.Float(string="Nombre de jour de travail", default="30")

    @api.cr_uid_ids_context
    def reinit(self, contract_ids):
        for record in self.browse(contract_ids):
            record.cumul_mensuel = record.cumul_mensuel - record.alloc_conges
            record.alloc_conges = 0
            record.nbj_aquis = record.nbj_aquis - record.nbj_pris
            record.nbj_pris = 0

    @api.onchange("convention_id")
    def onchange_categ(self):
        if self.convention_id:
            self.wage = self.convention_id.wage

    @api.multi
    def _get_droit(self, provision_amount):
        for record in self:

            if record.cumul_conges == 0: # external holidays
                record.cumul_mensuel += provision_amount
            else:
                val_pr = record.cumul_conges + provision_amount
                record.cumul_mensuel += val_pr
                record.cumul_conges = 0

            if record.cumul_jour == 0:
                record.nbj_aquis += record.company_id.nbj_alloue
            else:
                nb_aquis = record.company_id.nbj_alloue + record.cumul_jour
                record.nbj_aquis += nb_aquis
                record.cumul_jour = 0

            # create leaves line allocation
            self.env['hr.leave.allocation'].create({
                'name': 'Leave allowance',
                'number_of_days': record.company_id.nbj_alloue,
                'state': 'validate',
                'employee_id': record.employee_id.id
            })

    @api.multi
    @api.depends("cumul_mensuel", "nbj_pris", "nbj_aquis")
    def _get_alloc(self):
        for record in self:
            if record.nbj_pris == 0 and record.cumul_mensuel == 0:
                return True
            if record.nbj_pris == 0 and record.cumul_mensuel != 0:
                return True
            if record.nbj_pris != 0 and record.cumul_mensuel == 0:
                return True
            if record.nbj_pris != 0 and record.cumul_mensuel != 0:
                if record.nbj_aquis == 0:
                    return True
                else:
                    record.alloc_conges = (record.cumul_mensuel * record.nbj_pris) / record.nbj_aquis
            #if record.nbj_aquis >= record.nbj_travail:
            #    record.alloc_conges = (record.cumul_mensuel * record.nbj_pris) / record.nbj_travail

    @api.depends('dateAnciennete')
    def _get_duration(self):
        for record in self:
            server_dt = DEFAULT_SERVER_DATE_FORMAT
            today = datetime.now()
            dateAnciennete = datetime.strptime(str(record.dateAnciennete), server_dt)
            dur = today - dateAnciennete
            record.nb_days = dur.days
            # check if employee seniority is more than 10 years
            # if it is we add one day in nbj_aquis
            if dur.days >= 3653:
                if record.year_extra_day_anciennete:
                    if record.year_extra_day_anciennete != today.year:  # we must add it one time by year
                        record.year_extra_day_anciennete = today.year
                        record.nbj_aquis += 1
                        # create leaves line allocation
                        self.env['hr.leave.allocation'].create({
                            'name': 'Leave allowance for seniority',
                            'number_of_days': 1,
                            'state': 'validate',
                            'employee_id': record.employee_id.id
                        })
                else:
                    record.year_extra_day_anciennete = today.year
                    record.nbj_aquis += 1
                    # create leaves line allocation
                    self.env['hr.leave.allocation'].create({
                        'name': 'Leave allowance for seniority',
                        'number_of_days': 1,
                        'state': 'validate',
                        'employee_id': record.employee_id.id
                    })
