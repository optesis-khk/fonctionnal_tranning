from odoo import api, fields, models, _
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT as DF

class NomModel(models.Model):
    _name = "nom.model"

    name = fields.Char("nom du champ")
    champ1 = fields.Char(string="nom du champ", required="True")
    champ2 = fields.Integer(default="0")
    champ3 = fields.Float()
    champ_id = fields.Many2one("nom.model", string="nom du champ")
    champ_ids = fields.One2many("nom.model.line", "champ_id", string="nom du champ")
    champ4 = fields.Selection(selection=[('type1', 'Type 1'), ('type2', 'Type 2')], string="nom du champ")
    total = fields.Float("Total", store=True, compute="fonction")

    _sql_constraints = [
        ('uniq_name', 'unique(name)', "A project already exists with this name . Project's name must be unique!"),
        ('uniq_champ1', 'unique(champ1)', "A project's code already exists with this code . Project's code must be unique!"),
    ]

    #utuliser pour création de séquence
    @api.model
    def create(self, vals):
		if vals.get('name', '/') == '/':
			vals['name'] = self.env['ir.sequence'].next_by_code('nom.model') or '/'
		result = super(NomModel, self).create(vals)
		return result

    #calcul date
    def get_date(self):
        date = datetime.strptime(self.date, DF).date()
        if self.duree == "12":
            self.date = date + relativedelta(months=+12)
        if self.duree == "24":
            self.date = date + relativedelta(years=+24)
        if self.duree == "36":
            self.date = date + relativedelta(days=+36)
        #autre méthode

        server_dt = DEFAULT_SERVER_DATE_FORMAT
        date_from = datetime.strptime(date, server_dt)
        date_start = datetime.strptime(record.date_start, server_dt)
        dur = date_from - date_start
        record.nb_days = dur.days

    #utilisé pour les champs compute
    @api.depend("champ1")
    def fonction(self):
        record = self.pool.get('NomModel').browse(cr, uid, ids, context=context) #pour recupérer les valeurs d'un model
        default.update({'champ': i.champ+1}) #mettre a jour um champ

        #effectuer des recherche par rapport a des condition
        y = self.pool.get('pp.control')
            other_table2 = y.search(cr, uid,[('id','=','4'), ('other_field', '=', True)])
        #recupérer le resultat dans un dictionnaire
            record = y.browse(cr, uid, other_table2[0])

    #si changement du champ
    @api.onchange('champ1')
    def onchange(self):
        if self.champ1:
            self.champ2 = self.champ1.champ.id
        #fqire des domain dans le code
        return {'domain':{'account_analytic_id':[('alima_contrat_ids.projet_id.id','=',self.projet_id.id)]}} #pour ume conditiom
        return {'domain':{'budget_id':[('crossovered_budget_line.analytic_account_id.id','=',self.analytic_account_id.id),('account_ids.code','=',self.account_id.code)]}} #pour n condition

    #utuliser pour bloquer la suppression d'enregistrement
    @api.multi
    def unlink(self):
        if self.filtered(lambda x: x.state in ('done', 'confirmed', 'approved', 'cancel')):
            raise UserError(_('Cet enregistrement ne peux etre supprime'))
        return super(NomModel, self).unlink()

    #préparation des lignes et des en tete
    @api.multi
    def _prepare_line_values(self):
        res = dict()
        for record in self:
            lines = []
            for line in record.champ_ids:
                lines.append((0, 0, {'champ_id': line.champ.id,'champ': line.champ,}))
            res[record.id] = {
                'champ': record.champ,
                'champ_line': lines,  #affectation au champs one2many
            }
        return res

    #changement d'état pour workflow
    def action_button(self):
        for record in self:
            record.state = "confirmed"

    #passer des valeur d'un model a un autre    
    def action_done(self):
        for record in self:
            self.ensure_one()
            record.state = "done"
            values = self._prepare_line_values()
            order = self.env['sale.order'].create(values[self.id])
            return {
                "type": "ir.actions.act_window",
                "res_model": "nom.model",
                "views": [[False, "form"]],
                "res_id": order.id,
            }


#héritage model
class NomModelBis(models.Model):
    _inherit = "nom.model.line"
