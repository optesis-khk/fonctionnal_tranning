from odoo import api, fields, models, _
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT as DF
from datetime import date

class OptesisNote(models.Model):
    _name = "optesis.note"

    name = fields.Char("Nom", required="True")
    sequence = fields.Char("Sequence")
    date_debut = fields.Date("Date de debut", required="True")
    date_fin = fields.Date("Date de debut", required="True")
    note1 = fields.Boolean("Note 1")
    note3A = fields.Boolean("Note 3A")
    note3B = fields.Boolean("Note 3B")
    note3C = fields.Boolean("Note 3C")
    note3D = fields.Boolean("Note 3D")
    note3E = fields.Boolean("Note 3E")
    note4 = fields.Boolean("Note 4")
    note5 = fields.Boolean("Note 5")
    note6 = fields.Boolean("Note 6")
    note7 = fields.Boolean("Note 7")
    note8 = fields.Boolean("Note 8")
    note8A = fields.Boolean("Note 8A")
    note9 = fields.Boolean("Note 9")
    note10 = fields.Boolean("Note 10")
    note11 = fields.Boolean("Note 11")
    note12 = fields.Boolean("Note 12")
    note13 = fields.Boolean("Note 13")
    note14 = fields.Boolean("Note 14")
    note15A = fields.Boolean("Note 15A")
    note15B = fields.Boolean("Note 15B")
    note16A = fields.Boolean("Note 16A")
    note16B = fields.Boolean("Note 16B")
    note16B_BIS = fields.Boolean("Note 16B BIS")
    note16C = fields.Boolean("Note 16C")
    note17 = fields.Boolean("Note 17")
    note18 = fields.Boolean("Note 18")
    note19 = fields.Boolean("Note 19")
    note20 = fields.Boolean("Note 20")
    note21 = fields.Boolean("Note 21")
    note22 = fields.Boolean("Note 22")
    note23 = fields.Boolean("Note 23")
    note24 = fields.Boolean("Note 24")
    note25 = fields.Boolean("Note 25")
    note26 = fields.Boolean("Note 26")
    note27A = fields.Boolean("Note 27A")
    note27B = fields.Boolean("Note 27B")
    note28 = fields.Boolean("Note 28")
    note29 = fields.Boolean("Note 29")
    note30 = fields.Boolean("Note 30")
    note31 = fields.Boolean("Note 31")
    note32 = fields.Boolean("Note 32")
    note33 = fields.Boolean("Note 33")
    note34 = fields.Boolean("Note 34")
    note35 = fields.Boolean("Note 35")
    note36 = fields.Boolean("Note 36")
    note37 = fields.Boolean("Note 37")

    note1_lines1 = fields.One2many("optesis.note1.tab1", "note_id")
    note1_lines2 = fields.One2many("optesis.note1.tab2", "note_id")
    commentaire_note1 = fields.Text("Commentaire")

    note3A_lines = fields.One2many("optesis.note3a", "note_id")
    commentaire_note3A = fields.Text("Commentaire")

    note3B_lines = fields.One2many("optesis.note3b", "note_id")
    commentaire_note3B = fields.Text("Commentaire")

    note3C_lines = fields.One2many("optesis.note3c", "note_id")
    commentaire_note3C = fields.Text("Commentaire")

    note3D_lines = fields.One2many("optesis.note3d", "note_id")
    commentaire_note3D = fields.Text("Commentaire")

    note3E_lines = fields.One2many("optesis.note3e", "note_id")
    commentaire_note3E = fields.Text("Commentaire")

    note4_lines1 = fields.One2many("optesis.note4.tab1", "note_id")
    note4_lines2 = fields.One2many("optesis.note4.tab2", "note_id")
    commentaire_note4 = fields.Text("Commentaire")

    note5_lines1 = fields.One2many("optesis.note5.tab1", "note_id")
    commentaire1_note5 = fields.Text("Commentaire")
    note5_lines2 = fields.One2many("optesis.note5.tab2", "note_id")
    commentaire2_note5 = fields.Text("Commentaire")

    note6_lines = fields.One2many("optesis.note6", "note_id")
    commentaire_note6 = fields.Text("Commentaire")

    note7_lines = fields.One2many("optesis.note7", "note_id")
    commentaire_note7 = fields.Text("Commentaire")

    note8_lines = fields.One2many("optesis.note8", "note_id")
    commentaire_note8 = fields.Text("Commentaire")

    note8A_lines1 = fields.One2many("optesis.note8a.tab1", "note_id")
    note8A_lines2 = fields.One2many("optesis.note8a.tab2", "note_id")

    note9_lines = fields.One2many("optesis.note9", "note_id")
    commentaire_note9 = fields.Text("Commentaire")

    note10_lines = fields.One2many("optesis.note10", "note_id")
    commentaire_note10 = fields.Text("Commentaire")

    note11_lines = fields.One2many("optesis.note11", "note_id")
    commentaire_note11 = fields.Text("Commentaire")

    note12_lines1 = fields.One2many("optesis.note12.tab1", "note_id")
    commentaire1_note12 = fields.Text("Commentaire")
    note12_lines2 = fields.One2many("optesis.note12.tab2", "note_id")
    commentaire2_note12 = fields.Text("Commentaire")

    note13_lines = fields.One2many("optesis.note13", "note_id")
    commentaire_note13 = fields.Text("Commentaire")

    note14_lines = fields.One2many("optesis.note14", "note_id")
    commentaire_note14 = fields.Text("Commentaire")

    note15A_lines = fields.One2many("optesis.note15a", "note_id")
    commentaire_note15A = fields.Text("Commentaire")

    note15B_lines = fields.One2many("optesis.note15b", "note_id")
    commentaire_note15B = fields.Text("Commentaire")

    note16A_lines = fields.One2many("optesis.note16a", "note_id")
    commentaire_note16A = fields.Text("Commentaire")

    note16BTab1_lines = fields.One2many("optesis.note16b.tab1", "note_id")
    commentaire_note16BTab1 = fields.Text("Commentaire")

    note16BTab2_lines = fields.One2many("optesis.note16b.tab2", "note_id")
    commentaire_note16BTab2 = fields.Text("Commentaire")

    note16BTab3_lines = fields.One2many("optesis.note16b.tab3", "note_id")
    commentaire_note16BTab3 = fields.Text("Commentaire")

    note16BBISTab1_lines = fields.One2many("optesis.note16bbis.tab1", "note_id")
    commentaire_note16BBISTab1 = fields.Text("Commentaire")

    note16BBISTab2_lines = fields.One2many("optesis.note16bbis.tab2", "note_id")
    commentaire_note16BBISTab2 = fields.Text("Commentaire")

    note16C_lines = fields.One2many("optesis.note16c", "note_id")
    commentaire_note16C = fields.Text("Commentaire")

    note17_lines = fields.One2many("optesis.note17", "note_id")
    commentaire_note17 = fields.Text("Commentaire")

    note18_lines = fields.One2many("optesis.note18", "note_id")
    commentaire_note18 = fields.Text("Commentaire")

    note19_lines = fields.One2many("optesis.note19", "note_id")
    commentaire_note19 = fields.Text("Commentaire")

    note20_lines = fields.One2many("optesis.note20", "note_id")
    commentaire_note20 = fields.Text("Commentaire")

    note21_lines = fields.One2many("optesis.note21", "note_id")
    commentaire_note21 = fields.Text("Commentaire")

    note22_lines = fields.One2many("optesis.note22", "note_id")
    commentaire_note22 = fields.Text("Commentaire")

    note23_lines = fields.One2many("optesis.note23", "note_id")
    commentaire_note23 = fields.Text("Commentaire")

    note24_lines = fields.One2many("optesis.note24", "note_id")
    commentaire_note24 = fields.Text("Commentaire")

    note25_lines = fields.One2many("optesis.note25", "note_id")
    commentaire_note25 = fields.Text("Commentaire")

    note26_lines = fields.One2many("optesis.note26", "note_id")
    commentaire_note26 = fields.Text("Commentaire")

    note27A_lines = fields.One2many("optesis.note27a", "note_id")
    commentaire_note27A = fields.Text("Commentaire")

    note28_lines = fields.One2many("optesis.note28", "note_id")
    commentaire_note28 = fields.Text("Commentaire")

    note29_lines = fields.One2many("optesis.note29", "note_id")
    commentaire_note29 = fields.Text("Commentaire")

    note30_lines = fields.One2many("optesis.note30", "note_id")
    commentaire_note30 = fields.Text("Commentaire")

    note31_lines = fields.One2many("optesis.note31", "note_id")

    note32_lines = fields.One2many("optesis.note32", "note_id")

    note33_lines = fields.One2many("optesis.note33", "note_id")

    note34_lines = fields.One2many("optesis.note34", "note_id")

    note37_lines = fields.One2many("optesis.note37", "note_id")


    @api.model
    def create(self, vals):
        if vals.get('sequence', '/') == '/':
            vals['sequence'] = self.env['ir.sequence'].next_by_code('optesis.note') or '/'
        result = super(OptesisNote, self).create(vals)
        return result

    @api.onchange("note1")
    def onchange_note1(self):
        line = []
        line2 = []
        if self.note1 is True:
            line.append((0,0,{'name':'Dettes financieres et ressources assimilees'}))
            line.append((0,0,{'name':'Emprunts obligataires convertibles'}))
            line.append((0,0,{'name':'Autres emprunts obligataires'}))
            line.append((0,0,{'name':'Emprunts et dettes des etablissements de credit'}))
            line.append((0,0,{'name':'Autres dettes financieres'}))
            line.append((0,0,{'name':'Dettes du passif circulant'}))
            line.append((0,0,{'name':'Dettes de crédit-bail immobilier'}))
            line.append((0,0,{'name':'Dettes de crédit-bail mobilier'}))
            line.append((0,0,{'name':'Dettes sur contrats de location-vente'}))
            line.append((0,0,{'name':'Dettes sur contrats de location-acquisition'}))
            line.append((0,0,{'name':'Fournisseurs et comptes rattachés'}))
            line.append((0,0,{'name':'Clients'}))
            line.append((0,0,{'name':'Personnel'}))
            line.append((0,0,{'name':'Sécurité sociale et organismes sociaux'}))
            line.append((0,0,{'name':'Etat'}))
            line.append((0,0,{'name':'Organismes internationaux'}))
            line.append((0,0,{'name':'Associés et groupe'}))
            self.note1_lines1 = line

            line2.append((0,0,{'name':'Engagements consentis à des entites liees'}))
            line2.append((0,0,{'name':'Primes de remboursements, non echues'}))
            line2.append((0,0,{'name':'Avals, cautions, garanties'}))
            line2.append((0,0,{'name':'hypotheques, nantissements, gages, autres'}))
            line2.append((0,0,{'name':'Effets escomptes non echus'}))
            line2.append((0,0,{'name':'Creances commerciales et professionelles cedees'}))
            line2.append((0,0,{'name':'Abandons de creances conditionnels'}))
            self.note1_lines2 = line2

    @api.onchange("note3A")
    def onchange_note3A(self):
        line = []
        if self.note3A is True:
            line.append((0,0,{'name':'IMMOBILISATIONS INCORPORELLES'}))
            line.append((0,0,{'name':'Frais de développement et de prospection'}))
            line.append((0,0,{'name':'Brevet, licences, logiciels et droits similaires'}))
            line.append((0,0,{'name':'Fonds commercial et droit au bail'}))
            line.append((0,0,{'name':'Autres immobilisations incorporelles'}))
            line.append((0,0,{'name':'IMMOBILISATIONS CORPORELLES'}))
            line.append((0,0,{'name':'Terrains hors immeubles de placement'}))
            line.append((0,0,{'name':'Terrains - immeubles de placement'}))
            line.append((0,0,{'name':'Batiments hors immeubles de placement'}))
            line.append((0,0,{'name':'Batiments-immeubles de placement'}))
            line.append((0,0,{'name':'Aménagements, agencements et installations'}))
            line.append((0,0,{'name':'Matériel, mobilier et actifs biologiques'}))
            line.append((0,0,{'name':'Matériel de transport'}))
            line.append((0,0,{'name':'AVANCES ET ACOMPTES VERSES SUR IMMOBILISATTION'}))
            line.append((0,0,{'name':'IMMOBILISATIONS FINANCIERES'}))
            line.append((0,0,{'name':'Titres de participation'}))
            line.append((0,0,{'name':'Autres immobilisations financiéres'}))
            self.note3A_lines = line

    @api.onchange("note3B")
    def onchange_note3B(self):
        line = []
        if self.note3B is True:
            line.append((0,0,{'name':'Brevets, licences, logiciels et droits similaires'}))
            line.append((0,0,{'name':'Fonds commercial et droit au bail'}))
            line.append((0,0,{'name':'Autres immobilisations corporelles'}))
            line.append((0,0,{'name':'Terrains'}))
            line.append((0,0,{'name':'Bâtiments'}))
            line.append((0,0,{'name':'Aménagements, agencements et installations'}))
            line.append((0,0,{'name':'Matériel, mobilier et actifs biologiques'}))
            line.append((0,0,{'name':'Matériels de transport'}))
            self.note3B_lines = line

    @api.onchange("note3C")
    def onchange_note3C(self):
        line = []
        if self.note3C is True:
            line.append((0,0,{'name':'Frais de développement et de prospection'}))
            line.append((0,0,{'name':'Brevet, licences, logiciels et droits similaires'}))
            line.append((0,0,{'name':'Fonds commercial et droit au bail'}))
            line.append((0,0,{'name':'Autres immobilisations incorporelles'}))
            line.append((0,0,{'name':'Terrains hors immeubles de placement'}))
            line.append((0,0,{'name':'Terrains - immeubles de placement'}))
            line.append((0,0,{'name':'Batiments hors immeubles de placement'}))
            line.append((0,0,{'name':'Batiments-immeubles de placement'}))
            line.append((0,0,{'name':'Aménagements, agencements et installations'}))
            line.append((0,0,{'name':'Matériel, mobilier et actifs biologiques'}))
            line.append((0,0,{'name':'Matériels de transport'}))
            self.note3C_lines = line

    @api.onchange("note3D")
    def onchange_note3D(self):
        line = []
        if self.note3D is True:
            line.append((0,0,{'name':'Frais de développement et de prospection'}))
            line.append((0,0,{'name':'Brevet, licences, logiciels et droits similaires'}))
            line.append((0,0,{'name':'Fonds commercial et droit au bail'}))
            line.append((0,0,{'name':'Autres immobilisations incorporelles'}))
            line.append((0,0,{'name':'Terrains'}))
            line.append((0,0,{'name':'Bâtiments'}))
            line.append((0,0,{'name':'Aménagements, agencements et installations'}))
            line.append((0,0,{'name':'Matériel, mobilier et actifs biologiques'}))
            line.append((0,0,{'name':'Matériels de transport'}))
            line.append((0,0,{'name':'Titres de participations'}))
            line.append((0,0,{'name':'Autres immobilisations financiéres'}))
            self.note3D_lines = line

    @api.onchange("note3E")
    def onchange_note3E(self):
        line = []
        if self.note3E is True:
            line.append((0,0,{'name':''}))
            line.append((0,0,{'name':''}))
            line.append((0,0,{'name':''}))
            line.append((0,0,{'name':''}))
            line.append((0,0,{'name':''}))
            line.append((0,0,{'name':'Total écarts de réévaluation'}))
            line.append((0,0,{'name':'Total Provisions spéciales de réévaluation'}))
            line.append((0,0,{'name':'Montant de l’écart incorporé au capital'}))
            self.note3E_lines = line

    @api.onchange("note4")
    def onchange_note4(self):
        line = []
        line2 = []
        if self.note4 is True:
            line.append((0,0,{'name':'Titre de participation'}))
            line.append((0,0,{'name':'Prêts et créances'}))
            line.append((0,0,{'name':'Prêts au personnel'}))
            line.append((0,0,{'name':'Créances sur l’état'}))
            line.append((0,0,{'name':'Titres immobilisés'}))
            line.append((0,0,{'name':'Dépôts et cautionnement'}))
            line.append((0,0,{'name':'Intérêts courus'}))
            line.append((0,0,{'name':'TOTAL BRUT'}))
            line.append((0,0,{'name':'Dépréciations titres de participation'}))
            line.append((0,0,{'name':'Dépréciations autres immobilisations'}))
            line.append((0,0,{'name':'TOTAL NET DEPRECIATION'}))
            self.note4_lines1 = line

            line2.append((0,0,{'name':''}))
            self.note4_lines2 = line2

    @api.onchange("note5")
    def onchange_note5(self):
        line = []
        line2 = []
        if self.note5 is True:
            line.append((0,0,{'name':'Créances sur cession d’immobilisation'}))
            line.append((0,0,{'name':'Autres créances hors activités ordinaires'}))
            line.append((0,0,{'name':'TOTAL BRUT'}))
            line.append((0,0,{'name':'Dépréciations des créances HAO'}))
            line.append((0,0,{'name':'TOTAL NET DEPRECIATIONS'}))
            self.note5_lines1 = line

            line2.append((0,0,{'name':'Fournisseurs d’investissement'}))
            line2.append((0,0,{'name':'Fournisseurs d’investissement effet a payer'}))
            line2.append((0,0,{'name':'Fournisseurs d’investissement factures non parvenues'}))
            line2.append((0,0,{'name':'Versements restant a effectuer sur titres de participation et titres immobilises non liberes'}))
            line2.append((0,0,{'name':'Autres dettes hors activites ordinaires'}))
            self.note5_lines2 = line2


    @api.onchange("note6")
    def onchange_note6(self):
        line = []
        if self.note6 is True:
            line.append((0,0,{'name':'Marchandises'}))
            line.append((0,0,{'name':'Matiéres premiéres et fournitures liées'}))
            line.append((0,0,{'name':'Autres approvisionnements'}))
            line.append((0,0,{'name':'Produits en cours'}))
            line.append((0,0,{'name':'Services en cours'}))
            line.append((0,0,{'name':'Produits finis'}))
            line.append((0,0,{'name':'Produits intermédiaires'}))
            line.append((0,0,{'name':'Stocks en cours de route, en consignation ou en dépôt'}))
            line.append((0,0,{'name':'TOTAL BRUT STOCKS ET EN COURS'}))
            line.append((0,0,{'name':'Dépréciations des stocks'}))
            line.append((0,0,{'name':'TOTAL NET DEPRECIATION'}))
            self.note6_lines = line


    @api.onchange("note7")
    def onchange_note7(self):
        line = []
        if self.note7 is True:
            line.append((0,0,{'name':'Clients (hors réserves de propriété groupe)'}))
            line.append((0,0,{'name':'Clients effets à recevoir (hors réserves de propriété groupe)'}))
            line.append((0,0,{'name':'Clients et effets à recevoir avec réserves de propriété'}))
            line.append((0,0,{'name':'Clients et effets à recevoir Groupe'}))
            line.append((0,0,{'name':'Créances sur cession d’immobilisation'}))
            line.append((0,0,{'name':'Clients effets escomptés et non échus'}))
            line.append((0,0,{'name':'Créances litigieuses ou douteuses'}))
            line.append((0,0,{'name':'Clients produits à recevoir'}))
            line.append((0,0,{'name':'TOTAL BRUT CLIENTS'}))
            line.append((0,0,{'name':'Dépréciations des comptes clients'}))
            line.append((0,0,{'name':'TOTAL NET DEPRECIATION'}))
            line.append((0,0,{'name':'Clients, avances reçues hors groupe'}))
            line.append((0,0,{'name':'Clients, avances reçues groupe'}))
            line.append((0,0,{'name':'Autres clients crédteurs'}))
            line.append((0,0,{'name':'TOTAL CLIENTS CREDITEURS'}))
            self.note7_lines = line


    @api.onchange("note8")
    def onchange_note8(self):
        line = []
        if self.note8 is True:
            line.append((0,0,{'name':'Personnel'}))
            line.append((0,0,{'name':'Associés compte courant'}))
            line.append((0,0,{'name':'Organismes sociaux'}))
            line.append((0,0,{'name':'Etat et Collectivités publiques'}))
            line.append((0,0,{'name':'Organismes internationaux'}))
            line.append((0,0,{'name':'Apporteurs, associés et groupe'}))
            line.append((0,0,{'name':'Compte transitoire ajustement spécial lié à la révision du SYSCOHADA'}))
            line.append((0,0,{'name':'Autres débiteurs divers'}))
            line.append((0,0,{'name':'Charges constatées d’avance'}))
            line.append((0,0,{'name':'Comptes permanents non bloqués des établissements et des succursales'}))
            line.append((0,0,{'name':'Comptes de liaison charges et produits'}))
            line.append((0,0,{'name':'Comptes de liaison des sociétés en participation'}))
            line.append((0,0,{'name':'TOTAL AUTRES CREANCES'}))
            line.append((0,0,{'name':'Dépréciations des autres créances'}))
            line.append((0,0,{'name':'TOTAL NET DE DEPRECIATION'}))
            self.note8_lines = line


    @api.onchange("note8A")
    def onchange_note8A(self):
        line = []
        if self.note8A is True:
            line.append((0,0,{'name':'Montant global à étaler au 1er janvier 2018'}))
            line.append((0,0,{'name':'Durrée d’étalement retenue'}))
            self.note8A_lines1 = line


    @api.onchange("note9")
    def onchange_note9(self):
        line = []
        if self.note9 is True:
            line.append((0,0,{'name':'Titres de trésor et bons de caisse à court terme'}))
            line.append((0,0,{'name':'Actions'}))
            line.append((0,0,{'name':'Bons de souscription'}))
            line.append((0,0,{'name':'Titres négociables hors régions'}))
            line.append((0,0,{'name':'Intérêts courus'}))
            line.append((0,0,{'name':'Autres valeurs assimilées'}))
            line.append((0,0,{'name':'TOTAL BRUT TITRES'}))
            line.append((0,0,{'name':'Dépréciations des titres'}))
            line.append((0,0,{'name':'TOTAL NET DEPRECIATION'}))
            self.note9_lines = line

    @api.onchange("note10")
    def onchange_note10(self):
        line = []
        if self.note10 is True:
            line.append((0,0,{'name':'Effets à encaisser'}))
            line.append((0,0,{'name':'Effets à l’encaissement'}))
            line.append((0,0,{'name':'Chéques à encaisser'}))
            line.append((0,0,{'name':'Chéques à l’encaissement'}))
            line.append((0,0,{'name':'Cartes de crédit à encaisser'}))
            line.append((0,0,{'name':'Autres valeurs à encaisser'}))
            line.append((0,0,{'name':'TOTAL BRUT VALEURS A ENCAISSER'}))
            line.append((0,0,{'name':'Dépréciations des valeurs à encaisser'}))
            line.append((0,0,{'name':'TOTAL NET DEPRECIATION'}))
            self.note10_lines = line


    @api.onchange("note11")
    def onchange_note11(self):
        line = []
        if self.note11 is True:
            line.append((0,0,{'name':'Banques locales'}))
            line.append((0,0,{'name':'Banques autres états région'}))
            line.append((0,0,{'name':'Banques, dépôt à terme'}))
            line.append((0,0,{'name':'Autres Banques'}))
            line.append((0,0,{'name':'anques intérêts courus'}))
            line.append((0,0,{'name':'Chéques postaux'}))
            line.append((0,0,{'name':'Autres établissements financiers'}))
            line.append((0,0,{'name':'ements financiers interêts courus'}))
            line.append((0,0,{'name':'ruments de trésorerie'}))
            line.append((0,0,{'name':'Caisse'}))
            line.append((0,0,{'name':'Caisse électronique mobile'}))
            line.append((0,0,{'name':'Régies d’avance et virements accréditifs'}))
            line.append((0,0,{'name':'TOTAL BRUT DISPONIBLE'}))
            line.append((0,0,{'name':'Dépréciations'}))
            line.append((0,0,{'name':'TOTAL NET DEPRECIATION'}))
            self.note11_lines = line

    @api.onchange("note12")
    def onchange_note12(self):
        line = []
        line2 = []
        if self.note12 is True:
            line.append((0,0,{'name':'Ecarts de conversion actif : détailler les créance'}))
            line.append((0,0,{'name':' '}))
            line.append((0,0,{'name':' '}))
            line.append((0,0,{'name':' '}))
            line.append((0,0,{'name':'Ecarts de conversion passif : détailler les créance'}))
            line.append((0,0,{'name':' '}))
            line.append((0,0,{'name':' '}))
            line.append((0,0,{'name':' '}))
            self.note12_lines1 = line

            line2.append((0,0,{'name':'Transferts de charges d’exploitation : détailler la nature des charges transférées'}))
            line2.append((0,0,{'name':' '}))
            line2.append((0,0,{'name':' '}))
            line2.append((0,0,{'name':' '}))
            line2.append((0,0,{'name':'Transferts de charges financiéres : détailler la nature des charges transférées'}))
            line2.append((0,0,{'name':' '}))
            line2.append((0,0,{'name':' '}))
            line2.append((0,0,{'name':' '}))
            self.note12_lines2 = line2


    @api.onchange("note13")
    def onchange_note13(self):
        line = []
        if self.note13 is True:
            line.append((0,0,{'Nature_des_actions':'TOTAL'}))
            self.note13_lines = line


    @api.onchange("note14")
    def onchange_note14(self):
        line = []
        if self.note14 is True:
            line.append((0,0,{'name':'Primes d’apport'}))
            line.append((0,0,{'name':'Primes d’émission'}))
            line.append((0,0,{'name':'Primes de fusion'}))
            line.append((0,0,{'name':'Primes de conversion'}))
            line.append((0,0,{'name':'Autres primes'}))
            line.append((0,0,{'name':'TOTAL PRIMES'}))
            line.append((0,0,{'name':'Réserves légales'}))
            line.append((0,0,{'name':'Réserves statutaires'}))
            line.append((0,0,{'name':'Réserves de plus-values nettes à long terme'}))
            line.append((0,0,{'name':'d’attribution gratuite d’action au personnel salarié et aux dirigeants'}))
            line.append((0,0,{'name':'Autres réserves réglementées'}))
            line.append((0,0,{'name':'TOTAL RESERVES INDISPONIBLES'}))
            line.append((0,0,{'name':'Réserves libres'}))
            line.append((0,0,{'name':'Report à nouveau'}))
            self.note14_lines = line



    @api.onchange("note15A")
    def onchange_note15A(self):
        line = []
        if self.note15A is True:
            line.append((0,0,{'name':'Etat'}))
            line.append((0,0,{'name':'Régions'}))
            line.append((0,0,{'name':'Départements'}))
            line.append((0,0,{'name':'Communes et collectivités publiques décentralisées'}))
            line.append((0,0,{'name':'Entités publiques ou mixtes'}))
            line.append((0,0,{'name':'Entités et organismes privés'}))
            line.append((0,0,{'name':'Organismes internationaux'}))
            line.append((0,0,{'name':'Autres'}))
            line.append((0,0,{'name':'Amortissements dérogatoires'}))
            line.append((0,0,{'name':'Plus-value de cession à réinvertir'}))
            line.append((0,0,{'name':'Provisions spéciales de réévaluation'}))
            line.append((0,0,{'name':'Provisions réglementées relatives aux immobilisations'}))
            line.append((0,0,{'name':'Provisions réglementées relatives aux stocks' }))
            line.append((0,0,{'name':'Provisions pour investissement'}))
            line.append((0,0,{'name':'Autres provisions et fonds reglementés' }))
            line.append((0,0,{'name':'TOTAL SUBVENTIONS'}))
            line.append((0,0,{'name':'TOTAL PROVISIONS REGLEMENTEES' }))
            line.append((0,0,{'name':'TOTAL SUBVENTIONS ET PROVISIONS REGLEMENTEES'}))
            line.append((0,0,{'name':'TOTAL SUBVENTIONS ET PROVISIONS REGLEMENTEES 0' }))
            self.note15A_lines = line


    @api.onchange("note15B")
    def onchange_note15B(self):
        line = []
        if self.note15B is True:
            line.append((0,0,{'name':'Titres participatifs'}))
            line.append((0,0,{'name':'Avances conditionnées'}))
            line.append((0,0,{'name':'Titres subordonnés à durée indéterminée (T.S.D.I)'}))
            line.append((0,0,{'name':'Obligations remboursables en action (O.R.A)'}))
            line.append((0,0,{'name':'Autres'}))
            line.append((0,0,{'name':'TOTAL AUTRES FONDS PROPRES'}))
            self.note15B_lines = line


    @api.onchange("note16A")
    def onchange_note16A(self):
        line = []
        if self.note16A is True:
            line.append((0,0,{'name':'Emrpunts obligataires'}))
            line.append((0,0,{'name':'Emprunt et dettes auprés des établissements de crédit'}))
            line.append((0,0,{'name':'Avances reçues de l’Etat'}))
            line.append((0,0,{'name':'Dépôts et cautionnement reçus'}))
            line.append((0,0,{'name':'Intérêts courrus'}))
            line.append((0,0,{'name':'Avances assorties de conditions particulières'}))
            line.append((0,0,{'name':'Autres emprunts et dettes'}))
            line.append((0,0,{'name':'Dettes lièes à des participations'}))
            line.append((0,0,{'name':'Comptes permanents bloqués des établissements et succursales'}))
            line.append((0,0,{'name':'TOTAL EMPRUNTS ET DETTES FINANCIERES'}))
            line.append((0,0,{'name':'Crédit bail mobilier'}))
            line.append((0,0,{'name':'Crédit bail immobilier'}))
            line.append((0,0,{'name':'Intérêts courrus'}))
            line.append((0,0,{'name':'Autres locations acquisitions'}))
            line.append((0,0,{'name':'Location - Vente'}))
            line.append((0,0,{'name':'TOTAL DETTES DE LOCATION ACQUISITION'}))
            line.append((0,0,{'name':'Provisions pour litiges'}))
            line.append((0,0,{'name':'garanties données aux clients'}))
            line.append((0,0,{'name':'Provisions pour pertes sur marchés à achèvement futur'}))
            line.append((0,0,{'name':'Provisions pour perte de change'}))
            line.append((0,0,{'name':'Provisions pour impôts'}))
            line.append((0,0,{'name':'Provisions pour pensions et obligations assimilées'}))
            line.append((0,0,{'name':'Actif du régime de retraite'}))
            line.append((0,0,{'name':'Provisions pour amendes et pénalités'}))
            line.append((0,0,{'name':'Provisons pour assureur propre'}))
            line.append((0,0,{'name':'Provisions pour démantèlement et remise en état'}))
            line.append((0,0,{'name':'Autres provisions'}))
            line.append((0,0,{'name':'Provisions pour restructuration'}))
            line.append((0,0,{'name':'Provisions de droits à déduction'}))
            line.append((0,0,{'name':'TAL PROVISIONS FINANCIERES POUR RISQUES ET CHARGES'}))
            self.note16A_lines = line


    @api.onchange("note16B")
    def onchange_note16B(self):
        line = []
        line2 = []
        line3 = []
        if self.note16B is True:
            line.append((0,0,{'name':'Taux d’augmentation des salaires'}))
            line.append((0,0,{'name':'Taux d’actualisation'}))
            line.append((0,0,{'name':'Taux d’inflation'}))
            line.append((0,0,{'name':'Probabilité d’être dans l’entité à la date de départ à la retraite'}))
            line.append((0,0,{'name':'Probabilité d’être en vie à lâge de départ à la retraite (table de mortalité)'}))
            line.append((0,0,{'name':'Taux de rendement effectif des actifs du régime'}))
            self.note16BTab1_lines = line

            line2.append((0,0,{'name':'Obligation au titre des engagements de retraite à l’ouverture'}))
            line2.append((0,0,{'name':'Coût des services rendus a cours de l’exercice'}))
            line2.append((0,0,{'name':'Coût financier'}))
            line2.append((0,0,{'name':'Perte actuarielles / (gain)'}))
            line2.append((0,0,{'name':'Prestations payées au cours de l’exercice'}))
            line2.append((0,0,{'name':'Coût des services passés'}))
            line2.append((0,0,{'name':'Obligation au titre des engagements de retraite à clôture'}))
            self.note16BTab2_lines = line2

            line3.append((0,0,{'name':'Taux d’actualisation (variation de ... %)'}))
            line3.append((0,0,{'name':'Taux de progression des salaires (variation de ... %)'}))
            line3.append((0,0,{'name':'Taux de départ du personnel (variation de ...%)'}))
            self.note16BTab3_lines = line3


    @api.onchange("note16B_BIS")
    def onchange_note16BBIS(self):
        line = []
        line2 = []
        if self.note16B_BIS is True:
            line.append((0,0,{'name':'Valeur actuelle de l’obligation résultant de régimes financés'}))
            line.append((0,0,{'name':'Valeur actuelle des actifs affectés aux plans de retraite'}))
            self.note16BBISTab1_lines = line

            line2.append((0,0,{'name':'Actions'}))
            line2.append((0,0,{'name':'Obligations'}))
            line2.append((0,0,{'name':'Autres'}))
            self.note16BBISTab2_lines = line2


    @api.onchange("note16C")
    def onchange_note16C(self):
        line = []
        if self.note16C is True:
            line.append((0,0,{'name':'Actif éventuel'}))
            line.append((0,0,{'name':'Litiges'}))
            line.append((0,0,{'name':'............'}))
            line.append((0,0,{'name':'............'}))
            line.append((0,0,{'name':'............'}))
            line.append((0,0,{'name':'............'}))
            line.append((0,0,{'name':'Passif éventuel'}))
            line.append((0,0,{'name':'Litiges'}))
            line.append((0,0,{'name':'............'}))
            line.append((0,0,{'name':'............'}))
            line.append((0,0,{'name':'............'}))
            line.append((0,0,{'name':'............'}))
            self.note16C_lines = line


    @api.onchange("note17")
    def onchange_note17(self):
        line = []
        if self.note17 is True:
            line.append((0,0,{'name':'Fournisseurs dettes en comptes (hors groupe)'}))
            line.append((0,0,{'name':'Fournisseurs effet à payer (hors groupe)'}))
            line.append((0,0,{'name':'Fournisseurs, dettes et effet à payer groupe'}))
            line.append((0,0,{'name':'Fournisseurs factures non parvenues (horsgroupe)'}))
            line.append((0,0,{'name':'Fournisseurs factures non parvenues groupe'}))
            line.append((0,0,{'name':'TOTAL FOURNISSEURS'}))
            line.append((0,0,{'name':'Fournisseurs, avanves et accompte (horsgroupe)'}))
            line.append((0,0,{'name':'Fournisseurs, avanves et accompte groupe'}))
            line.append((0,0,{'name':'Fournisseurs, avanves et accompte (horsgroupe)'}))
            line.append((0,0,{'name':'TOTAL FOURNISSEURS DEBITEURS'}))
            self.note17_lines = line


    @api.onchange("note18")
    def onchange_note18(self):
        line = []
        if self.note18 is True:
            line.append((0,0,{'name':'Personnel avances et accomptes'}))
            line.append((0,0,{'name':'Personnel rémunérations dues'}))
            line.append((0,0,{'name':'Autres personnel'}))
            line.append((0,0,{'name':'Caisse de sécurité sociale'}))
            line.append((0,0,{'name':'Caisse de retraite'}))
            line.append((0,0,{'name':'Autres organismes sociaux'}))
            line.append((0,0,{'name':'TOTAL DETTES SOCIALES'}))
            line.append((0,0,{'name':'Etat, impôts sur les bénéfices'}))
            line.append((0,0,{'name':'Etats, impôts et taxes'}))
            line.append((0,0,{'name':'Etat, TVA'}))
            line.append((0,0,{'name':'Etat, impôts retenus à la source'}))
            line.append((0,0,{'name':'Autres dettes Etat'}))
            line.append((0,0,{'name':'TOTAL DETTES FISCALES'}))
            line.append((0,0,{'name':'TOTAL DETTES SOCIALES ET FISCALES'}))
            self.note18_lines = line


    @api.onchange("note19")
    def onchange_note19(self):
        line = []
        if self.note19 is True:
            line.append((0,0,{'name':'Organismes internationaux'}))
            line.append((0,0,{'name':'Apporteurs, opérations sur le capital'}))
            line.append((0,0,{'name':'Associés, compte'}))
            line.append((0,0,{'name':'Associés dividendes à payer'}))
            line.append((0,0,{'name':'Groupe, comptes courants'}))
            line.append((0,0,{'name':'Autres dettes associés'}))
            line.append((0,0,{'name':'TOTAL DETTES ASSOCIES'}))
            line.append((0,0,{'name':'Créditeurs divers'}))
            line.append((0,0,{'name':'Obligataires'}))
            line.append((0,0,{'name':'Rémunération d’administrateurs'}))
            line.append((0,0,{'name':'Compte du factor'}))
            line.append((0,0,{'name':'Versements restant à effectuer sur titre de déplacement non libérés'}))
            line.append((0,0,{'name':'Compte transitoire ajustement spécial lié à la révision SYSCOHADA'}))
            line.append((0,0,{'name':'Autres créditeur divers'}))
            line.append((0,0,{'name':'TOTAL CREDITEURS DIVERS'}))
            line.append((0,0,{'name':'Comptes permanents non bloqués des établissements et des succursales'}))
            line.append((0,0,{'name':'Comptes de liaison charges et produits'}))
            line.append((0,0,{'name':'Comptes de liaison des sociétés en participation'}))
            line.append((0,0,{'name':'TOTAL COMPTE DE LIAISON'}))
            line.append((0,0,{'name':'Provisions pour risques à court terme (voir note 28)'}))
            self.note19_lines = line


    @api.onchange("note20")
    def onchange_note20(self):
        line = []
        if self.note20 is True:
            line.append((0,0,{'name':'Escomptes de crédit de campagne'}))
            line.append((0,0,{'name':'Escomptes de crédit ordinaire'}))
            line.append((0,0,{'name':'TOTAL : BANQUES, CREDITS D’ESCOMPTE ET DE TRESORERIE'}))
            line.append((0,0,{'name':'Banques locales'}))
            line.append((0,0,{'name':'Banques autres états région'}))
            line.append((0,0,{'name':'Autres Banques'}))
            line.append((0,0,{'name':'Banques intérêts courus'}))
            line.append((0,0,{'name':'Crédit de trésorerie'}))
            line.append((0,0,{'name':'TOTAL : BANQUES, CREDITS DE TRESORERIE'}))
            line.append((0,0,{'name':''}))
            line.append((0,0,{'name':'TOTAL GENERAL'}))
            self.note20_lines = line

    @api.onchange("note21")
    def onchange_note21(self):
        line = []


        if self.note21 is True:
            line.append((0,0,{'name':'Ventes dans la Région'}))
            line.append((0,0,{'name':'Vente hors Région'}))
            line.append((0,0,{'name':'Vente groupe'}))
            line.append((0,0,{'name':'Ventes sur internet'}))
            line.append((0,0,{'name':'TOTAL : VENTES DE MARCHANDISES'}))
            line.append((0,0,{'name':''}))
            line.append((0,0,{'name':'Ventes dans la Région'}))
            line.append((0,0,{'name':'Vente hors Région'}))
            line.append((0,0,{'name':'Vente groupe'}))
            line.append((0,0,{'name':'Ventes sur internet'}))
            line.append((0,0,{'name':'TOTAL : VENTES DE PRODUITS FABRIQUES'}))
            line.append((0,0,{'name':''}))
            line.append((0,0,{'name':'Ventes dans la Région'}))
            line.append((0,0,{'name':'Vente hors Région'}))
            line.append((0,0,{'name':'Vente groupe'}))
            line.append((0,0,{'name':'Ventes sur internet'}))
            line.append((0,0,{'name':'TOTAL : VENTES DE TRAVAUX ET SERVICES VENDUS'}))
            line.append((0,0,{'name':''}))
            line.append((0,0,{'name':'Produits accessoires'}))
            line.append((0,0,{'name':'TOTAL : CHIFFRES D’AFFAIRE'}))
            line.append((0,0,{'name':''}))
            line.append((0,0,{'name':'Production immobilisée'}))
            line.append((0,0,{'name':'ubvention d’exploitation'}))
            line.append((0,0,{'name':'Autres produits'}))
            line.append((0,0,{'name':'TOTAL : AUTRES PRODUITS'}))
            line.append((0,0,{'name':''}))
            line.append((0,0,{'name':'TOTAL'}))

            self.note21_lines = line


    @api.onchange("note22")
    def onchange_note22(self):
        line = []


        if self.note22 is True:
            line.append((0,0,{'name':'Achats dans la Région'}))
            line.append((0,0,{'name':'Achats hors Région'}))
            line.append((0,0,{'name':'Achats groupe'}))
            line.append((0,0,{'name':'TOTAL : ACHATS DE MARCHANDISES'}))
            line.append((0,0,{'name':'TOTAL : ACHATS DE MARCHANDISES'}))
            line.append((0,0,{'name':'Achats dans la Région'}))
            line.append((0,0,{'name':'Achats hors Région'}))
            line.append((0,0,{'name':'Achats groupe'}))
            line.append((0,0,{'name':'TOTAL : ACHATS MATIERES PREMIERES ET FOURNITURES LIEES'}))
            line.append((0,0,{'name':'Matiéres consommables'}))
            line.append((0,0,{'name':'Matiéres combustibles'}))
            line.append((0,0,{'name':'Produit d’entretien'}))
            line.append((0,0,{'name':'Fournitures d’atelier, d’usine et de magasin'}))
            line.append((0,0,{'name':'Eaux'}))
            line.append((0,0,{'name':'Electricité'}))
            line.append((0,0,{'name':'Autres énergies'}))
            line.append((0,0,{'name':'Fourniture d’entretien'}))
            line.append((0,0,{'name':'Fourniture de bureau'}))
            line.append((0,0,{'name':'Petit matériel et outillages produits'}))
            line.append((0,0,{'name':'Achats études, prestation de services, de travaux matériels et équipements'}))
            line.append((0,0,{'name':'Frais sur achats'}))
            line.append((0,0,{'name':'Remises, rabais, remises et ristournes'}))
            line.append((0,0,{'name':'TOTAL : AUTRES ACHATS'}))


            self.note22_lines = line


    @api.onchange("note23")
    def onchange_note23(self):
        line = []


        if self.note23 is True:
            line.append((0,0,{'name':'Transport sur ventes'}))
            line.append((0,0,{'name':'Transport pour le compte de tiers'}))
            line.append((0,0,{'name':'Transport du personnel'}))
            line.append((0,0,{'name':'Transport de plis'}))
            line.append((0,0,{'name':'Autres transport'}))
            line.append((0,0,{'name':'TOTAL'}))

            self.note23_lines = line

    @api.onchange("note24")
    def onchange_note24(self):
        line = []


        if self.note24 is True:
            line.append((0,0,{'name':'Sous-traitance générale'}))
            line.append((0,0,{'name':'Locations et charges locatives'}))
            line.append((0,0,{'name':'Redevances de location acquisition'}))
            line.append((0,0,{'name':'Entretien, réparations et maintenance'}))
            line.append((0,0,{'name':'Primes d’assurances'}))
            line.append((0,0,{'name':'Etudes, recherches et documentation'}))
            line.append((0,0,{'name':'Publicité, publication, relations publiques'}))
            line.append((0,0,{'name':'Frais de télécommunication'}))
            line.append((0,0,{'name':'Frais bancaires'}))
            line.append((0,0,{'name':'Rémunération d’intermédiaires et de conseils'}))
            line.append((0,0,{'name':'Frais de formation du persoonel'}))
            line.append((0,0,{'name':'ances pour brevets, licences, logiciels, concession et droit similaires'}))
            line.append((0,0,{'name':'Cotisations'}))
            line.append((0,0,{'name':'Autres charges externes'}))
            line.append((0,0,{'name':'TOTAL'}))


            self.note24_lines = line

    @api.onchange("note25")
    def onchange_note25(self):
        line = []


        if self.note25 is True:
            line.append((0,0,{'name':'Impôts et taxe directs'}))
            line.append((0,0,{'name':'Impôts et taxe indirects'}))
            line.append((0,0,{'name':'Droits d’enregistrement'}))
            line.append((0,0,{'name':'Pénalités et amendes fiscales'}))
            line.append((0,0,{'name':'Autres impôts et taxes'}))
            line.append((0,0,{'name':'TOTAL'}))


            self.note25_lines = line

    @api.onchange("note26")
    def onchange_note26(self):
        line = []


        if self.note26 is True:
            line.append((0,0,{'name':'Pertes sur créances clients'}))
            line.append((0,0,{'name':'Pertes sur autres débiteurs'}))
            line.append((0,0,{'name':'Quote-part de résultat sur opération faite en commun'}))
            line.append((0,0,{'name':'Valeur comptable des cessions courantes d’immobilisations'}))
            line.append((0,0,{'name':'Indemnités de fonction et autres rémunérations d’administrateurs'}))
            line.append((0,0,{'name':'Dons et mécénat'}))
            line.append((0,0,{'name':'Autres charges divers'}))
            line.append((0,0,{'name':'Charges pour dépréciation et provisions pour risques à court terme d’exploitation (voir note 28)'}))
            line.append((0,0,{'name':'TOTAL'}))


            self.note26_lines = line

    @api.onchange("note27A")
    def onchange_note27A(self):
        line = []


        if self.note27A is True:
            line.append((0,0,{'name':'Rémunérations directes versées au personnel'}))
            line.append((0,0,{'name':'Indémnité de logement'}))
            line.append((0,0,{'name':'Prime de transport'}))
            line.append((0,0,{'name':'Autres primes'}))
            line.append((0,0,{'name':'Charges sociales'}))
            line.append((0,0,{'name':'Médecine du travail'}))
            line.append((0,0,{'name':'Equipement du personnel'}))
            line.append((0,0,{'name':'TOTAL'}))

            self.note27A_lines = line


    @api.onchange("note28")
    def onchange_note28(self):
        line = []
        if self.note28 is True:
            line.append((0,0,{'name':'Provisions réglementées'}))
            line.append((0,0,{'name':'Provisions financiéres pour risques et charges'}))
            line.append((0,0,{'name':'Dépréciations des immobilisations'}))
            line.append((0,0,{'name':'TOTAL : DOTATIONS'}))
            line.append((0,0,{'name':'Dépréciations des stocks'}))
            line.append((0,0,{'name':'Dépréciations actif circulant HAO'}))
            line.append((0,0,{'name':'BDépréciations fournisseurs'}))
            line.append((0,0,{'name':'Dépréciations clients'}))
            line.append((0,0,{'name':'Dépréciations autres créances'}))
            line.append((0,0,{'name':'Dépréciations titres de placement'}))
            line.append((0,0,{'name':'Dépréciations valeurs à encaisser'}))
            line.append((0,0,{'name':'Dépréciations disponibilité'}))
            line.append((0,0,{'name':'Dépréciations et provisions pour risques à court termes exploitation'}))
            line.append((0,0,{'name':'Dépréciations et provisions pour risques à court termes à caractére financier'}))
            line.append((0,0,{'name':'TOTAL: CHARGE POUR DEPRECIATIONS ET PROVISIONS A COURT TERME'}))
            line.append((0,0,{'name':'TOTAL'}))
            self.note28_lines = line

    @api.onchange("note29")
    def onchange_note29(self):
        line = []
        if self.note29 is True:
            line.append((0,0,{'name':'Intérêts des emprunts'}))
            line.append((0,0,{'name':'Intérêts dans loyers de location acquisition'}))
            line.append((0,0,{'name':'Escomptes accordés'}))
            line.append((0,0,{'name':'Autres intérêts'}))
            line.append((0,0,{'name':'Escomptes des effets de commerce'}))
            line.append((0,0,{'name':'Pertes de change'}))
            line.append((0,0,{'name':'Perte sur cessions de titre de placement'}))
            line.append((0,0,{'name':'Malis provenant d’attribution gratuite d’actions au personnel salarié et aux dirigeants'}))
            line.append((0,0,{'name':'Pertes sur risques financiers'}))
            line.append((0,0,{'name':'Charges pour dépréciation et provisions à court terme à caractére financier (voir note 28)'}))
            line.append((0,0,{'name':'SOUS TOTAL : FRAIS FINANCIERS'}))
            line.append((0,0,{'name':'Intérêts de prêts et créances diverses'}))
            line.append((0,0,{'name':'Revenus de participation'}))
            line.append((0,0,{'name':'Escomptes obtenus'}))
            line.append((0,0,{'name':'Gains de change'}))
            line.append((0,0,{'name':'Gains sur cessions de titres de placement'}))
            line.append((0,0,{'name':'Gains sur risques financiers'}))
            line.append((0,0,{'name':'Reprises de charges pour dépréciation et provisions à court terme à caractére financier (voir note 28)'}))
            line.append((0,0,{'name':'SOUS TOTAL : REVENUS FINANCIERS'}))
            self.note29_lines = line

    @api.onchange("note30")
    def onchange_note30(self):
        line = []
        if self.note30 is True:
            line.append((0,0,{'name':'Charges HAO constatées (1) à détailler'}))
            line.append((0,0,{'name':'(1) ...........................................................'}))
            line.append((0,0,{'name':'(1) ...........................................................'}))
            line.append((0,0,{'name':'(1) ...........................................................'}))
            line.append((0,0,{'name':'Perte sur créances HAO'}))
            line.append((0,0,{'name':'Dons et libéralités accordés'}))
            line.append((0,0,{'name':'Abandon de créances consentis'}))
            line.append((0,0,{'name':'Charges provisionneées HAO'}))
            line.append((0,0,{'name':'Dotation hors activités ordinaires'}))
            line.append((0,0,{'name':'Participation des travailleurs'}))
            line.append((0,0,{'name':'Subvention d’équilibre'}))
            line.append((0,0,{'name':'SOUS TOTAL: AUTRES CHARGES HAO'}))
            line.append((0,0,{'name':'Produits HAO constatés (1) à détailler'}))
            line.append((0,0,{'name':'(1) ...........................................................'}))
            line.append((0,0,{'name':'(1) ...........................................................'}))
            line.append((0,0,{'name':'(1) ...........................................................'}))
            line.append((0,0,{'name':'Dons et libéralités obtenus'}))
            line.append((0,0,{'name':'Abandon de créances obtenus'}))
            line.append((0,0,{'name':'Transferts de charges HAO'}))
            line.append((0,0,{'name':'Reprises des charges pour dépréciations et provisions à court terme HAO'}))
            line.append((0,0,{'name':'Reprises hors activités ordinaire'}))
            line.append((0,0,{'name':'SOUS TOTAL : AUTRES PRODUITS HAO'}))
            line.append((0,0,{'name':'TOTAL'}))
            self.note30_lines = line

    @api.onchange("note31")
    def onchange_note31(self):
        line = []
        if self.note31 is True:
            line.append((0,0,{'name':'STRUCTURE DU CAPITAL A LA CLOTURE DE L’EXERCICE'}))
            line.append((0,0,{'name':'Capital social'}))
            line.append((0,0,{'name':'Actions ordinaires'}))
            line.append((0,0,{'name':'Actions et dividendes prioritaires (A.D.P) sans droit de vote'}))
            line.append((0,0,{'name':'Actions nouvelles à émettre :'}))
            line.append((0,0,{'name':'        -par conversion d’obligations'}))
            line.append((0,0,{'name':'        -par exercice de droits de souscription'}))
            line.append((0,0,{'name':'OPERATIONS ET RESULTAT DE L’EXERCICE'}))
            line.append((0,0,{'name':'Résultat des activités ordinaires (R.A.O) hors dotations et reprises (exploitation et financiére)'}))
            line.append((0,0,{'name':'Participaton des travailleurs aux bénéfices'}))
            line.append((0,0,{'name':'Impôt sur le résultat'}))
            line.append((0,0,{'name':'Résultat net'}))
            line.append((0,0,{'name':'RESULTAT ET DIVIDENDES DISTRIBUES'}))
            line.append((0,0,{'name':'Résultat distribué'}))
            line.append((0,0,{'name':'Dividende attribuée à chaque action'}))
            line.append((0,0,{'name':'PERSONNEL ET POLITIQUE SALARIALE'}))
            line.append((0,0,{'name':'Effectif moyen personnel extérieur'}))
            line.append((0,0,{'name':'Masse salariale distribuée au cours de l’exercice'}))
            line.append((0,0,{'name':'Avantages sociaux versés au cours de l’exercice [Sécurité sociale, oeuvres sociales]'}))
            line.append((0,0,{'name':'Personnel extérieur facturé à l’entité'}))
            self.note31_lines = line

    @api.onchange("note32")
    def onchange_note32(self):
        line = []
        if self.note32 is True:
            line.append((0,0,{'name':''}))
            line.append((0,0,{'name':''}))
            line.append((0,0,{'name':''}))
            line.append((0,0,{'name':''}))
            line.append((0,0,{'name':''}))
            line.append((0,0,{'name':''}))
            line.append((0,0,{'name':''}))
            line.append((0,0,{'name':''}))
            line.append((0,0,{'name':'NON VENTILLE'}))
            line.append((0,0,{'name':'TOTAL'}))
            self.note32_lines = line

    @api.onchange("note33")
    def onchange_note33(self):
        line = []
        if self.note33 is True:
            line.append((0,0,{'name':''}))
            line.append((0,0,{'name':'TOTAL'}))
            self.note33_lines = line

    @api.onchange("note34")
    def onchange_note34(self):
        line = []
        if self.note34 is True:
            line.append((0,0,{'name':'Chiffre d’affaires'}))
            line.append((0,0,{'name':'Marge commerciale'}))
            line.append((0,0,{'name':'Valeur ajoutée'}))
            line.append((0,0,{'name':'Excédent Brut d’exploitation (EBE)'}))
            line.append((0,0,{'name':'Résultat d’exploitation'}))
            line.append((0,0,{'name':'Résultat financier'}))
            line.append((0,0,{'name':'Résultat des activités ordinaires'}))
            line.append((0,0,{'name':'Résultat hors activités ordinaires'}))
            line.append((0,0,{'name':'Résultat net'}))
            line.append((0,0,{'name':'DETERMINATION DE LA CAPACITE D’AUTOFINANCEMENT'}))
            line.append((0,0,{'name':'Exédent brut d’exploitation'}))
            line.append((0,0,{'name':'+ Revenus financiers'}))
            line.append((0,0,{'name':'+ Produis HAO'}))
            line.append((0,0,{'name':'- Frais financiers'}))
            line.append((0,0,{'name':'- Impôt sur les résultats'}))
            line.append((0,0,{'name':'= CAPACITE D’AUTOFINANCEMENT GLOBALE (C.A.F.G)'}))
            line.append((0,0,{'name':'- Distributions de dividendes opérées durant l’exercice'}))
            line.append((0,0,{'name':'= AUTOFINANCEMENT'}))
            line.append((0,0,{'name':'ANALYSE DE LA RENTABILITE'}))
            line.append((0,0,{'name':'Rentabilité économique = Résultat d’exploitation (a) / Capitaux propres + dettes financières (%)'}))
            line.append((0,0,{'name':'Rentabilité financière = Résultat net / Capitaux propres (%)'}))
            line.append((0,0,{'name':'ANALYSE DE LA Structure FINANCIERE'}))
            line.append((0,0,{'name':'+ Capitaux propres et ressources assimilées'}))
            line.append((0,0,{'name':'+ Dettes financières* et autres ressources assimilées (b)'}))
            line.append((0,0,{'name':'= Ressources stables'}))
            line.append((0,0,{'name':'- Actif immobilisé'}))
            line.append((0,0,{'name':'= FONDS DE ROULEMENT (1)'}))
            line.append((0,0,{'name':'+ Actif circulant d’exploitation (b)'}))
            line.append((0,0,{'name':'- Passif circulant d’exploitation (b)'}))
            line.append((0,0,{'name':'+ Actif circulant HAO'}))
            line.append((0,0,{'name':'- Passif circulant HAO'}))
            line.append((0,0,{'name':'= BESOIN DE FINANCEMENT HAO (3)E'}))
            line.append((0,0,{'name':'BESOIN DE FINANCEMENT GLOBAL (4) = (2) + (3)'}))
            line.append((0,0,{'name':'TRESORERIE NETTE(5) = (1) - (4)'}))
            line.append((0,0,{'name':'CONTRÔLE : TRESORERIE NETTTE = (TRESORERIE - ACTIF) - (TRESORERIE - PASSIF)'}))
            line.append((0,0,{'name':'ANALYSE DE LA VARIATION DE LA TRESORERIE'}))
            line.append((0,0,{'name':'Flux de trésorerie des activités opérationnelles'}))
            line.append((0,0,{'name':'- Flux de trésorerie des activités d’investissement'}))
            line.append((0,0,{'name':'+ Flux de trésorerie des actitivtés de financement'}))
            line.append((0,0,{'name':'= VARIATION DE LA TRESORERIE NETTE DE LA PERIODE'}))
            line.append((0,0,{'name':'ANALYSE DE LA VARIATION de L’ENDETTEMENT FINANCIER NET'}))
            line.append((0,0,{'name':'Endettement financier brut (Dettes financières + Trésorerie - passif)'}))
            line.append((0,0,{'name':'- Trésoreie - actif'}))
            line.append((0,0,{'name':'= ENDETTEMENT FINANCIER NET'}))
            line.append((0,0,{'name':'SOLDES INTERMEDIAIRES DE GESTION'}))
            self.note34_lines = line

    @api.onchange("note37")
    def onchange_note37(self):
        line = []
        if self.note37 is True:
            line.append((0,0,{'name':'1 : RESULTAT NET COMPTABLE DE LEXERCICE'}))
            line.append((0,0,{'name':''}))
            line.append((0,0,{'name':'2 : A REINTEGRER'}))
            line.append((0,0,{'name':'Impôt sur le résultat'}))
            line.append((0,0,{'name':'...........................................'}))
            line.append((0,0,{'name':'...........................................'}))
            line.append((0,0,{'name':'...........................................'}))
            line.append((0,0,{'name':'...........................................'}))
            line.append((0,0,{'name':'...........................................'}))
            line.append((0,0,{'name':'...........................................'}))
            line.append((0,0,{'name':'...........................................'}))
            line.append((0,0,{'name':'...........................................'}))
            line.append((0,0,{'name':'...........................................'}))
            line.append((0,0,{'name':'3 : A DEDUIRE'}))
            line.append((0,0,{'name':'...........................................'}))
            line.append((0,0,{'name':'...........................................'}))
            line.append((0,0,{'name':'...........................................'}))
            line.append((0,0,{'name':'...........................................'}))
            line.append((0,0,{'name':'...........................................'}))
            line.append((0,0,{'name':'...........................................'}))
            line.append((0,0,{'name':'...........................................'}))
            line.append((0,0,{'name':'...........................................'}))
            line.append((0,0,{'name':'...........................................'}))
            line.append((0,0,{'name':'...........................................'}))
            line.append((0,0,{'name':'4 : RESULTAT IMPOSABLE AVANT DEDUCTION DES DEFICITES (4=1+2-3)'}))
            line.append((0,0,{'name':''}))
            line.append((0,0,{'name':'...........................................'}))
            line.append((0,0,{'name':'...........................................'}))
            line.append((0,0,{'name':'...........................................'}))
            line.append((0,0,{'name':'...........................................'}))
            line.append((0,0,{'name':'6 : AMORTISSEMENTS REGULIEREMENT DIFFERES'}))
            line.append((0,0,{'name':'...........................................'}))
            line.append((0,0,{'name':'...........................................'}))
            line.append((0,0,{'name':'...........................................'}))
            line.append((0,0,{'name':'...........................................'}))
            line.append((0,0,{'name':'7 : AMORTISSEMENTS DE L’EXERCICE A DIFFERERE'}))
            line.append((0,0,{'name':'...........................................'}))
            line.append((0,0,{'name':''}))
            line.append((0,0,{'name':'8 : RESULTAT FISCAL DE L’EXERCICE (8=4-5-6+7)'}))
            line.append((0,0,{'name':''}))
            line.append((0,0,{'name':'9 : IMPOTS SUR LE RESULTAT AU TAUX DE ....'}))
            self.note37_lines = line




