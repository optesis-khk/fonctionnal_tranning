# -*- coding:utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError, UserError
import datetime


class inventory_transfert(models.Model):
    _name = "optesis.asset.transfert"
    _description = "transfert d'inventaire"

    name = fields.Char(string="name")
    inventory_ids = fields.One2many(comodel_name="account.asset.asset", string="Inventaire", inverse_name="transfert_id")
    old_inventory_ids = fields.One2many(comodel_name="account.asset.asset", string="Inventaire",
                                    inverse_name="old_transfert_id")
    site_id = fields.Many2one(comodel_name='optesis.site', string="Site")
    building_id = fields.Many2one(comodel_name="optesis.building", string="Batiment")
    level_id = fields.Many2one(comodel_name="optesis.level", string="Niveau")
    room_id = fields.Many2one(comodel_name="optesis.room", string="Local")
    date = fields.Date(string="Date de transfert", default=datetime.date.today())
    state = fields.Selection([('draft', 'Brouillon'),('transfer', 'Transferer')], string="Etat", default='draft',  index=True, readonly=True)
    service_id = fields.Many2one('optesis.service', string="Service")
    condition_id = fields.Many2one('optesis.condition', string="Etat")
    code_barre = fields.Char(string="Transfert")

    _defaults = {
        'name': lambda obj, cr, uid, context: '/',
    }

    @api.model
    def create(self, vals):
        if vals.get('name', '/') == '/':
            vals['name'] = self.env['ir.sequence'].next_by_code('optesis.asset.transfert') or '/'
        result = super(inventory_transfert, self).create(vals)
        return result

    @api.one
    def do_transfer(self):
        if self.inventory_ids:
            for asset in self.inventory_ids:
                description = 'Transfert '
                if self.site_id.id != asset.site.id:
                    description += 'du site {} au site {}, '.format(asset.site.name, self.site_id.name)
                if self.building_id.id != asset.building.id:
                    description += 'du building {} au building {}, '.format(asset.building.name, self.building_id.name)
                if self.level_id.id != asset.level.id:
                    description += 'du niveau {} au niveau {}, '.format(asset.level.name, self.level_id.name)
                if self.room_id.id != asset.room.id:
                    description += 'du local {} au local {}, '.format(asset.room.name, self.room_id.name)
                if self.service_id.id != asset.service.id:
                    description += 'du service {} au service {}, '.format(asset.service.name, self.service_id.name)
                if self.condition_id.id != asset.condition.id:
                    description += 'du condition {} au condition {}, '.format(asset.condition.name, self.condition_id.name)
                log = self.env['optesis.account.asset.log']
                log.create({'date': datetime.datetime.now(),
                            'asset_id': asset.id,
                            'description':description})

                asset.update({'site':self.site_id.id, 'building':self.building_id.id, 'level':self.level_id.id,
                              'room':self.room_id.id,'service':self.service_id.id,'condition':self.condition_id.id})

            self.state = 'transfer'


    @api.multi
    @api.onchange('code_barre')
    def change_code_barre(self):
        if self.code_barre:
            assets = self.env['account.asset'].search([('code_bar','=',self.code_barre)])
            if assets:
                for asset in assets:
                    if self.inventory_ids:
                        find = 0
                        for line in self.inventory_ids:
                            if line.code_bar == asset.code_bar:
                                find = 1
                                break
                        if find == 1:
                            self.code_barre = None
                            raise UserError(_("Enregistrement deja ajoute."))
                        else:
                            self.inventory_ids   +=  self.env['optesis.asset.asset.transient'].create(
                                {
                                    'family_id' : asset.family_id.id,
                                    'product_id' : asset.product_id.id,
                                    'agents' : asset.agents.id,
                                    'code_bar' : asset.code_bar,
                                    'service' : asset.service.id,
                                    'condition' : asset.condition.id,
                                    'brand' : asset.brand,
                                    'specifications' : asset.specifications,
                                    'department' : asset.department.id,
                                    'direction' : asset.direction.id,
                                    'site' : asset.site.id,
                                    'building' : asset.building.id,
                                    'level' : asset.level.id,
                                    'room' : asset.room.id,
                                    'inventory_date' : asset.inventory_date,
                                    'asset_number' :  asset.asset_number,
                                    'old_transfert_id' : asset.old_transfert_id.id,
                                    'transfert_id' : self._origin.id if hasattr(self, '_origin') else None,
                                    'log_ids' : asset.log_ids,
                                    'last' : asset.last,
                                    'value' : asset.value,
                                    'date_service' : asset.date_service,
                                })
                    else:
                        self.inventory_ids   +=  self.env['optesis.asset.asset.transient'].create(
                            {
                                'family_id' : asset.family_id.id,
                                'product_id' : asset.product_id.id,
                                'agents' : asset.agents.id,
                                'code_bar' : asset.code_bar,
                                'service' : asset.service.id,
                                'condition' : asset.condition.id,
                                'brand' : asset.brand,
                                'specifications' : asset.specifications,
                                'department' : asset.department.id,
                                'direction' : asset.direction.id,
                                'site' : asset.site.id,
                                'building' : asset.building.id,
                                'level' : asset.level.id,
                                'room' : asset.room.id,
                                'inventory_date' : asset.inventory_date,
                                'asset_number' :  asset.asset_number,
                                'old_transfert_id' : asset.old_transfert_id.id,
                                'transfert_id' : self._origin.id if hasattr(self, '_origin') else None,
                                'log_ids' : asset.log_ids,
                                'last' : asset.last,
                                'value' : asset.value,
                                'date_service' : asset.date_service,
                            })
                self.code_barre = None
            else:
                return {
                    'type': 'ir.actions.act_window',
                    'res_model': 'optesis.asset.asset',
                    'view_type': 'form',
                    'view_mode': 'form',
                    'context': {
                        'default_code_bar': self.code_barre,
                        'default_service': self.service_id.id,
                        'default_site': self.site_id.id,
                        'default_building': self.building_id.id,
                        'default_level': self.level_id.id,
                        'default_room': self.room_id.id,
                        'default_condition': self.condition_id.id,
                    },
                    'target': 'new',
                }


    def start_tranfert(self):
        self.state = 'open'
