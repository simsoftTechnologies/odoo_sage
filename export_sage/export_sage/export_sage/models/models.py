# -*- coding: utf-8 -*-

from openerp import models, fields, api
# import pyodbc
import pymssql
import logging
_logger = logging.getLogger(__name__)
from odoo import api, fields, models, tools, _
from odoo.exceptions import ValidationError



	
	
	
	
	
	
	
	
	
	
	
	
	
	
class parametrage_sage(models.Model):
	_name = 'parametrage.sage'
	
	base = fields.Char('base1')
	DATABASE = fields.Char('base')
	name = fields.Char('DSN')
	UID = fields.Char('user')
	PWD = fields.Char('mot de passe')
	serveur = fields.Char('Serveur')
	# cnx = pyodbc.connect('DSN=MySQLServerDatabase;DATABASE=TUNITEC_LABEL2013;UID=sa;PWD=1234')
		
	def trytt (self):
		
		raise ValidationError(_('Error ! You cannot create recursive categories.'))
		return re
	def tryttt (self):
		 raise ValidationError(_('Error ! You cannot create recursivddddddddddde categories.'))
		
	@api.multi
	def test_connection_sage(self):
		server = self.serveur
		user = self.UID
		password = self.PWD
		database = self.DATABASE
	

			
		try:   
			conn = pymssql.connect(server+':1433', user, password, database)
			cursor = conn.cursor()
			
			cursor.execute("select * from F_COMPTET")
			row = cursor.fetchall()
			
			if row:
				_logger.error('connxion')
				_logger.error(row)
			
	
		except  :
			raise ValidationError(_('Erreur de connexion.'))
			
			
	
class plan_action(models.Model):

	_name = "plan.action"
	
	
	name= fields.Char('Plan action')
	qui= fields.Char('Qui')
	quand= fields.Date('Quand')
	calender_plan=fields.Many2one('calendar.event')
	
class satisfaction_client(models.Model):

	_name = "satisfaction.client"
	
	
	name= fields.Char('Qualité')
	prix= fields.Char('Prix')
	otd= fields.Char('OTD:')
	service= fields.Char('Service')
	calender_satisfaction=fields.Many2one('calendar.event')
	
class calendar_event(models.Model):

	_inherit = 'calendar.event'
	
	
	date = fields.Date('Date de la visite')
	object = fields.Char('Object visite')
	communication = fields.Char('Type de communication')
	client_prospect = fields.Char('Client/Prospect')
	activite = fields.Char('Activité')
	Departement = fields.Char('Département')
	societe = fields.Char('Société')
	code_client = fields.Char('Code client')
	adresse = fields.Char('Adresse')
	telephone = fields.Char('Télephone')
	mobile = fields.Char('Mobile')
	site_internet = fields.Char('Site internet')
	fax = fields.Char('Fax')
	nom_contact1 = fields.Char('Nom de contact')
	telephone1 = fields.Char('Télèphone')
	portable1 = fields.Char('Portable')
	email1 = fields.Char('Email')
	nom_contact2 = fields.Char('Nom de contact')
	telephone2 = fields.Char('Télèphone')
	portable2 = fields.Char('Portable')
	email2 = fields.Char('Email')
	raison_visite = fields.Char('Raison de la visite et objectif du RDV')
	objectif_client = fields.Char('Objectif du client')
	chiffre_affaire = fields.Char('Chiffre d Affaire potentiel annuel EN K euros')
	approbation_manager = fields.Char('Approbation manager')
	retour_manager = fields.Char('Retour et commentairedu manager')
	resume_visite = fields.Text('Résumé de la visite')
	plan_action = fields.One2many('plan.action','calender_plan',string='Plan d actoin')
	concurrents=fields.Char('Concurrents(si l information est disponible)')
	points_attendus = fields.Char('Points d améliorations attendus')
	quelle_innovation = fields.Char('Quelle innovation avez-vous montrées au client')
	frequence_visite = fields.Char('Fréquence de visite souhaitée')
	satisfaction = fields.One2many('satisfaction.client','calender_satisfaction',string='satisfaction')
	resultat= fields.Text('Resultat')
	verifier = fields.Text('Vérification')
	type = fields.Text('Type')
	
	