class OptesisNote1Tab1(models.Model):
    _name = "optesis.note1.tab1"

    name = fields.Char("Libelle")
    montant = fields.Char("Montant brut")
    note = fields.Char("Note")
    hypo = fields.Char("Hypotheques")
    nant = fields.Char("Nantissements")
    gage = fields.Char("Gages / autres")
    note_id = fields.Many2one("optesis.note", ondelete='cascade')


class OptesisNote1Tab2(models.Model):
    _name = "optesis.note1.tab2"

    name = fields.Char("Libelle")
    eng_dons = fields.Char("Engagements Dons")
    eng_recu = fields.Char("Engagements Dons")
    note_id = fields.Many2one("optesis.note", ondelete='cascade')


class OptesisNote3a(models.Model):
    _name = "optesis.note3a"

    name = fields.Char("RUBRIQUES - SITUATIONS")
    montant_ouverture = fields.Char("MONTANT BRUT A L’OUVERTURE DE L’EXERCICE")
    acqisition = fields.Char("Acquisition Apport Creation")
    virement = fields.Char("Virement poste a poste")
    reevaluation = fields.Char("Suite a une reevaluation pratiquee au cours de l’exercice")
    cession = fields.Char("Cession / Hors service")
    virement2 = fields.Char("Virements de poste a poste")
    montant_cloture = fields.Char("MONTANT BRUT A LA CLOTURE DE L’EXERCICE")
    note_id = fields.Many2one("optesis.note", ondelete='cascade')

