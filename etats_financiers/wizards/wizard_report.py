# -*- coding: utf-8 -*-

from odoo import api, fields, models


class BilanWizard(models.TransientModel):
    _name = "wizard.report.bilan"
    _description = "report bilan wizard"

    debut = fields.Date("Date debut")
    fin = fields.Date("Date fin")

    @api.multi
    def check_report(self):
        data = {}
        data['form'] = self.read(['debut', 'fin'])[0]
        return self._print_report(data)

    def _print_report(self, data):
        data['form'].update(self.read(['debut', 'fin'])[0])
        return {'type': 'ir.actions.report','report_name': 'etats_financiers.report_bilan','report_type':"qweb-pdf",'data': data,}


class CompteResultatWizard(models.TransientModel):
    _name = "wizard.report.compte_resultat"
    _description = "report compte resultat wizard"

    debut = fields.Date("Date debut")
    fin = fields.Date("Date fin")

    @api.multi
    def check_report(self):
        data = {}
        data['form'] = self.read(['debut', 'fin'])[0]
        return self._print_report(data)

    def _print_report(self, data):
        data['form'].update(self.read(['debut', 'fin'])[0])
        return {'type': 'ir.actions.report','report_name': 'etats_financiers.report_compte_resultat','report_type':"qweb-pdf",'data': data,}


class TabFluxTresoWizard(models.TransientModel):
    _name = "wizard.report.tab_flux_treso"
    _description = "report Tableaux de flux de tresorerie wizard"

    debut = fields.Date("Date debut")
    fin = fields.Date("Date fin")

    @api.multi
    def check_report(self):
        data = {}
        data['form'] = self.read(['debut', 'fin'])[0]
        return self._print_report(data)

    def _print_report(self, data):
        data['form'].update(self.read(['debut', 'fin'])[0])
        return {'type': 'ir.actions.report','report_name': 'etats_financiers.report_tab_flux_treso','report_type':"qweb-pdf",'data': data,}
