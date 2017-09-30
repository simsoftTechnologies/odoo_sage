# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from itertools import groupby
from datetime import datetime, timedelta

from openerp import api, fields, models, _
from odoo.exceptions import UserError
from odoo.tools import float_is_zero, float_compare, DEFAULT_SERVER_DATETIME_FORMAT
from odoo.tools.misc import formatLang
# import pymssql
from odoo.exceptions import ValidationError
import odoo.addons.decimal_precision as dp
from datetime import datetime
from dateutil.relativedelta import relativedelta
import datetime
import time
from odoo import api,tools ,fields, models, _
from datetime import datetime, timedelta, date, time
from time import *
import codecs
import sys
import logging
_logger = logging.getLogger(__name__)



class group_general(models.Model):
	_name = "group_general"
	
	
	name =fields.Char('Groupe générale de client')
	
class group_specifique(models.Model):
	_name = "group_specifique"
	
	name =fields.Char('Groupe spécifique de client')
	
class res_partner(models.Model):

	_inherit = "res.partner"

	
	@api.multi
	def get_ctnum(self):
		vals=[]
		valus=[]
		valeurs=[]
		dd= ''
		compt = ''
		ctnum = ''
		seq_obj= self.env['ir.sequence'].search([('name','=','ct_num_tiers')])
		if seq_obj:		
			
			ctnum = str(seq_obj.next_by_id())
			
			self.ct_num = 'CR' + ctnum
			
			vals = {
				'code' : '4112' + ctnum,
				'name' : self.name,
				'user_type_id' : '1',   
				'partner_id_t' : self.id,
				'reconcile' : True,
				}
			self.env['account.account'].create(vals)
		else:
			valeurs = {
				'name':'ct_num_tiers',
				'prefix':'00',
				   
				}  
			self.env['ir.sequence'].create(valeurs)
			seq_objh= self.env['ir.sequence'].search([('name','=','ct_num_tiers')])
			ctnum = str(seq_objh.next_by_id())
			self.ct_num = 'CR' + ctnum
			
			valsz = {
				'code' : '4112' + ctnum,
				'name' : self.name,
				'user_type_id' : '1',   
				'partner_id_t' : self.id,
				'reconcile' : True,
				}
			self.env['account.account'].create(valsz)
	
	@api.one
	@api.depends('ct_num')
	def get_compte_ctnum(self):
		self.ct_num2 = self.ct_num  
		
			
	
	@api.one
	@api.depends('ct_num2')
	def get_compte_comptable(self):
		
		for line in self.env['account.account'].search([]):
			
			self.property_account_receivable_id =  line.code
			
	ct_num = fields.Char('Compte tiers')
	property_account_receivable_id = fields.Char(compute='get_compte_comptable' , readonly = False)
	ct_num2 = fields.Char('ctnum2', compute='get_compte_ctnum' )
	group_client_general = fields.Many2one('group_general' ,string = 'Groupe générale de client ')
	group_client_specifique = fields.Many2one('group_specifique' ,string = 'Groupe spécifique de client ')
	chiffre_affaire = fields.Float('chiffre affaire n')
	chiffre_affaire1 = fields.Float('chiffre affaire n-1')
	chiffre_affaire2 = fields.Float('chiffre affaire n-2')
	condition_genrale = fields.Char('Condition Générale de vente')
	secteur_activite = fields.Char('Secteur activite')
	classement_client = fields.Char('Classement client')
	cd = fields.Char('CD')
	
   
	
	@api.model
	def create(self, vals):
		move = super(res_partner, self.with_context(check_move_validity=False)).create(vals)
		move.get_ctnum()
		
		return move
		

	
	