class OptesisNote3b(models.Model):
    _name = "optesis.note3b"

    name = fields.Char("SITUATION ET MOUVEMENTS RUBRIQUES")
    nature_contrat = fields.Char("NATURE DU CONTRAT (I;M;A)")
    montant_ouverture = fields.Char("MONTANT BRUT A L’OUVERTURE DE L’EXERCICE")
    acqisition = fields.Char("Acquisition Apport creance")
    virement = fields.Char("Virement de poste a poste")
    reevaluation = fields.Char("Suite a une reevaluation pratiquee au cours de l’exercice")
    cession = fields.Char("Cession Scission Hors service")
    virement2 = fields.Char("Virement de poste a poste")
    montant_cloture = fields.Char("MONTANT BRUT A LA CLOTURE DE L’EXERCICE")
    note_id = fields.Many2one("optesis.note", ondelete='cascade')


class OptesisNote3c(models.Model):
    _name = "optesis.note3c"

    name = fields.Char("SITUATION ET MOUVEMENTS RUBRIQUES")
    amortissement_ouverture = fields.Char("AMORTISSEMENTS CUMULES A L’OUVERTURE DE L’EXERCICE")
    augmentation = fields.Char("AUGMENTATION: DOTATION DE L’EXERCICE")
    diminutions = fields.Char("DIMUNITIONS: Amortissements relatifs aux elements de l’actif")
    amortissement_clorute = fields.Char("CUMUL DES AMORTISSEMENTS A LA CLOTURE DE L’EXERCICE")
    note_id = fields.Many2one("optesis.note", ondelete='cascade')


class OptesisNote3d(models.Model):
    _name = "optesis.note3d"

    name = fields.Char("Libelle")
    montant = fields.Float("MONTANT BRUT")
    amortissement = fields.Float("AMORTISSEMENTS PRATIQUES")
    valeur_compta = fields.Float("VALEUR COMPTABLE NETTE")
    cession = fields.Float("PRIX DE CESSION")
    value = fields.Float("PLUS-VALUE OU MOINS-VALUE")
    note_id = fields.Many2one("optesis.note", ondelete='cascade')


class OptesisNote3e(models.Model):
    _name = "optesis.note3e"

    name = fields.Char("Elements reevalues par postes du bilan")
    montant = fields.Float("Montant couts historiques")
    ecart_provision = fields.Float("Ecarts et provisions speciales de reevaluation")
    note_id = fields.Many2one("optesis.note", ondelete='cascade')


class OptesisNote4Tab1(models.Model):
    _name = "optesis.note4.tab1"

    name = fields.Char("Libelle")
    annee_n = fields.Integer("Annee N")
    annee_n1 = fields.Integer("Annee N-1")
    variation = fields.Float("Variation en %")
    creance1 = fields.Float("Creances a un an au plus")
    creance2 = fields.Float("Creances a plus d’un an et a deux ans au plus")
    creance3 = fields.Float("Creances a plus de deux ans")
    note_id = fields.Many2one("optesis.note", ondelete='cascade')


class OptesisNote4Tab2(models.Model):
    _name = "optesis.note4.tab2"

    name = fields.Char("Denomination sociale")
    localisation = fields.Char("Localisation (Ville / Pays)")
    valeur_acquisition = fields.Float("Valeur d’acquisition")
    detenu = fields.Float("% Detenu")
    montant = fields.Float("Montant des capitaux propres filiale")
    resultat = fields.Float("Resultat dernier exrcice filiale")
    note_id = fields.Many2one("optesis.note", ondelete='cascade')


class OptesisNote5Tab1(models.Model):
    _name = "optesis.note5.tab1"

    name = fields.Char("Libelles")
    annee_n = fields.Integer("Annee N")
    annee_n1 = fields.Integer("Annee N-1")
    variation = fields.Float("Variation en %")
    note_id = fields.Many2one("optesis.note", ondelete='cascade')


class OptesisNote5Tab2(models.Model):
    _name = "optesis.note5.tab2"

    name = fields.Char("Libelles")
    annee_n = fields.Integer("Annee N")
    annee_n1 = fields.Integer("Annee N-1")
    variation = fields.Float("Variation en %")
    note_id = fields.Many2one("optesis.note", ondelete='cascade')

class OptesisNote6(models.Model):
    _name = "optesis.note6"

    name = fields.Char("Libelles")
    annee_n = fields.Integer("Annee N")
    annee_n1 = fields.Integer("Annee N-1")
    variation = fields.Float("Variation en %")
    note_id = fields.Many2one("optesis.note", ondelete='cascade')

class OptesisNote7(models.Model):
    _name = "optesis.note7"

    name = fields.Char("Libelles")
    annee_n = fields.Integer("Annee N")
    annee_n1 = fields.Integer("Annee N-1")
    variation = fields.Float("Variation en %")
    creance1 = fields.Float("Creances a un an au plus")
    creance2 = fields.Float("Creances a plus d’un an et a deux ans au plus")
    creance3 = fields.Float("Creances a plus de deux ans")
    note_id = fields.Many2one("optesis.note", ondelete='cascade')


class OptesisNote8(models.Model):
    _name = "optesis.note8"

    name = fields.Char("Libelles")
    annee_n = fields.Integer("Annee N")
    annee_n1 = fields.Integer("Annee N-1")
    variation = fields.Float("Variation en %")
    creance1 = fields.Float("Creances a un an au plus")
    creance2 = fields.Float("Creances a plus d’un an et a deux ans au plus")
    creance3 = fields.Float("Creances a plus de deux ans")
    note_id = fields.Many2one("optesis.note", ondelete='cascade')


class OptesisNote8aTab1(models.Model):
    _name = "optesis.note8a.tab1"

    name = fields.Char("Libelles")
    frais = fields.Float("Frais d’etablissement")
    charge =fields.Float("Charge à répartir sur plusieurs exercices")
    prime = fields.Float("Prime de remboursement des oblgations")
    note_id = fields.Many2one("optesis.note", ondelete='cascade')


class OptesisNote8aTab2(models.Model):
    _name = "optesis.note8a.tab2"

    name = fields.Char("Libelles")
    compte1 = fields.Float("Comptes")
    montant1 = fields.Float("Montants")
    compte2 = fields.Float("Comptes")
    montant2 = fields.Float("Montants")
    compte3 = fields.Float("Comptes")
    montant3 = fields.Float("Montants")
    note_id = fields.Many2one("optesis.note", ondelete='cascade')


class OptesisNote9(models.Model):
    _name = "optesis.note9"

    name = fields.Char("Libelles")
    annee_n = fields.Integer("Annee N")
    annee_n1 = fields.Integer("Annee N-1")
    variation = fields.Float("Variation en %")
    note_id = fields.Many2one("optesis.note", ondelete='cascade')


class OptesisNote10(models.Model):
    _name = "optesis.note10"

    name = fields.Char("Libelles")
    annee_n = fields.Integer("Annee N")
    annee_n1 = fields.Integer("Annee N-1")
    variation = fields.Float("Variation en %")
    note_id = fields.Many2one("optesis.note", ondelete='cascade')


class OptesisNote11(models.Model):
    _name = "optesis.note11"

    name = fields.Char("Libelles")
    annee_n = fields.Integer("Annee N")
    annee_n1 = fields.Integer("Annee N-1")
    variation = fields.Float("Variation en %")
    note_id = fields.Many2one("optesis.note", ondelete='cascade')


class OptesisNote12Tab1(models.Model):
    _name = "optesis.note12.tab1"

    name = fields.Char("Libelles")
    Devises = fields.Char("Devises")
    Montant_en_D = fields.Float("Montant en devises")
    Cours_U_A_A = fields.Integer("Cours UML Année acquisition")
    Cours_U = fields.Char("Cours UML 31/12")
    Variation = fields.Integer("Variation en valeur absolue")
    note_id = fields.Many2one("optesis.note", ondelete='cascade')


class OptesisNote12Tab2(models.Model):
    _name = "optesis.note12.tab2"

    name = fields.Char("Libelles")
    annee_n = fields.Integer("Annee N")
    annee_n1 = fields.Integer("Annee N-1")
    variation = fields.Float("Variation en %")
    note_id = fields.Many2one("optesis.note", ondelete='cascade')

class OptesisNote13(models.Model):
    _name = "optesis.note13"

    name = fields.Char("Nom et Prénoms")
    Nationalite = fields.Char("Nationalité")
    Nature_des_actions = fields.Char("Nature des actions ou parts (ordinaires ou préférences)")
    Nombre = fields.Float("Nombre")
    Montant_total = fields.Float("Montant total")
    Cession = fields.Float("Cession ou remboursement en cours d’exercice")
    note_id = fields.Many2one("optesis.note", ondelete='cascade')

class OptesisNote14(models.Model):
    _name = "optesis.note14"

    name = fields.Char("Libelles")
    annee_n = fields.Float("Annee N")
    annee_n1 = fields.Float("Annee N-1")
    variation = fields.Float("Varitaion en valeur absolue")
    note_id = fields.Many2one("optesis.note", ondelete='cascade')


class OptesisNote15A(models.Model):
    _name = "optesis.note15a"

    name = fields.Char("Libelles")
    NOTE = fields.Char("NOTE")
    annee_n = fields.Float("Annee N")
    annee_n1 = fields.Float("Annee N-1")
    variation_va = fields.Float("Varitaion en valeur absolue")
    variation_p = fields.Char("Variation en %")
    regim_fiscal = fields.Char("Régime fiscal")
    echeance = fields.Char("Echéance")
    note_id = fields.Many2one("optesis.note", ondelete='cascade')


class OptesisNote15B(models.Model):
    _name = "optesis.note15b"

    name = fields.Char("Libelles")
    NOTE = fields.Char("NOTE")
    annee_n = fields.Float("Annee N")
    annee_n1 = fields.Float("Annee N-1")
    variation_va = fields.Float("Varitaion en valeur absolue")
    variation_p = fields.Char("Variation en %")
    echeance = fields.Char("Echéance")
    note_id = fields.Many2one("optesis.note", ondelete='cascade')

class OptesisNote16A(models.Model):
    _name = "optesis.note16a"

    name = fields.Char("Libelles")
    annee_n = fields.Float("Annee N")
    annee_n1 = fields.Float("Annee N-1")
    variation_va = fields.Float("Varitaion en valeur absolue")
    variation_p = fields.Char("Variation en %")
    Dettes_1aP = fields.Float("Dettes à un an au plus")
    Dettes_2aP = fields.Float("Dettes à plus d’un an et à deux ans au plus")
    Dettes_P2a = fields.Float("Dettes à plus de deux ans")

    note_id = fields.Many2one("optesis.note", ondelete='cascade')


class OptesisNote16BTab1(models.Model):
    _name = "optesis.note16b.tab1"

    name = fields.Char("Libelles")
    annee_n = fields.Float("Annee N")
    annee_n1 = fields.Float("Annee N-1")
    note_id = fields.Many2one("optesis.note", ondelete='cascade')

class OptesisNote16BTab2(models.Model):
    _name = "optesis.note16b.tab2"

    name = fields.Char("Libelles")
    annee_n = fields.Float("Annee N")
    annee_n1 = fields.Float("Annee N-1")
    note_id = fields.Many2one("optesis.note", ondelete='cascade')


class OptesisNote16BTab3(models.Model):
    _name = "optesis.note16b.tab3"

    name = fields.Char("Libelles")
    augmentationN = fields.Float("augmentation N")
    diminutionsN = fields.Float("diminutions N")
    augmentationN1 = fields.Float("augmentation N-1")
    diminutionsN1 = fields.Float("diminutions N-1")
    note_id = fields.Many2one("optesis.note", ondelete='cascade')


class OptesisNote16BBISTab1(models.Model):
    _name = "optesis.note16bbis.tab1"

    name = fields.Char("Libelles")
    annee_n = fields.Float("Annee N")
    annee_n1 = fields.Float("Annee N-1")
    note_id = fields.Many2one("optesis.note", ondelete='cascade')

class OptesisNote16BBISTab2(models.Model):
    _name = "optesis.note16bbis.tab2"

    name = fields.Char("Libelles")
    RendementN = fields.Float("Rendement attendu N")
    juste_VAN = fields.Float("juste valeur des actifs N")
    RendementN1 = fields.Float("Rendement attendu N-1")
    juste_VAN1 = fields.Float("juste valeur des actifs N-1")
    note_id = fields.Many2one("optesis.note", ondelete='cascade')

class OptesisNote16C(models.Model):
    _name = "optesis.note16c"

    name = fields.Char("Libelles")
    annee_n = fields.Float("Annee N")
    annee_n1 = fields.Float("Annee N-1")
    note_id = fields.Many2one("optesis.note", ondelete='cascade')


class OptesisNote17(models.Model):
    _name = "optesis.note17"

    name = fields.Char("Libelles")
    annee_n = fields.Float("Annee N")
    annee_n1 = fields.Float("Annee N-1")
    variation_p = fields.Char("Variation en %")
    Dettes_1aP = fields.Float("Dettes à un an au plus")
    Dettes_2aP = fields.Float("Dettes à plus d’un an et à deux ans au plus")
    Dettes_P2a = fields.Float("Dettes à plus de deux ans")
    note_id = fields.Many2one("optesis.note", ondelete='cascade')


class OptesisNote18(models.Model):
    _name = "optesis.note18"

    name = fields.Char("Libelles")
    annee_n = fields.Float("Annee N")
    annee_n1 = fields.Float("Annee N-1")
    variation_va = fields.Float("Varitaion en valeur absolue")
    variation_p = fields.Char("Variation en %")
    Dettes_1aP = fields.Float("Dettes à un an au plus")
    Dettes_2aP = fields.Float("Dettes à plus d’un an et à deux ans au plus")
    Dettes_P2a = fields.Float("Dettes à plus de deux ans")
    note_id = fields.Many2one("optesis.note", ondelete='cascade')


class OptesisNote19(models.Model):
    _name = "optesis.note19"

    name = fields.Char("Libelles")
    annee_n = fields.Float("Annee N")
    annee_n1 = fields.Float("Annee N-1")
    variation_va = fields.Float("Varitaion en valeur absolue")
    variation_p = fields.Char("Variation en %")
    Dettes_1aP = fields.Float("Dettes à un an au plus")
    Dettes_2aP = fields.Float("Dettes à plus d’un an et à deux ans au plus")
    Dettes_P2a = fields.Float("Dettes à plus de deux ans")
    note_id = fields.Many2one("optesis.note", ondelete='cascade')

class OptesisNote20(models.Model):
    _name = "optesis.note20"

    name = fields.Char("Libelles")
    annee_n = fields.Float("Annee N")
    annee_n1 = fields.Float("Annee N-1")
    variation_p = fields.Char("Variation en %")
    note_id = fields.Many2one("optesis.note", ondelete='cascade')

class OptesisNote21(models.Model):
    _name = "optesis.note21"

    name = fields.Char("Libelles")
    annee_n = fields.Float("Annee N")
    annee_n1 = fields.Float("Annee N-1")
    variation_p = fields.Char("Variation en %")
    note_id = fields.Many2one("optesis.note", ondelete='cascade')


class OptesisNote22(models.Model):
    _name = "optesis.note22"

    name = fields.Char("Libelles")
    annee_n = fields.Float("Annee N")
    annee_n1 = fields.Float("Annee N-1")
    variation_p = fields.Char("Variation en %")
    note_id = fields.Many2one("optesis.note", ondelete='cascade')


class OptesisNote23(models.Model):
    _name = "optesis.note23"

    name = fields.Char("Libelles")
    annee_n = fields.Float("Annee N")
    annee_n1 = fields.Float("Annee N-1")
    variation_p = fields.Char("Variation en %")
    note_id = fields.Many2one("optesis.note", ondelete='cascade')


class OptesisNote24(models.Model):
    _name = "optesis.note24"

    name = fields.Char("Libelles")
    annee_n = fields.Float("Annee N")
    annee_n1 = fields.Float("Annee N-1")
    variation_p = fields.Char("Variation en %")
    note_id = fields.Many2one("optesis.note", ondelete='cascade')

class OptesisNote25(models.Model):
    _name = "optesis.note25"

    name = fields.Char("Libelles")
    annee_n = fields.Float("Annee N")
    annee_n1 = fields.Float("Annee N-1")
    variation_p = fields.Char("Variation en %")
    note_id = fields.Many2one("optesis.note", ondelete='cascade')

class OptesisNote26(models.Model):
    _name = "optesis.note26"

    name = fields.Char("Libelles")
    annee_n = fields.Float("Annee N")
    annee_n1 = fields.Float("Annee N-1")
    variation_p = fields.Char("Variation en %")
    note_id = fields.Many2one("optesis.note", ondelete='cascade')

class OptesisNote27A(models.Model):
    _name = "optesis.note27a"

    name = fields.Char("Libelles")
    annee_n = fields.Float("Annee N")
    annee_n1 = fields.Float("Annee N-1")
    variation_p = fields.Char("Variation en %")
    note_id = fields.Many2one("optesis.note", ondelete='cascade')

class OptesisNote28(models.Model):
    _name = "optesis.note28"

    name = fields.Char("SITUATION ET MOUVEMENTS NATURE")
    provision_ouverture = fields.Float("Provisions à l’ouverture de l’exercice")
    exploitation_augmentation = fields.Float("Augmentation: dotations Exploitation")
    financiers_augmentation = fields.Float("Augmentation: dotations Financiers")
    hors_activite_augmentation = fields.Float("Augmentation: dotations Hors activités ordinaire")
    exploitation_diminution = fields.Float("Diminution: reprises Exploitation")
    financiers_diminution = fields.Float("Diminution: reprises Financiers")
    hors_activite_diminution = fields.Float("Diminution: reprises Hors activités ordinaire")
    provision_cloturre = fields.Float("Provisions à la clôture de l’exercice")
    note_id = fields.Many2one("optesis.note", ondelete='cascade')

class OptesisNote29(models.Model):
    _name = "optesis.note29"

    name = fields.Char("Libelles")
    annee_n = fields.Integer("Annee N")
    annee_n1 = fields.Integer("Annee N-1")
    variation = fields.Float("Variation en %")
    note_id = fields.Many2one("optesis.note", ondelete='cascade')


class OptesisNote30(models.Model):
    _name = "optesis.note30"

    name = fields.Char("Libelles")
    annee_n = fields.Float("Annee N")
    annee_n1 = fields.Float("Annee N-1")
    variation = fields.Float("Variation en %")
    note_id = fields.Many2one("optesis.note", ondelete='cascade')


class OptesisNote31(models.Model):
    _name = "optesis.note31"

    name = fields.Char("Libelles")
    annee_n = fields.Float("Annee N")
    annee_n1 = fields.Float("Annee N-1")
    annee_n2 = fields.Float("Annee N-2")
    annee_n3 = fields.Float("Annee N-3")
    annee_n4 = fields.Float("Annee N-4")
    note_id = fields.Many2one("optesis.note", ondelete='cascade')


class OptesisNote32(models.Model):
    _name = "optesis.note32"

    name = fields.Char("Désignation du produit")
    unite = fields.Char("Unite de quantite choisie")
    quantite_pays = fields.Float("PRODUCTION VENDUE DANS LE PAYS: Quantite")
    valeur_pays= fields.Float("PRODUCTION VENDUE DANS LE PAYS: Valeur")
    quantite_ohada = fields.Float("PRODUCTION VENDUE DANS LES AUTRES PAYS DE L’OHADA: Quantite")
    valeur_ohada= fields.Float("PRODUCTION VENDUE DANS LES AUTRES PAYS DE L’OHADA: Valeur")
    quantite_hors_ohada = fields.Float("PRODUCTION VENDUE HORS OHADA: Quantite")
    valeur_hors_ohada = fields.Float("PRODUCTION VENDUE HORS OHADA: Valeur")
    quantite_immo = fields.Float("PRODUCTION IMMOBILISEEE: Quantite")
    valeur_immo = fields.Float("PRODUCTION IMMOBILISEEE: Valeur")
    quantite_ouverture = fields.Float("STOCK OUVERTURE DE L’EXERCICE: Quantite")
    valeur_ouvertute = fields.Float("STOCK OUVERTURE DE L’EXERCICE: Valeur")
    quantite_cloture = fields.Float("STOCK CLÔTURE DE L’EXERCICE: Quantite")
    valeur_cloture = fields.Float("STOCK CLÔTURE DE L’EXERCICE: Valeur")
    note_id = fields.Many2one("optesis.note", ondelete='cascade')

class OptesisNote33(models.Model):
    _name = "optesis.note33"

    name = fields.Char("Désignation ")
    unite = fields.Char("Unite de quantite choisie")
    quantite_pays = fields.Float("Prdouit de l’Etat: Quantite")
    valeur_pays = fields.Float("Prdouit de l’Etat: Val")
    quantite_etat = fields.Float("Achetes dans l’Etat: Quantite")
    valeur_etat= fields.Float("Achetes dans l’Etat: Valeur")
    quantite_hors_etat = fields.Float("Achetes hors de l’Eta: Quantite")
    valeur_hors_etat = fields.Float("Achetes hors de l’Eta: Valeur")
    variation = fields.Float("Variation des stocks")
    note_id = fields.Many2one("optesis.note", ondelete='cascade')

class OptesisNote34(models.Model):
    _name = "optesis.note34"

    name = fields.Char("Libelle")
    annee_n = fields.Integer("Annee N")
    annee_n1 = fields.Integer("Annee N-1")
    variation = fields.Float("Variation en %")
    note_id = fields.Many2one("optesis.note", ondelete='cascade')


class OptesisNote37(models.Model):
    _name = "optesis.note37"

    name = fields.Char("Libelles")
    montant = fields.Float("Montant")
    note_id = fields.Many2one("optesis.note", ondelete='cascade')
