# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from itertools import groupby
from datetime import datetime, timedelta

from openerp import api, fields, models, _
from odoo.exceptions import UserError
from odoo.tools import float_is_zero, float_compare, DEFAULT_SERVER_DATETIME_FORMAT
from odoo.tools.misc import formatLang
import pymssql
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




		
		
class SaleOrder(models.Model):
	_inherit = "sale.order"  
	
	
	
	nom_projet = fields.Char('Nom de projet')
	ct_num = fields.Char('compte tiers')
	8
	@api.multi
	@api.onchange('partner_id')
	def product_id_noted(self):
		
		self.ct_num =  self.partner_id.ct_num
		
	def _get_defaut_date(self):
		now = datetime.now()
		return now
		
	@api.multi   
	def create_devis(self) :
	
		server = self.env['parametrage.sage'].search([]).serveur   
		user = self.env['parametrage.sage'].search([]).UID  
		password = self.env['parametrage.sage'].search([]).PWD 
		database = self.env['parametrage.sage'].search([]).DATABASE
		
		conn = pymssql.connect(server +':1433', user, password, database)
		cursor = conn.cursor()
		
		
		CG_Num = self.partner_id.property_account_receivable_id
		CG_Type = 0
		CG_Intitule = self.partner_id.name
		CG_Classement = self.partner_id.name
		N_Nature = 6
		CG_Report = 1
		CR_Num = 'NULL'
		CG_Analytique = 0
		CG_Echeance = 0
		CG_Quantite = 0
		CG_Lettrage = 0
		CG_Tiers = 0
		CG_DateCreate  = self._get_defaut_date()
		CG_Devise = 1
		N_Devise = 1
		TA_Code = 0
		CG_Sommeil = 1
		CG_ReportAnal = 0
		CT_Num=self.partner_id.ct_num
		CT_Type = 0
		CT_Intitule = self.partner_id.name
		CG_NumPrinc = self.partner_id.property_account_receivable_id
		CT_Qualite = 'NULL'
		CT_Classement = self.partner_id.name
		CT_Contact = self.partner_id.mobile
		Ct_Adresse = self.partner_id.street
		Ct_Complement = self.partner_id.city
		CT_CodePostal = self.partner_id.city
		CT_Ville = self.partner_id.city
		CT_CodeReqion = self.partner_id.city
		CT_Pays = self.partner_id.city
		Ct_Raccourci = "NULL"
		Bt_num = 0
		N_Devise = 0
		CT_Ape = 0
		CT_Identifiant = 0
		CT_Siret = 0
		CT_Statistique01 = 0
		CT_Statistique02= 0 
		CT_Statistique03 =0 
		CT_Statistique04 =0 
		CT_Statistique05 =0 
		CT_Statistique06 =0 
		CT_Statistique07 =0 
		CT_Statistique08 =0 
		CT_Statistique09 =0 
		CT_Statistique10 =0 
		CT_Commentaire = 'NULL'
		CT_Encours ='NULL'
		CT_Assurance = 'NULL'
		N_Risque ='NULL'
		CO_No = 0
		N_CatTarif = 0
		CT_Taux01 = 0
		CT_Taux02 = 0
		CT_Taux03 = 0
		CT_Taux04 = 0
		N_CatCompta = 0
		N_Period = 0
		Ct_Facture =0
		CT_BLFact =0 
		CT_Langue = 0
		N_Expedition =0 
		N_Condition =0
		CT_DateCreat =0
		CT_Saut =0 
		CT_Lettrage =0 
		CT_ValidEch =0
		CT_Sommeil =0
		NE_No = 0
		CT_ControlEnc =0
		CT_NotRappel =0
		N_Analytique =0
		CA_Num =0 
		
		if self.partner_id.phone == False:
			CT_Telephone = ''
		else :
			CT_Telephone = self.partner_id.phone

			
		if self.partner_id.fax == False:
			CT_Telecopie = ''
		else :
			CT_Telecopie = self.partner_id.fax

		
		if self.partner_id.email == False:
			CT_Email = ''
		else :
			CT_Email = self.partner_id.email

		
		if self.partner_id.city == False:
			CT_Site = ''
		else :
			CT_Site = self.partner_id.city

		
		if self.partner_id.phone == False:
			CT_Surveillance = ''
		else :
			CT_Surveillance = self.partner_id.phone
		CT_Num =  self.ct_num 
		
		
		cursor.execute("select CT_Num from F_COMPTET")
		
		row = cursor.fetchall()
		
		for line  in range(len(row)):
			
			if CT_Num  == row[line][0]:
				
				
		
				_logger.error('client existe')
				break
		else :   
			# cursor.execute("SELECT  TOP (1) CG_Num AS Expr1 FROM  F_COMPTEG GROUP BY CG_Type, CG_Num HAVING  (CG_Type = 0) AND (CG_Num LIKE '4%') ORDER BY Expr1 DESC")
			# rowwws = cursor.fetchall()
			 
			# for lineer  in range(len(rowwws)):
			
			# CG_Num  = int(rowwws[lineer][0]) + 1 
				
			CG_DateCreate = self.date_order
			r = CG_Intitule
			r10 = CG_Intitule
			r1 = CG_Intitule
			r4= CG_Intitule
			r5= CG_Intitule
			r2 = CG_Classement
			r3 = CG_Classement
			# r10 = sys.getdefaultencoding()
			# r = r.encode('sys.getdefaultencoding()', 'replace')
			r2 = r2.encode('ascii', 'xmlcharrefreplace')
			r1 = r1.encode('ascii', 'replace').decode('utf-8')
			r4 = r4.encode('ascii', 'backslashreplace').decode('utf-8')
			_logger.error('rvvgvgvgvg')
			# _logger.error(r10)
			# _logger.error(r)
			_logger.error(r1)
			_logger.error(r2)
			_logger.error(r3)
			_logger.error(r4)
			_logger.error(r5)
			_logger.error(CG_Num)
			_logger.error(CG_Type)
			_logger.error(CG_Classement)
			_logger.error(N_Nature)
			_logger.error(CG_Report)
			_logger.error(CG_Analytique)
			_logger.error(CG_Echeance)
			_logger.error(CG_Quantite)
			_logger.error(CG_Lettrage)
			_logger.error(CG_DateCreate)
			# rr= ("INSERT INTO F_COMPTEG (CG_Num,CG_Type,CG_Intitule,CG_Classement,N_Nature,CG_Report,CG_Analytique,CG_Echeance,CG_Quantite,CG_Lettrage,CG_Devise,CG_DateCreate,CG_Tiers,CG_Saut)  VALUES ("+str(CG_Num)+",'"+str(CG_Type)+"','"+str(CG_Intitule)+"','"+str(CG_Classement)+"' ,'"+str(N_Nature)+"','"+str(CG_Report)+"','"+str(CG_Analytique)+"','"+str(CG_Echeance)+"','"+str(CG_Quantite)+"','"+str(CG_Lettrage)+"', 1,'"+str(CG_DateCreate)+"',1,1)")
			# _logger.error(rr)
			# rr =("INSERT INTO F_COMPTEG (CG_Num,CG_Type,CG_Intitule,CG_Classement,N_Nature,CG_Report,CG_Analytique,CG_Echeance,CG_Quantite,CG_Lettrage,CG_Devise,CG_DateCreate,CG_Tiers,CG_Saut)  VALUES ("+str(CG_Num)+",'"+str(CG_Type)+"','"+str(r4)+"','"+str(r4)+"' ,'"+str(N_Nature)+"','"+str(CG_Report)+"','"+str(CG_Analytique)+"','"+str(CG_Echeance)+"','"+str(CG_Quantite)+"','"+str(CG_Lettrage)+"', 1,'"+str(CG_DateCreate)+"',1,1)")
			
			# rr = rr.encode('ascii', 'xmlcharrefreplace').decode('ascii')
			# _logger.error('encode')
			# _logger.error(rr)
			rr= ("INSERT INTO F_COMPTEG (CG_Num,CG_Type,CG_Intitule,CG_Classement,N_Nature,CG_Report,CG_Analytique,CG_Echeance,CG_Quantite,CG_Lettrage,CG_Devise,CG_DateCreate,CG_Tiers,CG_Saut)  VALUES ("+str(CG_Num)+",'"+str(CG_Type)+"','"+str(CG_Intitule)+"','"+str(CG_Classement)+"' ,'"+str(N_Nature)+"','"+str(CG_Report)+"','"+str(CG_Analytique)+"','"+str(CG_Echeance)+"','"+str(CG_Quantite)+"','"+str(CG_Lettrage)+"', 1,'"+str(CG_DateCreate)+"',1,1)")
			_logger.error(rr)
			cursor.execute("INSERT INTO F_COMPTEG (CG_Num,CG_Type,CG_Intitule,CG_Classement,N_Nature,CG_Report,CG_Analytique,CG_Echeance,CG_Quantite,CG_Lettrage,CG_Devise,CG_DateCreate,CG_Tiers,CG_Saut)  VALUES ("+str(CG_Num)+",'"+str(CG_Type)+"','"+str(CG_Intitule)+"','"+str(CG_Classement)+"' ,'"+str(N_Nature)+"','"+str(CG_Report)+"','"+str(CG_Analytique)+"','"+str(CG_Echeance)+"','"+str(CG_Quantite)+"','"+str(CG_Lettrage)+"', 1,'"+str(CG_DateCreate)+"',1,1)")
			conn.commit()



			CT_Qualite = ''
			if self.partner_id.name == False:
				CT_Classement = ''
			else :
			
				CT_Classement=  self.partner_id.name
			if self.partner_id.phone == False:
				CT_Contact = ''
			else :
			
				CT_Contact = self.partner_id.phone
			if self.partner_id.street  == False:
				CT_Adresse = ''
			else :
			
				CT_Adresse = self.partner_id.street
			if self.partner_id.street2 == False:
				CT_Complement = ''
			else :
			
				CT_Complement = self.partner_id.street2
			if self.partner_id.zip == False:
				CT_CodePostal = ''
			else :
				CT_CodePostal = self.partner_id.zip
			if self.partner_id.city == False:
				CT_Ville = ''   
			else :
				CT_Ville = self.partner_id.city
			if self.partner_id.state_id.name == False:
				CT_CodeRegion = ''
			else :
			
				CT_CodeRegion = self.partner_id.state_id.name
			if self.partner_id.country_id.name == False:
				CT_Pays = ''
			else :
				CT_Pays = self.partner_id.country_id.name
			
			CT_Raccourci = ''

			BT_Num = 0
			N_Devise = 0
			CT_Ape = ''
			CT_Siret = ''
			CT_Statistique01 = self.partner_id.secteur_activite
			CT_Statistique02 = self.partner_id.classement_client
			CT_Statistique03 = ''
			CT_Statistique04 = ''
			CT_Statistique05 = ''
			CT_Statistique06 = ''
			CT_Statistique07 = ''
			CT_Statistique08 =''
			CT_Statistique09 = ''
			CT_Statistique10 = ''

			CT_Commentaire = ''
			CT_Encours = 0
			CT_Assurance = 0
			CT_NumPayeur =  self.ct_num 

			N_Risque = 1
			CO_No = 0
			cbCO_No = 'NULL'

			N_CatTarif = 1
			CT_Taux01 = 0
			CT_Taux02 = 0
			CT_Taux03 = 0
			CT_Taux04 = 0
			N_CatCompta = 1
			N_Period = 1


			CT_DateCreate = self.date_order
			
			chaine = "INSERT INTO F_COMPTET (CT_Num,CT_Intitule,CT_Type,CG_NumPrinc,CT_Qualite,CT_Classement,CT_Contact,CT_Adresse,CT_Complement,CT_CodePostal,CT_Ville,CT_CodeRegion,CT_Pays,CT_Raccourci,BT_Num,N_Devise,CT_Ape,CT_Identifiant,CT_Siret,CT_Statistique01,CT_Statistique02,CT_Statistique03,CT_Statistique04,CT_Statistique05,CT_Statistique06,CT_Statistique07,CT_Statistique08,CT_Statistique09,CT_Statistique10,CT_Commentaire,CT_Encours,CT_Assurance,CT_NumPayeur,N_Risque,CO_No,cbCO_No,N_CatTarif,CT_Taux01,CT_Taux02,CT_Taux03,CT_Taux04,N_CatCompta,N_Period,CT_Facture,CT_BLFact,CT_Langue,N_Expedition,N_Condition,CT_DateCreate,CT_Saut,CT_Lettrage,CT_ValidEch,CT_Sommeil,DE_No,cbDE_No,CT_ControlEnc,CT_NotRappel,N_Analytique,cbN_Analytique,CA_Num,CT_Telephone,CT_Telecopie,CT_EMail,CT_Site,CT_Coface,CT_Surveillance,CT_SvDateCreate,CT_SvFormeJuri,CT_SvEffectif,CT_SvCA,CT_SvResultat,CT_SvIncident,CT_SvDateIncid,CT_SvPrivil,CT_SvRegul,CT_SvCotation,CT_SvDateMaj,CT_SvObjetMaj,CT_SvDateBilan,CT_SvNbMoisBilan,N_AnalytiqueIFRS,cbN_AnalytiqueIFRS,CA_NumIFRS,CT_PrioriteLivr,CT_LivrPartielle,MR_No,cbMR_No,CT_NotPenal,EB_No,cbEB_No,CT_NumCentrale,CT_DateFermeDebut,CT_DateFermeFin,CT_FactureElec,CT_TypeNIF,CT_RepresentInt,CT_RepresentNIF,CT_EdiCodeType,CT_EdiCode,CT_EdiCodeSage,CT_ProfilSoc,CT_StatutContrat,CT_DateMAJ,CT_EchangeRappro,CT_EchangeCR,PI_NoEchange,cbPI_NoEchange,CT_BonAPayer,CT_DelaiTransport,CT_DelaiAppro,CT_LangueISO2,cbCreateur) VALUES ('"+str(CT_Num)+"','"+str(CT_Intitule)+"','"+str(CG_Type)+"','"+str(CG_Num)+"','"+str(CT_Qualite)+"','"+str(CT_Classement)+"','"+str(CT_Contact)+"','"+str(CT_Adresse)+"','"+str(CT_Complement)+"','"+str(CT_CodePostal)+"','"+str(CT_Ville)+"','"+str(CT_CodeRegion)+"','"+str(CT_Pays)+"' ,'"+str(CT_Raccourci)+"',"+str(BT_Num)+","+str(N_Devise)+",'"+str(CT_Ape)+"','"+str(CT_Identifiant)+"','"+str(CT_Siret)+"','"+str(CT_Statistique01)+"','"+str(CT_Statistique02)+"','"+str(CT_Statistique03)+"','"+str(CT_Statistique04)+"','"+str(CT_Statistique05)+"','"+str(CT_Statistique06)+"','"+str(CT_Statistique07)+"','"+str(CT_Statistique08)+"','"+str(CT_Statistique09)+"','"+str(CT_Statistique10)+"','"+str(CT_Commentaire)+"','"+str(CT_Encours)+"','"+str(CT_Assurance)+"','"+str(CT_NumPayeur)+"',"+str(N_Risque)+","+str(CO_No)+","+str(cbCO_No)+","+str(N_CatTarif)+","+str(CT_Taux01)+","+str(CT_Taux02)+","+str(CT_Taux03)+","+str(CT_Taux04)+","+str(N_CatCompta)+","+str(N_Period)+",1,0,0,1,1,'"+str(CT_DateCreate)+"',1,1,0,0,0,NULL,0,0,0,NULL,NULL,'"+str(CT_Telephone)+"','"+str(CT_Telecopie)+"','"+str(CT_Email)+"','','',0,'1900-01-01 00:00:00','','',0,0,0,'1900-01-01 00:00:00',0,'','','1900-01-01 00:00:00','','1900-01-01 00:00:00',0,0,NULL,NULL,0,0,0,NULL,0,0,NULL,NULL,'1900-01-01 00:00:00','1900-01-01 00:00:00',0,0,'','',0,'','',0,0,'1900-01-01 00:00:00',0,1,0,NULL,0,0,0,'','COLU')"
			chaine = chaine.encode('ascii', 'xmlcharrefreplace').decode('ascii')
			_logger.error('encode')
			_logger.error(chaine)
			cursor.execute(chaine)
			
			

			
			
			conn.commit()    
				
		for sale in self.order_line : 

			FA_CodeFamille = sale.product_id.categ_id.code_famille
			FA_Type  = 0
			FA_Intitule = sale.product_id.categ_id.name
			FA_UniteVen = 1 
			FA_Coef = 0
			FA_SuiviStock = 0
			FA_Garantie = 0
			FA_Central =''
			FA_Stat01 =''
			FA_Stat02= ''
			FA_Stat03 =''
			FA_Stat04= ''
			FA_Stat05=''
			FA_CodeFiscal=''
			FA_Pays = ''
			FA_UnitePoids = 2
			FA_Escompte = 0
			FA_Delai = 0
			FA_HorsStat = 0
			FA_VteDebit = 0 
			FA_NotImp = 0
			FA_Frais01FR_Denomination = 'stockage'
			FA_Frais01FR_Rem01REM_Valeur = 0
			FA_Frais01FR_Rem01REM_Type = 0
			FA_Frais01FR_Rem02REM_Valeur = 0
			FA_Frais01FR_Rem02REM_Type = 0
			FA_Frais01FR_Rem03REM_Valeur = 0
			FA_Frais01FR_Rem03REM_Type = 0
			FA_Frais02FR_Denomination = 'transport'
			FA_Frais02FR_Rem01REM_Valeur = 0
			FA_Frais02FR_Rem01REM_Type = 0
			FA_Frais02FR_Rem02REM_Valeur = 0
			FA_Frais02FR_Rem02REM_Type = 0
			FA_Frais02FR_Rem03REM_Valeur = 0
			FA_Frais02FR_Rem03REM_Type = 0
			FA_Frais03FR_Denomination = 'annexe'
			FA_Frais03FR_Rem01REM_Valeur = 0
			FA_Frais03FR_Rem01REM_Type =0
			FA_Frais03FR_Rem02REM_Valeur= 0
			FA_Frais03FR_Rem02REM_Type =0
			FA_Frais03FR_Rem03REM_Valeur =0
			FA_Frais03FR_Rem03REM_Type =0
			FA_Contremarque =0
			FA_FactPoids =0
			FA_FactForfait= 0
			FA_Publie = 1
			FA_RacineRef = ''
			FA_RacineCB= ''
			CL_No1 = 0
			cbCL_No1 = 'NULL'
			CL_No2 = 0
			cbCL_No2 = 'NULl'
			CL_No3 = 0
			cbCL_No3 = 'NULL'
			CL_No4 = 0
			cbCL_No4 = 'NULL'
			FA_Nature = 2
			FA_NbColis = 0
			FA_SousTraitance = 0
			FA_Fictif =0
			FA_Criticite = 0
			cbCreateur = 'COLU'
			
			# **************************************article****************************
			AR_Ref = sale.product_id.product_tmpl_id.default_code
			AR_Ref = sale.product_id.product_tmpl_id.default_code
			AR_Design = sale.product_id.name
			FA_CodeFamille = sale.product_id.categ_id.code_famille
			AR_Substitut = sale.product_id.product_tmpl_id.default_code
			AR_Raccourci ='NULL'
			AR_Garantie = 0
			AR_UnitePoids = 2
			AR_PoidsNet = 0
			AR_PoidsBrut = 0
			AR_UniteVen = sale.product_id.lst_price
			# AR_PrixAch = sale.prix1
			AR_PrixAch = 1
			AR_Coef =0
			AR_PrixVen = sale.prix1
			AR_PrixTTC = 0
			AR_Gamme1 = 0
			AR_Gamme2 = 0
			AR_SuiviStock = 2
			AR_Nomencl = 0
			AR_Stat01 = ''
			AR_Stat02 = ''
			AR_Stat03 = ''
			AR_Stat04 = ''
			AR_Stat05 = ''

			AR_EdiCode = 'NULL'
			AR_Escompte =0 
			AR_Delai =0 
			AR_HorsStat =0  
			AR_VteDebit=0
			AR_NotImp =0
			AR_Sommeil = 0
			AR_Langue1 = '' 
			AR_Langue2 = ''
			AR_CodeBarre = 'NULL'
			AR_CodeFiscal = ''
			AR_Pays = ''
			AR_Frais01FR_Denomination = 'cout de stockage'
			AR_Frais01FR_Rem01REM_Valeur =0
			AR_Frais01FR_Rem01REM_Type = 0
			AR_Frais01FR_Rem02REM_Valeur = 0
			AR_Frais01FR_Rem02REM_Type = 0
			AR_Frais01FR_Rem03REM_Valeur = 0
			AR_Frais01FR_Rem03REM_Type = 0
			AR_Frais02FR_Denomination = 'cout de transport'
			AR_Frais02FR_Rem01REM_Valeur = 0
			AR_Frais02FR_Rem01REM_Type = 0
			AR_Frais02FR_Rem02REM_Valeur = 0
			AR_Frais02FR_Rem02REM_Type = 0
			AR_Frais02FR_Rem03REM_Valeur = 0
			AR_Frais02FR_Rem03REM_Type = 0
			AR_Frais03FR_Denomination = 'annexe'

			AR_Frais03FR_Rem01REM_Valeur = 0
			AR_Frais03FR_Rem01REM_Type  = 0
			AR_Frais03FR_Rem02REM_Valeur = 0
			AR_Frais03FR_Rem02REM_Type = 0
			AR_Frais03FR_Rem03REM_Valeur = 0
			AR_Frais03FR_Rem03REM_Type = 0
			AR_Condition = 0
			AR_PUNet = 0
			AR_Contremarque = 0
			AR_FactPoids = 0
			AR_FactForfait = 0 
			# AR_DateCreation = datetime.strptime((self.date_order),'%Y-%m-%d %H:%M:%S').strftime('%d-%m-%Y %H:%M:%S')
			AR_DateCreation = self.date_order
			AR_SaisieVar = 0
			AR_Transfere = 0
			AR_Publie = 1
			# AR_DateModif = datetime.strptime((self.date_order),'%Y-%m-%d %H:%M:%S').strftime('%d-%m-%Y %H:%M:%S')
			AR_DateModif = self.date_order
			AR_Photo = ''
			AR_PrixAchNouv = 0
			AR_CoefNouv = 0
			AR_PrixVenNouv = 0
			# AR_DateApplication = datetime.strptime((self.date_order),'%Y-%m-%d %H:%M:%S').strftime('%d-%m-%Y %H:%M:%S')
			AR_DateApplication = self.date_order
			AR_CoutStd = 0
			AR_QteComp = 1
			AR_QteOperatoire = 1
			CO_No = 0
			AR_Prevision = 0
			CL_No1 = 0
			CL_No2 = 0
			CL_No3 = 0
			CL_No4 = 0
			if len(sale.product_id.product_variant_ids) <= 1:
				AR_Type = 0
			else :
				AR_Type = 1
			RP_CodeDefaut = 'NULL'
			Duree_de_vie = 1
			quantite = '5'
			Process_1 = '5'
			Calage_P1 = '5'
			TirageP1 = '5'
			Process_2 = '5'
			Calage_P2 = '5'
			Tirage_P2 = '5'
			Process_3 = '5'
			Calage__Tirage_P3 = '5'
			AR_EdiCode = '5'
			AR_Nature = 2
			AR_DelaiFabrication = 0
			AR_NbColis = 0
			AR_DelaiPeremption = 0 
			AR_DelaiSecurite = 0
			AR_Fictif = 0
			AR_SousTraitance = 0
			AR_TypeLancement = 0
			AR_CODEEDIED_CODE1 = 5
			AR_CODEEDIED_CODE2 = 5
			AR_CODEEDIED_CODE3 = 5
			AR_CODEEDIED_CODE4 = 5
			AR_Cycle = 1
			AR_Criticite = 0
			# AR_DateModif = datetime.strptime((self.date_order),'%Y-%m-%d %H:%M:%S').strftime('%d-%m-%Y %H:%M:%S')
			AR_DateModif = self.date_order
			# AR_DateApplication = datetime.strptime((self.date_order),'%Y-%m-%d %H:%M:%S').strftime('%d-%m-%Y %H:%M:%S')
			AR_DateApplication = self.date_order
			AR_SousTraitance = ''
			cbCO_No ='NULL'
			cbCL_No1 = 'NULL'
			cbCL_No2 ='NULL'
			cbCL_No3 ='NULL'
			cbCL_No4 = 'NULL'
			cbCreateur =  'COLU'
		
			cursor.execute("select AR_Ref from F_Article")
			
			row_article = cursor.fetchall()
			
			
			for line_article  in range(len(row_article)):
				
				
				
				
				
				if AR_Ref  ==  row_article[line_article][0]:
					
		
					_logger.error('article existe')
					if len(sale.product_id.product_variant_ids) > 1:
						_logger.error('gamme_vasi')
						for line_gamme in sale.product_id.product_variant_ids:
							for lii in line_gamme :
										
										
										

								AE_Reff = lii.default_code
								AE_PrixAch = lii.lst_price
								AE_CodeBarre = lii.barcode
								AR_CoutStd = lii.standard_price
								
								for lio in lii.attribute_value_ids :
									EG_Enumeree = lio.name  
								EG_Enumere = EG_Enumeree
								_logger.error("EG_EnumereEG_EnumereEG_Enumere")
								_logger.error(EG_Enumere)
								AG_No2 = 0
								cursor.execute("select EG_Enumere from F_ARTGAMME")
			
								row_artgam = cursor.fetchall()
								for line_artgam  in range(len(row_artgam)):
									if EG_Enumere  ==  row_artgam[line_artgam][0]: 
										_logger.error('gamme et article existe')
										break
								else:
									_logger.error(':p')
									AR_PUNet = sale.product_id.lst_price
									_logger.error('popopopopoppo')
									cursor.execute("select MAX(AG_No) from F_ARTGAMME")   
									rows_AG_No = cursor.fetchall()
									for lines_AG_Noo in range(len(rows_AG_No)):
										AG_Noo =  rows_AG_No[lines_AG_Noo][0]
										AG_No = AG_Noo +1
										
										AG_Type = 0
										
										cbCreateur= 'COLU'  
										AG_No2 = 0
										  
										ARy_Gamme1 = sale.product_id.attribute_line_ids.attribute_id.numero
										
										AR_Ref_art = sale.product_id.product_tmpl_id.default_code25
										
										ARi_Design = sale.product_id.product_tmpl_id.name
										ARr_Substitut = sale.product_id.product_tmpl_id.default_code25
										op= ("INSERT INTO  F_ARTGAMME(AR_Ref,AG_No,EG_Enumere,AG_Type,cbCreateur) values ('"+str(AR_Ref_art)+"',"+str(AG_No)+",'"+str(EG_Enumere)+"',0,'"+str(cbCreateur)+"')")
										_logger.error(op)
										cursor.execute ("INSERT INTO  F_ARTGAMME(AR_Ref,AG_No,EG_Enumere,AG_Type,cbCreateur) values ('"+str(AR_Ref_art)+"',"+str(AG_No)+",'"+str(EG_Enumere)+"',0,'"+str(cbCreateur)+"')")
										conn.commit()  
										
										cursor.execute ("INSERT INTO  F_ARTENUMREF(AR_Ref,AG_No1,AG_No2,AE_Ref,AE_PrixAch,AE_CodeBarre,AE_PrixAchNouv,AE_EdiCode,AE_Sommeil,cbCreateur) values ('"+str(AR_Ref_art)+"',"+str(AG_No)+","+str(AG_No2)+",'"+str(AE_CodeBarre)+"',"+str(AE_PrixAch)+",'"+str(AE_CodeBarre)+"',0,'1',0,'"+str(cbCreateur)+"')")
										conn.commit()  
										
										cursor.execute ("INSERT INTO  F_ARTPRIX(AR_Ref,AG_No1,AG_No2,AR_PUNet,AR_CoutStd,cbCreateur) values ('"+str(AR_Ref_art)+"',"+str(AG_No)+","+str(AG_No2)+","+str(AR_PUNet)+","+str(AR_CoutStd)+",'"+str(cbCreateur)+"')")
										conn.commit() 
								
					
				
									
					break
			else :  
				cursor.execute("select FA_CodeFamille from F_FAMILLE")
				rows_famille = cursor.fetchall()
				
				for lines_famille in range(len(rows_famille)):
					if FA_CodeFamille ==  rows_famille[lines_famille][0]:
						
						
						cursor.execute ("INSERT INTO  F_Article(AR_Ref,AR_Design,FA_CodeFamille,AR_Raccourci,AR_Garantie,AR_UnitePoids,AR_PoidsNet,AR_PoidsBrut,AR_UniteVen,AR_PrixAch,AR_Coef,AR_PrixVen,AR_PrixTTC,AR_Gamme1,AR_Gamme2,AR_SuiviStock,AR_Nomencl,AR_Stat01,AR_Stat02,AR_Stat03,AR_Stat04,AR_Stat05,AR_Escompte,AR_Delai,AR_HorsStat,AR_VteDebit,AR_NotImp,AR_Sommeil,AR_Langue1,AR_Langue2,AR_EdiCode,AR_CodeBarre,AR_CodeFiscal,AR_Pays,AR_Frais01FR_Denomination,AR_Frais01FR_Rem01REM_Valeur,AR_Frais01FR_Rem01REM_Type,AR_Frais01FR_Rem02REM_Valeur,AR_Frais01FR_Rem02REM_Type,AR_Frais01FR_Rem03REM_Valeur,AR_Frais01FR_Rem03REM_Type,AR_Frais02FR_Denomination,AR_Frais02FR_Rem01REM_Valeur,AR_Frais02FR_Rem01REM_Type,AR_Frais02FR_Rem02REM_Valeur,AR_Frais02FR_Rem02REM_Type,AR_Frais02FR_Rem03REM_Valeur,AR_Frais02FR_Rem03REM_Type,AR_Frais03FR_Rem01REM_Valeur,AR_Frais03FR_Rem01REM_Type,AR_Frais03FR_Rem02REM_Valeur,AR_Frais03FR_Rem02REM_Type,AR_Frais03FR_Rem03REM_Valeur,AR_Frais03FR_Rem03REM_Type,AR_Condition,AR_PUNet,AR_Contremarque,AR_FactPoids,AR_FactForfait,AR_DateCreation,AR_SaisieVar,AR_Transfere,AR_Publie,AR_DateModif,AR_Photo,AR_PrixAchNouv,AR_CoefNouv,AR_PrixVenNouv,AR_DateApplication,AR_CoutStd,AR_QteComp,AR_QteOperatoire,CO_No,cbCO_No,AR_Prevision,CL_No1,cbCL_No1,CL_No2,cbCL_No2,CL_No3,cbCL_No3,CL_No4,cbCL_No4,AR_Type,RP_CodeDefaut,AR_Nature,AR_DelaiFabrication,AR_NbColis,AR_DelaiPeremption,AR_DelaiSecurite,AR_Fictif,AR_SousTraitance,AR_TypeLancement,cbCreateur) values ('"+str(AR_Ref)+"','"+str(AR_Design)+"','"+str(FA_CodeFamille)+"',"+str(AR_Raccourci)+","+str(AR_Garantie)+","+str(AR_UnitePoids)+","+str(AR_PoidsNet)+","+str(AR_PoidsBrut)+","+str(AR_UniteVen)+","+str(AR_PrixAch)+","+str(AR_Coef)+","+str(AR_PrixVen)+","+str(AR_PrixTTC)+","+str(AR_Gamme1)+","+str(AR_Gamme2)+","+str(AR_SuiviStock)+","+str(AR_Nomencl)+",'"+str(AR_Stat01)+"','"+str(AR_Stat02)+"','"+str(AR_Stat03)+"','"+str(AR_Stat04)+"','"+str(AR_Stat05)+"',"+str(AR_Escompte)+","+str(AR_Delai)+","+str(AR_HorsStat)+","+str(AR_VteDebit)+","+str(AR_NotImp)+","+str(AR_Sommeil)+",'"+str(AR_Langue1)+"','"+str(AR_Langue2)+"',"+str(AR_EdiCode)+","+str(AR_CodeBarre)+",'"+str(AR_CodeFiscal)+"','"+str(AR_Pays)+"','"+str(AR_Frais01FR_Denomination)+"',"+str(AR_Frais01FR_Rem01REM_Valeur)+","+str(AR_Frais01FR_Rem01REM_Type)+","+str(AR_Frais01FR_Rem02REM_Valeur)+","+str(AR_Frais01FR_Rem02REM_Type)+","+str(AR_Frais01FR_Rem03REM_Valeur)+","+str(AR_Frais01FR_Rem03REM_Type)+",'"+str(AR_Frais02FR_Denomination)+"',"+str(AR_Frais02FR_Rem01REM_Valeur)+","+str(AR_Frais02FR_Rem01REM_Type)+","+str(AR_Frais02FR_Rem02REM_Valeur)+","+str(AR_Frais02FR_Rem02REM_Type)+","+str(AR_Frais02FR_Rem03REM_Valeur)+","+str(AR_Frais02FR_Rem03REM_Type)+","+str(AR_Frais03FR_Rem01REM_Valeur)+","+str(AR_Frais03FR_Rem01REM_Type)+","+str(AR_Frais03FR_Rem02REM_Valeur)+","+str(AR_Frais03FR_Rem02REM_Type)+","+str(AR_Frais03FR_Rem03REM_Valeur)+","+str(AR_Frais03FR_Rem03REM_Type)+","+str(AR_Condition)+","+str(AR_PUNet)+","+str(AR_Contremarque)+","+str(AR_FactPoids)+","+str(AR_FactForfait)+",'"+str(AR_DateCreation)+"',"+str(AR_SaisieVar)+","+str(AR_Transfere)+","+str(AR_Publie)+",'"+str(AR_DateModif)+"','"+str(AR_Photo)+"',"+str(AR_PrixAchNouv)+","+str(AR_CoefNouv)+","+str(AR_PrixVenNouv)+",'"+str(AR_DateApplication)+"',"+str(AR_CoutStd)+","+str(AR_QteComp)+","+str(AR_QteOperatoire)+","+str(CO_No)+","+str(cbCO_No)+","+str(AR_Prevision)+","+str(CL_No1)+","+str(cbCL_No1)+","+str(CL_No2)+","+str(cbCL_No2)+","+str(CL_No3)+","+str(cbCL_No3)+","+str(CL_No4)+","+str(cbCL_No4)+","+str(AR_Type)+","+str(RP_CodeDefaut)+","+str(AR_Nature)+","+str(AR_DelaiFabrication)+","+str(AR_NbColis)+","+str(AR_DelaiPeremption)+","+str(AR_DelaiSecurite)+","+str(AR_Fictif)+",'"+str(AR_SousTraitance)+"',"+str(AR_TypeLancement)+",'"+str(cbCreateur)+"')")
						conn.commit() 
					
						_logger.error('2')
				
						
						if len(sale.product_id.product_variant_ids) > 1:
							_logger.error('omapaua')
							for line_gamme in sale.product_id.product_variant_ids:
								AR_PUNet = sale.product_id.lst_price
								
								cursor.execute("select MAX(AG_No) from F_ARTGAMME")   
								rows_AG_No = cursor.fetchall()
								for lines_AG_Noo in range(len(rows_AG_No)):
									AG_Noo =  rows_AG_No[lines_AG_Noo][0]
								AG_No = AG_Noo +1

								AG_Type = 0
								
								cbCreateur= 'COLU'  
								AG_No2 = 0
								
								ARy_Gamme1 = sale.product_id.attribute_line_ids.attribute_id.numero
								
								AR_Ref_art = sale.product_id.product_tmpl_id.default_code25
								
								ARi_Design = sale.product_id.product_tmpl_id.name
								ARr_Substitut = sale.product_id.product_tmpl_id.default_code
								
								
								
								for lii in line_gamme :
								
									AE_Reff = lii.default_code
									
									
									
									AE_PrixAch = lii.lst_price
									AE_CodeBarre = lii.barcode
									AR_CoutStd = lii.standard_price
									
									for lio in lii.attribute_value_ids :
										EG_Enumeree = lio.name
									EG_Enumere = EG_Enumeree
									AG_No2 = 0
									
									
									cursor.execute ("INSERT INTO  F_ARTGAMME(AR_Ref,AG_No,EG_Enumere,AG_Type,cbCreateur) values ('"+str(AR_Ref_art)+"',"+str(AG_No)+",'"+str(EG_Enumere)+"',0,'"+str(cbCreateur)+"')")
									conn.commit()  
									
									cursor.execute ("INSERT INTO  F_ARTENUMREF(AR_Ref,AG_No1,AG_No2,AE_Ref,AE_PrixAch,AE_CodeBarre,AE_PrixAchNouv,AE_EdiCode,AE_Sommeil,cbCreateur) values ('"+str(AR_Ref_art)+"',"+str(AG_No)+","+str(AG_No2)+",'"+str(AE_Reff)+"',"+str(AE_PrixAch)+",'"+str(AE_CodeBarre)+"',0,'1',0,'"+str(cbCreateur)+"')")
									conn.commit()  
									
									cursor.execute ("INSERT INTO  F_ARTPRIX(AR_Ref,AG_No1,AG_No2,AR_PUNet,AR_CoutStd,cbCreateur) values ('"+str(AR_Ref_art)+"',"+str(AG_No)+","+str(AG_No2)+","+str(AR_PUNet)+","+str(AR_CoutStd)+",'"+str(cbCreateur)+"')")
									conn.commit() 
							# for lineee in sale :
								# AC_RefClient = sale.reference
								# cursor.execute("select AR_Ref  from F_ARTCLIENT")   
								# rows_Artcli = cursor.fetchall()
								# for lines_Artc in range(len(rows_Artcli)):
									# if AR_Ref  == rows_Artcli[lines_Artc][0]:
										
							
										# _logger.error('F_ARTCLIENT existe')
										# break
								# else :
									
									# cursor.execute ("INSERT INTO F_ARTCLIENT (AR_Ref,AC_Categorie,AC_PrixVen,AC_Coef,AC_PrixTTC,AC_Arrondi,AC_QteMont,EG_Champ,AC_PrixDev,AC_Devise,CT_Num,AC_Remise,AC_Calcul,AC_TypeRem,AC_RefClient,AC_CoefNouv,AC_PrixVenNouv,AC_PrixDevNouv,AC_RemiseNouv,AC_DateApplication,cbCreateur) VALUES ('"+str(AR_Ref)+"',0,0,0,0,0,1,1,0,0,'"+str(CT_Num)+"',0,0,0,'"+str(AC_RefClient)+"',0,0,0,0,'1900-01-01 00:00:00','COLU')")
									# conn.commit()
						
						break 
						
				else : 
					tt = ("INSERT INTO F_FAMILLE (FA_CodeFamille,FA_Type,FA_Intitule,FA_UniteVen,FA_Coef,FA_SuiviStock,FA_Garantie,FA_Central,FA_Stat01,FA_Stat02,FA_Stat03,FA_Stat04,FA_Stat05,FA_CodeFiscal,FA_Pays,FA_UnitePoids,FA_Escompte,FA_Delai,FA_HorsStat,FA_VteDebit,FA_NotImp,FA_Frais01FR_Denomination,FA_Frais01FR_Rem01REM_Valeur,FA_Frais01FR_Rem01REM_Type,FA_Frais01FR_Rem02REM_Valeur,FA_Frais01FR_Rem02REM_Type,FA_Frais01FR_Rem03REM_Valeur,FA_Frais01FR_Rem03REM_Type,FA_Frais02FR_Denomination,FA_Frais02FR_Rem01REM_Valeur,FA_Frais02FR_Rem01REM_Type,FA_Frais02FR_Rem02REM_Valeur,FA_Frais02FR_Rem02REM_Type,FA_Frais02FR_Rem03REM_Valeur,FA_Frais02FR_Rem03REM_Type,FA_Frais03FR_Denomination,FA_Frais03FR_Rem01REM_Valeur,FA_Frais03FR_Rem01REM_Type,FA_Frais03FR_Rem02REM_Valeur,FA_Frais03FR_Rem02REM_Type,FA_Frais03FR_Rem03REM_Valeur,FA_Frais03FR_Rem03REM_Type,FA_Contremarque,FA_FactPoids,FA_FactForfait,FA_Publie,FA_RacineRef,FA_RacineCB,CL_No1,cbCL_No1,CL_No2,cbCL_No2,CL_No3,cbCL_No3,CL_No4,cbCL_No4,FA_Nature,FA_NbColis,FA_SousTraitance,FA_Fictif,cbCreateur) VALUES('"+str(FA_CodeFamille)+"',"+str(FA_Type)+",'"+str(FA_Intitule)+"',"+str(FA_UniteVen)+","+str(FA_Coef)+","+str(FA_SuiviStock)+","+str(FA_Garantie)+",'"+str(FA_Central)+"','"+str(FA_Stat01)+"','"+str(FA_Stat02)+"','"+str(FA_Stat03)+"','"+str(FA_Stat04)+"','"+str(FA_Stat05)+"','"+str(FA_CodeFiscal)+"','"+str(FA_Pays)+"',"+str(FA_UnitePoids)+","+str(FA_Escompte)+","+str(FA_Delai)+","+str(FA_HorsStat)+","+str(FA_VteDebit)+","+str(FA_NotImp)+",'"+str(FA_Frais01FR_Denomination)+"',"+str(FA_Frais01FR_Rem01REM_Valeur)+","+str(FA_Frais01FR_Rem01REM_Type)+","+str(FA_Frais01FR_Rem02REM_Valeur)+","+str(FA_Frais01FR_Rem02REM_Type)+","+str(FA_Frais01FR_Rem03REM_Valeur)+","+str(FA_Frais01FR_Rem03REM_Type)+",'"+str(FA_Frais02FR_Denomination)+"',"+str(FA_Frais02FR_Rem01REM_Valeur)+","+str(FA_Frais02FR_Rem01REM_Type)+","+str(FA_Frais02FR_Rem02REM_Valeur)+","+str(FA_Frais02FR_Rem02REM_Type)+","+str(FA_Frais02FR_Rem03REM_Valeur)+","+str(FA_Frais02FR_Rem03REM_Type)+",'"+str(FA_Frais03FR_Denomination)+"',"+str(FA_Frais03FR_Rem01REM_Valeur)+","+str(FA_Frais03FR_Rem01REM_Type)+","+str(FA_Frais03FR_Rem02REM_Valeur)+","+str(FA_Frais03FR_Rem02REM_Type)+","+str(FA_Frais03FR_Rem03REM_Valeur)+","+str(FA_Frais03FR_Rem03REM_Type)+","+str(FA_Contremarque)+","+str(FA_FactPoids)+","+str(FA_FactForfait)+","+str(FA_Publie)+",'"+str(FA_RacineRef)+"','"+str(FA_RacineCB)+"',"+str(CL_No1)+","+str(cbCL_No1)+","+str(CL_No2)+","+str(cbCL_No2)+","+str(CL_No3)+","+str(cbCL_No3)+","+str(CL_No4)+","+str(cbCL_No4)+","+str(FA_Nature)+","+str(FA_NbColis)+","+str(FA_SousTraitance)+","+str(FA_Fictif)+",'"+str(cbCreateur)+"')")
					_logger.error(tt)
					cursor.execute("INSERT INTO F_FAMILLE (FA_CodeFamille,FA_Type,FA_Intitule,FA_UniteVen,FA_Coef,FA_SuiviStock,FA_Garantie,FA_Central,FA_Stat01,FA_Stat02,FA_Stat03,FA_Stat04,FA_Stat05,FA_CodeFiscal,FA_Pays,FA_UnitePoids,FA_Escompte,FA_Delai,FA_HorsStat,FA_VteDebit,FA_NotImp,FA_Frais01FR_Denomination,FA_Frais01FR_Rem01REM_Valeur,FA_Frais01FR_Rem01REM_Type,FA_Frais01FR_Rem02REM_Valeur,FA_Frais01FR_Rem02REM_Type,FA_Frais01FR_Rem03REM_Valeur,FA_Frais01FR_Rem03REM_Type,FA_Frais02FR_Denomination,FA_Frais02FR_Rem01REM_Valeur,FA_Frais02FR_Rem01REM_Type,FA_Frais02FR_Rem02REM_Valeur,FA_Frais02FR_Rem02REM_Type,FA_Frais02FR_Rem03REM_Valeur,FA_Frais02FR_Rem03REM_Type,FA_Frais03FR_Denomination,FA_Frais03FR_Rem01REM_Valeur,FA_Frais03FR_Rem01REM_Type,FA_Frais03FR_Rem02REM_Valeur,FA_Frais03FR_Rem02REM_Type,FA_Frais03FR_Rem03REM_Valeur,FA_Frais03FR_Rem03REM_Type,FA_Contremarque,FA_FactPoids,FA_FactForfait,FA_Publie,FA_RacineRef,FA_RacineCB,CL_No1,cbCL_No1,CL_No2,cbCL_No2,CL_No3,cbCL_No3,CL_No4,cbCL_No4,FA_Nature,FA_NbColis,FA_SousTraitance,FA_Fictif,cbCreateur) VALUES('"+str(FA_CodeFamille)+"',"+str(FA_Type)+",'"+str(FA_Intitule)+"',"+str(FA_UniteVen)+","+str(FA_Coef)+","+str(FA_SuiviStock)+","+str(FA_Garantie)+",'"+str(FA_Central)+"','"+str(FA_Stat01)+"','"+str(FA_Stat02)+"','"+str(FA_Stat03)+"','"+str(FA_Stat04)+"','"+str(FA_Stat05)+"','"+str(FA_CodeFiscal)+"','"+str(FA_Pays)+"',"+str(FA_UnitePoids)+","+str(FA_Escompte)+","+str(FA_Delai)+","+str(FA_HorsStat)+","+str(FA_VteDebit)+","+str(FA_NotImp)+",'"+str(FA_Frais01FR_Denomination)+"',"+str(FA_Frais01FR_Rem01REM_Valeur)+","+str(FA_Frais01FR_Rem01REM_Type)+","+str(FA_Frais01FR_Rem02REM_Valeur)+","+str(FA_Frais01FR_Rem02REM_Type)+","+str(FA_Frais01FR_Rem03REM_Valeur)+","+str(FA_Frais01FR_Rem03REM_Type)+",'"+str(FA_Frais02FR_Denomination)+"',"+str(FA_Frais02FR_Rem01REM_Valeur)+","+str(FA_Frais02FR_Rem01REM_Type)+","+str(FA_Frais02FR_Rem02REM_Valeur)+","+str(FA_Frais02FR_Rem02REM_Type)+","+str(FA_Frais02FR_Rem03REM_Valeur)+","+str(FA_Frais02FR_Rem03REM_Type)+",'"+str(FA_Frais03FR_Denomination)+"',"+str(FA_Frais03FR_Rem01REM_Valeur)+","+str(FA_Frais03FR_Rem01REM_Type)+","+str(FA_Frais03FR_Rem02REM_Valeur)+","+str(FA_Frais03FR_Rem02REM_Type)+","+str(FA_Frais03FR_Rem03REM_Valeur)+","+str(FA_Frais03FR_Rem03REM_Type)+","+str(FA_Contremarque)+","+str(FA_FactPoids)+","+str(FA_FactForfait)+","+str(FA_Publie)+",'"+str(FA_RacineRef)+"','"+str(FA_RacineCB)+"',"+str(CL_No1)+","+str(cbCL_No1)+","+str(CL_No2)+","+str(cbCL_No2)+","+str(CL_No3)+","+str(cbCL_No3)+","+str(CL_No4)+","+str(cbCL_No4)+","+str(FA_Nature)+","+str(FA_NbColis)+","+str(FA_SousTraitance)+","+str(FA_Fictif)+",'"+str(cbCreateur)+"')")
					conn.commit() 
			
			
					cursor.execute("select MAX(AG_No) from F_ARTGAMME")
					rows_AG_No = cursor.fetchall()
					
					
					for lines_AG_Noo in range(len(rows_AG_No)):
						
						AG_Noo =  rows_AG_No[lines_AG_Noo][0]
					
					
							  
					_logger.error('3')
					tu = ("INSERT INTO  F_Article(AR_Ref,AR_Design,FA_CodeFamille,AR_Substitut,AR_Raccourci,AR_Garantie,AR_UnitePoids,AR_PoidsNet,AR_PoidsBrut,AR_UniteVen,AR_PrixAch,AR_Coef,AR_PrixVen,AR_PrixTTC,AR_Gamme1,AR_Gamme2,AR_SuiviStock,AR_Nomencl,AR_Stat01,AR_Stat02,AR_Stat03,AR_Stat04,AR_Stat05,AR_Escompte,AR_Delai,AR_HorsStat,AR_VteDebit,AR_NotImp,AR_Sommeil,AR_Langue1,AR_Langue2,AR_EdiCode,AR_CodeBarre,AR_CodeFiscal,AR_Pays,AR_Frais01FR_Denomination,AR_Frais01FR_Rem01REM_Valeur,AR_Frais01FR_Rem01REM_Type,AR_Frais01FR_Rem02REM_Valeur,AR_Frais01FR_Rem02REM_Type,AR_Frais01FR_Rem03REM_Valeur,AR_Frais01FR_Rem03REM_Type,AR_Frais02FR_Denomination,AR_Frais02FR_Rem01REM_Valeur,AR_Frais02FR_Rem01REM_Type,AR_Frais02FR_Rem02REM_Valeur,AR_Frais02FR_Rem02REM_Type,AR_Frais02FR_Rem03REM_Valeur,AR_Frais02FR_Rem03REM_Type,AR_Frais03FR_Rem01REM_Valeur,AR_Frais03FR_Rem01REM_Type,AR_Frais03FR_Rem02REM_Valeur,AR_Frais03FR_Rem02REM_Type,AR_Frais03FR_Rem03REM_Valeur,AR_Frais03FR_Rem03REM_Type,AR_Condition,AR_PUNet,AR_Contremarque,AR_FactPoids,AR_FactForfait,AR_DateCreation,AR_SaisieVar,AR_Transfere,AR_Publie,AR_DateModif,AR_Photo,AR_PrixAchNouv,AR_CoefNouv,AR_PrixVenNouv,AR_DateApplication,AR_CoutStd,AR_QteComp,AR_QteOperatoire,CO_No,cbCO_No,AR_Prevision,CL_No1,cbCL_No1,CL_No2,cbCL_No2,CL_No3,cbCL_No3,CL_No4,cbCL_No4,AR_Type,RP_CodeDefaut,AR_Nature,AR_DelaiFabrication,AR_NbColis,AR_DelaiPeremption,AR_DelaiSecurite,AR_Fictif,AR_SousTraitance,AR_TypeLancement,AR_Cycle,cbCreateur) values ('"+str(AR_Ref)+"','"+str(AR_Design)+"','"+str(FA_CodeFamille)+"','"+str(AR_Substitut)+"',"+str(AR_Raccourci)+","+str(AR_Garantie)+","+str(AR_UnitePoids)+","+str(AR_PoidsNet)+","+str(AR_PoidsBrut)+","+str(AR_UniteVen)+","+str(AR_PrixAch)+","+str(AR_Coef)+","+str(AR_PrixVen)+","+str(AR_PrixTTC)+","+str(AR_Gamme1)+","+str(AR_Gamme2)+","+str(AR_SuiviStock)+","+str(AR_Nomencl)+",'"+str(AR_Stat01)+"','"+str(AR_Stat02)+"','"+str(AR_Stat03)+"','"+str(AR_Stat04)+"','"+str(AR_Stat05)+"',"+str(AR_Escompte)+","+str(AR_Delai)+","+str(AR_HorsStat)+","+str(AR_VteDebit)+","+str(AR_NotImp)+","+str(AR_Sommeil)+",'"+str(AR_Langue1)+"','"+str(AR_Langue2)+"',"+str(AR_EdiCode)+","+str(AR_CodeBarre)+",'"+str(AR_CodeFiscal)+"','"+str(AR_Pays)+"','"+str(AR_Frais01FR_Denomination)+"',"+str(AR_Frais01FR_Rem01REM_Valeur)+","+str(AR_Frais01FR_Rem01REM_Type)+","+str(AR_Frais01FR_Rem02REM_Valeur)+","+str(AR_Frais01FR_Rem02REM_Type)+","+str(AR_Frais01FR_Rem03REM_Valeur)+","+str(AR_Frais01FR_Rem03REM_Type)+",'"+str(AR_Frais02FR_Denomination)+"',"+str(AR_Frais02FR_Rem01REM_Valeur)+","+str(AR_Frais02FR_Rem01REM_Type)+","+str(AR_Frais02FR_Rem02REM_Valeur)+","+str(AR_Frais02FR_Rem02REM_Type)+","+str(AR_Frais02FR_Rem03REM_Valeur)+","+str(AR_Frais02FR_Rem03REM_Type)+","+str(AR_Frais03FR_Rem01REM_Valeur)+","+str(AR_Frais03FR_Rem01REM_Type)+","+str(AR_Frais03FR_Rem02REM_Valeur)+","+str(AR_Frais03FR_Rem02REM_Type)+","+str(AR_Frais03FR_Rem03REM_Valeur)+","+str(AR_Frais03FR_Rem03REM_Type)+","+str(AR_Condition)+","+str(AR_PUNet)+","+str(AR_Contremarque)+","+str(AR_FactPoids)+","+str(AR_FactForfait)+",'"+str(AR_DateCreation)+"',"+str(AR_SaisieVar)+","+str(AR_Transfere)+","+str(AR_Publie)+",'"+str(AR_DateModif)+"','"+str(AR_Photo)+"',"+str(AR_PrixAchNouv)+","+str(AR_CoefNouv)+","+str(AR_PrixVenNouv)+",'"+str(AR_DateApplication)+"',"+str(AR_CoutStd)+","+str(AR_QteComp)+","+str(AR_QteOperatoire)+","+str(CO_No)+","+str(cbCO_No)+","+str(AR_Prevision)+","+str(CL_No1)+","+str(cbCL_No1)+","+str(CL_No2)+","+str(cbCL_No2)+","+str(CL_No3)+","+str(cbCL_No3)+","+str(CL_No4)+","+str(cbCL_No4)+","+str(AR_Type)+","+str(RP_CodeDefaut)+","+str(AR_Nature)+","+str(AR_DelaiFabrication)+","+str(AR_NbColis)+","+str(AR_DelaiPeremption)+","+str(AR_DelaiSecurite)+","+str(AR_Fictif)+",'"+str(AR_SousTraitance)+"',"+str(AR_TypeLancement)+",'"+str(cbCreateur)+"')")
					_logger.error(tu)
					cursor.execute ("INSERT INTO  F_Article(AR_Ref,AR_Design,FA_CodeFamille,AR_Substitut,AR_Raccourci,AR_Garantie,AR_UnitePoids,AR_PoidsNet,AR_PoidsBrut,AR_UniteVen,AR_PrixAch,AR_Coef,AR_PrixVen,AR_PrixTTC,AR_Gamme1,AR_Gamme2,AR_SuiviStock,AR_Nomencl,AR_Stat01,AR_Stat02,AR_Stat03,AR_Stat04,AR_Stat05,AR_Escompte,AR_Delai,AR_HorsStat,AR_VteDebit,AR_NotImp,AR_Sommeil,AR_Langue1,AR_Langue2,AR_EdiCode,AR_CodeBarre,AR_CodeFiscal,AR_Pays,AR_Frais01FR_Denomination,AR_Frais01FR_Rem01REM_Valeur,AR_Frais01FR_Rem01REM_Type,AR_Frais01FR_Rem02REM_Valeur,AR_Frais01FR_Rem02REM_Type,AR_Frais01FR_Rem03REM_Valeur,AR_Frais01FR_Rem03REM_Type,AR_Frais02FR_Denomination,AR_Frais02FR_Rem01REM_Valeur,AR_Frais02FR_Rem01REM_Type,AR_Frais02FR_Rem02REM_Valeur,AR_Frais02FR_Rem02REM_Type,AR_Frais02FR_Rem03REM_Valeur,AR_Frais02FR_Rem03REM_Type,AR_Frais03FR_Rem01REM_Valeur,AR_Frais03FR_Rem01REM_Type,AR_Frais03FR_Rem02REM_Valeur,AR_Frais03FR_Rem02REM_Type,AR_Frais03FR_Rem03REM_Valeur,AR_Frais03FR_Rem03REM_Type,AR_Condition,AR_PUNet,AR_Contremarque,AR_FactPoids,AR_FactForfait,AR_DateCreation,AR_SaisieVar,AR_Transfere,AR_Publie,AR_DateModif,AR_Photo,AR_PrixAchNouv,AR_CoefNouv,AR_PrixVenNouv,AR_DateApplication,AR_CoutStd,AR_QteComp,AR_QteOperatoire,CO_No,cbCO_No,AR_Prevision,CL_No1,cbCL_No1,CL_No2,cbCL_No2,CL_No3,cbCL_No3,CL_No4,cbCL_No4,AR_Type,RP_CodeDefaut,AR_Nature,AR_DelaiFabrication,AR_NbColis,AR_DelaiPeremption,AR_DelaiSecurite,AR_Fictif,AR_SousTraitance,AR_TypeLancement,cbCreateur) values ('"+str(AR_Ref)+"','"+str(AR_Design)+"','"+str(FA_CodeFamille)+"','"+str(AR_Substitut)+"',"+str(AR_Raccourci)+","+str(AR_Garantie)+","+str(AR_UnitePoids)+","+str(AR_PoidsNet)+","+str(AR_PoidsBrut)+","+str(AR_UniteVen)+","+str(AR_PrixAch)+","+str(AR_Coef)+","+str(AR_PrixVen)+","+str(AR_PrixTTC)+","+str(AR_Gamme1)+","+str(AR_Gamme2)+","+str(AR_SuiviStock)+","+str(AR_Nomencl)+",'"+str(AR_Stat01)+"','"+str(AR_Stat02)+"','"+str(AR_Stat03)+"','"+str(AR_Stat04)+"','"+str(AR_Stat05)+"',"+str(AR_Escompte)+","+str(AR_Delai)+","+str(AR_HorsStat)+","+str(AR_VteDebit)+","+str(AR_NotImp)+","+str(AR_Sommeil)+",'"+str(AR_Langue1)+"','"+str(AR_Langue2)+"',"+str(AR_EdiCode)+","+str(AR_CodeBarre)+",'"+str(AR_CodeFiscal)+"','"+str(AR_Pays)+"','"+str(AR_Frais01FR_Denomination)+"',"+str(AR_Frais01FR_Rem01REM_Valeur)+","+str(AR_Frais01FR_Rem01REM_Type)+","+str(AR_Frais01FR_Rem02REM_Valeur)+","+str(AR_Frais01FR_Rem02REM_Type)+","+str(AR_Frais01FR_Rem03REM_Valeur)+","+str(AR_Frais01FR_Rem03REM_Type)+",'"+str(AR_Frais02FR_Denomination)+"',"+str(AR_Frais02FR_Rem01REM_Valeur)+","+str(AR_Frais02FR_Rem01REM_Type)+","+str(AR_Frais02FR_Rem02REM_Valeur)+","+str(AR_Frais02FR_Rem02REM_Type)+","+str(AR_Frais02FR_Rem03REM_Valeur)+","+str(AR_Frais02FR_Rem03REM_Type)+","+str(AR_Frais03FR_Rem01REM_Valeur)+","+str(AR_Frais03FR_Rem01REM_Type)+","+str(AR_Frais03FR_Rem02REM_Valeur)+","+str(AR_Frais03FR_Rem02REM_Type)+","+str(AR_Frais03FR_Rem03REM_Valeur)+","+str(AR_Frais03FR_Rem03REM_Type)+","+str(AR_Condition)+","+str(AR_PUNet)+","+str(AR_Contremarque)+","+str(AR_FactPoids)+","+str(AR_FactForfait)+",'"+str(AR_DateCreation)+"',"+str(AR_SaisieVar)+","+str(AR_Transfere)+","+str(AR_Publie)+",'"+str(AR_DateModif)+"','"+str(AR_Photo)+"',"+str(AR_PrixAchNouv)+","+str(AR_CoefNouv)+","+str(AR_PrixVenNouv)+",'"+str(AR_DateApplication)+"',"+str(AR_CoutStd)+","+str(AR_QteComp)+","+str(AR_QteOperatoire)+","+str(CO_No)+","+str(cbCO_No)+","+str(AR_Prevision)+","+str(CL_No1)+","+str(cbCL_No1)+","+str(CL_No2)+","+str(cbCL_No2)+","+str(CL_No3)+","+str(cbCL_No3)+","+str(CL_No4)+","+str(cbCL_No4)+","+str(AR_Type)+","+str(RP_CodeDefaut)+","+str(AR_Nature)+","+str(AR_DelaiFabrication)+","+str(AR_NbColis)+","+str(AR_DelaiPeremption)+","+str(AR_DelaiSecurite)+","+str(AR_Fictif)+",'"+str(AR_SousTraitance)+"',"+str(AR_TypeLancement)+",'"+str(cbCreateur)+"')")
					conn.commit()
					
					_logger.error('2')

					_logger.error('4')					
					if len(sale.product_id.product_variant_ids) > 1:
							_logger.error('omapaua')
							for line_gamme in sale.product_id.product_variant_ids:
								AR_PUNet = sale.product_id.lst_price
								
								cursor.execute("select MAX(AG_No) from F_ARTGAMME")   
								rows_AG_No = cursor.fetchall()
								for lines_AG_Noo in range(len(rows_AG_No)):
									AG_Noo =  rows_AG_No[lines_AG_Noo][0]
								AG_No = AG_Noo +1
								
								AG_Type = 0
								
								cbCreateur= 'COLU'  
								AG_No2 = 0
								
								ARy_Gamme1 = sale.product_id.attribute_line_ids.attribute_id.numero
								
								AR_Ref_art = sale.product_id.product_tmpl_id.default_code25
								
								ARi_Design = sale.product_id.product_tmpl_id.name
								ARr_Substitut = sale.product_id.product_tmpl_id.default_code25
								
								
								
								for lii in line_gamme :
									
									
									

									AE_Reff = lii.default_code
									AE_PrixAch = lii.lst_price
									AE_CodeBarre = lii.barcode
									AR_CoutStd = lii.standard_price
									
									for lio in lii.attribute_value_ids :
										EG_Enumeree = lio.name  
									EG_Enumere = EG_Enumeree
									AG_No2 = 0
									
									
									cursor.execute ("INSERT INTO  F_ARTGAMME(AR_Ref,AG_No,EG_Enumere,AG_Type,cbCreateur) values ('"+str(AR_Ref_art)+"',"+str(AG_No)+",'"+str(EG_Enumere)+"',0,'"+str(cbCreateur)+"')")
									conn.commit()  
									
									cursor.execute ("INSERT INTO  F_ARTENUMREF(AR_Ref,AG_No1,AG_No2,AE_Ref,AE_PrixAch,AE_CodeBarre,AE_PrixAchNouv,AE_EdiCode,AE_Sommeil,cbCreateur) values ('"+str(AR_Ref_art)+"',"+str(AG_No)+","+str(AG_No2)+",'"+str(AE_CodeBarre)+"',"+str(AE_PrixAch)+",'"+str(AE_CodeBarre)+"',0,'1',0,'"+str(cbCreateur)+"')")
									conn.commit()  
									
									cursor.execute ("INSERT INTO  F_ARTPRIX(AR_Ref,AG_No1,AG_No2,AR_PUNet,AR_CoutStd,cbCreateur) values ('"+str(AR_Ref_art)+"',"+str(AG_No)+","+str(AG_No2)+","+str(AR_PUNet)+","+str(AR_CoutStd)+",'"+str(cbCreateur)+"')")
									conn.commit() 
									
			
		
			if len(sale.product_id.product_variant_ids) <= 1:
				qty1 = sale.qty1
				qty2 = sale.qty2
				qty3 = sale.qty3
				qty4 = sale.qty4
				prix1 = sale.prix1
				prix2 = sale.prix2
				prix3 = sale.prix3
				prix4 = sale.prix4
				for lineee in sale :
					AC_RefClient = sale.reference
					cursor.execute("select AR_Ref  from F_ARTCLIENT")   
					rows_Artcli = cursor.fetchall()
					for lines_Artc in range(len(rows_Artcli)):
						if AR_Ref  == rows_Artcli[lines_Artc][0]:
							
				
							_logger.error('F_ARTCLIENT existe')
							break
					else :
						er=("INSERT INTO F_ARTCLIENT (AR_Ref,AC_Categorie,AC_PrixVen,AC_Coef,AC_PrixTTC,AC_Arrondi,AC_QteMont,EG_Champ,AC_PrixDev,AC_Devise,CT_Num,AC_Remise,AC_Calcul,AC_TypeRem,AC_RefClient,AC_CoefNouv,AC_PrixVenNouv,AC_PrixDevNouv,AC_RemiseNouv,AC_DateApplication,cbCreateur) VALUES ('"+str(AR_Ref)+"',0,0,0,0,0,3,6,0,0,'"+str(CT_Num)+"',0,0,0,'"+str(AC_RefClient)+"',0,0,0,0,'1900-01-01 00:00:00','COLU')")
						_logger.error(er)
						cursor.execute ("INSERT INTO F_ARTCLIENT (AR_Ref,AC_Categorie,AC_PrixVen,AC_Coef,AC_PrixTTC,AC_Arrondi,AC_QteMont,EG_Champ,AC_PrixDev,AC_Devise,CT_Num,AC_Remise,AC_Calcul,AC_TypeRem,AC_RefClient,AC_CoefNouv,AC_PrixVenNouv,AC_PrixDevNouv,AC_RemiseNouv,AC_DateApplication,cbCreateur) VALUES ('"+str(AR_Ref)+"',0,0,0,0,0,3,6,0,0,'"+str(CT_Num)+"',0,0,0,'"+str(AC_RefClient)+"',0,0,0,0,'1900-01-01 00:00:00','COLU')")
						conn.commit() 
					
				
							
						
				if  sale.qty1 >= 0 :  
					
					r=("INSERT INTO F_TARIFQTE (AR_Ref,TQ_RefCF,TQ_BorneSup,TQ_Remise01REM_Valeur,TQ_Remise01REM_Type,TQ_Remise02REM_Valeur,TQ_Remise02REM_Type,TQ_Remise03REM_Valeur,TQ_Remise03REM_Type,TQ_PrixNet,cbCreateur) VALUES('"+str(AR_Ref)+"','"+str(CT_Num)+"',"+str(qty1)+","+str(prix1)+",2,0,0,0,0,0,'COLU')")
					_logger.error(r)
					cursor.execute ("INSERT INTO F_TARIFQTE (AR_Ref,TQ_RefCF,TQ_BorneSup,TQ_Remise01REM_Valeur,TQ_Remise01REM_Type,TQ_Remise02REM_Valeur,TQ_Remise02REM_Type,TQ_Remise03REM_Valeur,TQ_Remise03REM_Type,TQ_PrixNet,cbCreateur) VALUES('"+str(AR_Ref)+"','"+str(CT_Num)+"',"+str(qty1)+",0,2,0,0,0,0,"+str(prix1)+",'COLU')")
					conn.commit()   


					
				if  sale.qty2 >= 1 :
					_logger.error("ioioi")
					cursor.execute ("INSERT INTO F_TARIFQTE (AR_Ref,TQ_RefCF,TQ_BorneSup,TQ_Remise01REM_Valeur,TQ_Remise01REM_Type,TQ_Remise02REM_Valeur,TQ_Remise02REM_Type,TQ_Remise03REM_Valeur,TQ_Remise03REM_Type,TQ_PrixNet,cbCreateur) VALUES('"+str(AR_Ref)+"','"+str(CT_Num)+"',"+str(qty2)+",0,2,0,0,0,0,"+str(prix2)+",'COLU')")
					conn.commit()  


					
				if  sale.qty3 >= 1 :
					_logger.error("hihhi")
					cursor.execute ("INSERT INTO F_TARIFQTE (AR_Ref,TQ_RefCF,TQ_BorneSup,TQ_Remise01REM_Valeur,TQ_Remise01REM_Type,TQ_Remise02REM_Valeur,TQ_Remise02REM_Type,TQ_Remise03REM_Valeur,TQ_Remise03REM_Type,TQ_PrixNet,cbCreateur) VALUES('"+str(AR_Ref)+"','"+str(CT_Num)+"',"+str(qty3)+",0,2,0,0,0,0,"+str(prix3)+",'COLU')")
					conn.commit() 


					
				if  sale.qty4 >= 1 :
					_logger.error("hjb")
					cursor.execute ("INSERT INTO F_TARIFQTE (AR_Ref,TQ_RefCF,TQ_BorneSup,TQ_Remise01REM_Valeur,TQ_Remise01REM_Type,TQ_Remise02REM_Valeur,TQ_Remise02REM_Type,TQ_Remise03REM_Valeur,TQ_Remise03REM_Type,TQ_PrixNet,cbCreateur) VALUES('"+str(AR_Ref)+"','"+str(CT_Num)+"',"+str(qty4)+",0,2,0,0,0,0,"+str(prix4)+",'COLU')")
					conn.commit() 


				 
							
	@api.multi 
	def action_just_confirm(self):
		for order in self:
			if order.state == 'draft':
				name = 'Pre_BC'
				order.state = 'sale'
			
		if self.env['ir.values'].get_default('sale.config.settings', 'auto_done_setting'):
			self.action_done()
		self.create_devis()
		return True
	
	def length(self):  
		  
		return len(self.order_line)

	@api.multi
	def create_devis_cmde(self) :

		server = self.env['parametrage.sage'].search([]).serveur   
		user = self.env['parametrage.sage'].search([]).UID 
		password = self.env['parametrage.sage'].search([]).PWD 
		database = self.env['parametrage.sage'].search([]).DATABASE

		conn = pymssql.connect(server +':1433', user, password, database)
		cursor = conn.cursor()	
		
		
	
		
		CG_Num = self.partner_id.property_account_receivable_id
		CG_Type = 0
		CG_Intitule = self.partner_id.name
		CG_Classement = self.partner_id.name
		N_Nature = 6
		CG_Report = 1
		CR_Num = 'NULL'
		CG_Analytique = 0
		CG_Echeance = 0
		CG_Quantite = 0
		CG_Lettrage = 0
		CG_Tiers = 0
		CG_DateCreate  = self._get_defaut_date()
		CG_Devise = 1
		N_Devise = 1
		TA_Code = 0
		CG_Sommeil = 1
		CG_ReportAnal = 0
		CT_Num=self.partner_id.ct_num
		CT_Type = 0
		CT_Intitule = self.partner_id.name
		CG_NumPrinc = self.partner_id.property_account_receivable_id
		CT_Qualite = 'NULL'
		CT_Classement = self.partner_id.name
		CT_Contact = self.partner_id.name
		Ct_Adresse = self.partner_id.street
		Ct_Complement = self.partner_id.city
		CT_CodePostal = self.partner_id.city
		CT_Ville = self.partner_id.city
		CT_CodeReqion = self.partner_id.city
		CT_Pays = self.partner_id.city
		Ct_Raccourci = "NULL"
		Bt_num = 0
		N_Devise = 0
		CT_Ape = 0
		CT_Identifiant = 0
		CT_Siret = 0
		CT_Statistique01 = 0
		CT_Statistique02= 0 
		CT_Statistique03 =0 
		CT_Statistique04 =0 
		CT_Statistique05 =0 
		CT_Statistique06 =0 
		CT_Statistique07 =0 
		CT_Statistique08 =0 
		CT_Statistique09 =0 
		CT_Statistique10 =0 
		CT_Commentaire = 'NULL'
		CT_Encours ='NULL'
		CT_Assurance = 'NULL'
		N_Risque ='NULL'
		CO_No = 0
		N_CatTarif = 0
		CT_Taux01 = 0
		CT_Taux02 = 0
		CT_Taux03 = 0
		CT_Taux04 = 0
		N_CatCompta = 0
		N_Period = 0
		Ct_Facture =0
		CT_BLFact =0 
		CT_Langue = 0
		N_Expedition =0 
		N_Condition =0
		CT_DateCreat =0
		CT_Saut =0 
		CT_Lettrage =0 
		CT_ValidEch =0
		CT_Sommeil =0
		NE_No = 0
		CT_ControlEnc =0
		CT_NotRappel =0
		N_Analytique =0
		CA_Num =0 
		CT_Telephone = self.partner_id.phone
		CT_Telecopie = self.partner_id.fax
		CT_Email = self.partner_id.email
		CT_Site = self.partner_id.city
		CT_Surveillance = self.partner_id.phone
		DO_Piece = self.name
		DO_Date = self.date_order
		DO_Ref =0

		CT_Num =  self.ct_num 
		cursor.execute("select DO_Piece from F_DOCENTETE")
		
		rows_DL_pi = cursor.fetchall()
		
		for line_piece  in range(len(rows_DL_pi)):
			
			if DO_Piece  == rows_DL_pi[line_piece][0]:
				_logger.error('bc existe')

				break
				
		else :
		
			tt = "INSERT INTO F_DOCENTETE(DO_Domaine,DO_Type,DO_Piece,DO_Date,DO_Ref,DO_Tiers,CT_NumPayeur,CG_Num) VALUES (0,1,'"+str(DO_Piece)+"','"+str(DO_Date)+"','"+str(DO_Ref)+"','"+str(CT_Num)+"','"+str(CT_Num)+"','"+str(CG_Num)+"')"
			conn.commit()
			_logger.error(tt)
			cursor.execute("INSERT INTO F_DOCENTETE(DO_Domaine,DO_Type,DO_Piece,DO_Date,DO_Ref,DO_Tiers,CT_NumPayeur,CG_Num) VALUES (0,1,'"+str(DO_Piece)+"','"+str(DO_Date)+"','"+str(DO_Ref)+"','"+str(CT_Num)+"','"+str(CT_Num)+"','"+str(CG_Num)+"')")
			conn.commit()
				
			
			for sale_ligne in self.order_line :
				cursor.execute("select MAX(DL_No) from F_DOCLIGNE")
				rows_DL_No = cursor.fetchall()
				
				
				for lines_DL_Noo in range(len(rows_DL_No)):
					
					No =  rows_DL_No[lines_DL_Noo][0]

				
				DO_Domaine = 0
				DO_Type = 1
				DO_Piece = self.name
				CT_Num = self.ct_num
				DL_PieceBC = ''
				DL_PieceBL = ''
				DO_Date = self.date_order
				DL_DateBC =  self.date_order
				DL_DateBL =  self.date_order
				DL_Ligne = self.length()
				DO_Ref =0
				DL_TNomencl = 0
				DL_TRemPied = 0
				DL_TRemExep = 0
				AR_Ref = sale_ligne.product_id.product_tmpl_id.default_code
				if len(sale_ligne.product_id.product_variant_ids) <= 1:
					DL_Design = sale_ligne.product_id.name
					_logger.error(DL_Design)
				else :
					DL_Design = sale_ligne.product_id.product_tmpl_id.name
					_logger.error(DL_Design)
				DL_Qte = sale_ligne.product_uom_qty
				DL_QteBC = sale_ligne.product_uom_qty
				DL_QteBL = sale_ligne.product_uom_qty
				DL_PoidsNet = sale_ligne.product_id.weight
				DL_PoidsBrut = 0
				DL_Remise01REM_Valeur = 0
				DL_Remise01REM_Type = 0
				DL_Remise02REM_Valeur = 0
				DL_Remise02REM_Type = 0
				DL_Remise03REM_Valeur = 0
				DL_Remise03REM_Type = 0
				DL_PrixUnitaire = sale_ligne.product_id.standard_price
				DL_PUBC = 0
				DL_Taxe1 = 0
				DL_TypeTaux1 = 0
				DL_TypeTaxe1 = 0
				DL_Taxe2 = 0
				DL_TypeTaux2 = 0
				DL_TypeTaxe2 = 0
				CO_No = 0 
				cbCO_No = 'NULL'
				AG_No1 = 0
				AG_No2 = 0
				DL_PrixRU = 0
				DL_CMUP = 0
				DL_MvtStock = 6
				DT_No = 0
				cbDT_No = 'NULL'
				AF_RefFourniss = ''
				EU_Enumere = 0
				EU_Qte = sale_ligne.product_uom_qty
				DL_TTC = 0
				DE_No = 2 
				cbDE_No = 2 
				DL_NoRef = 1
				DL_TypePL = 0 
				DL_PUDevise = 0
				DL_PUTTC = sale_ligne.product_id.standard_price
				# *******
				DL_No = No +1
				DO_DateLivr =  self.date_order
				CA_Num = ''
				DL_Taxe3 = 0
				DL_TypeTaux3 = 0
				DL_TypeTaxe3 = 0
				DL_Frais = 0
				DL_Valorise = 1
				AR_RefCompose  = 'NULL'
				DL_NonLivre = 0
				AC_RefClient = ''
				DL_MontantHT  = sale_ligne.product_id.lst_price
				DL_MontantTTC = sale_ligne.product_id.lst_price
				DL_FactPoids = 0
				DL_Escompte = 0
				DL_PiecePL = ''
				DL_DatePL =  self.date_order
				DL_QtePL = sale_ligne.product_uom_qty
				DL_NoColis = ''
				DL_NoLink = 0 
				cbDL_NoLink = 'NULL'
				RP_Code = 'NULL'
				DL_QteRessource = 0
				DL_DateAvancement =  self.date_order
				PF_Num = ''
				DL_CodeTaxe1 = 'NULL'
				DL_CodeTaxe2 = 'NULL'
				DL_CodeTaxe3 = 'NULL'
				DL_PieceOFProd = 0
				DL_PieceDE = ''
				DL_DateDE = self.date_order
				DL_QteDE = sale_ligne.product_uom_qty
				DL_Operation = ''
				cbCreateur = 'COLU'
	  
				opii = ("INSERT INTO F_DOCLIGNE (DO_Domaine,DO_Type,CT_Num,DO_Piece,DL_PieceBC,DL_PieceBL,DO_Date,DL_DateBC,DL_DateBL,DL_Ligne,DO_Ref,DL_TNomencl,DL_TRemPied,DL_TRemExep,AR_Ref,DL_Design,DL_Qte,DL_QteBC,DL_QteBL,DL_PoidsNet,DL_PoidsBrut,DL_Remise01REM_Valeur,DL_Remise01REM_Type,DL_Remise02REM_Valeur,DL_Remise02REM_Type,DL_Remise03REM_Valeur,DL_Remise03REM_Type,DL_PrixUnitaire,DL_PUBC,DL_Taxe1,DL_TypeTaux1,DL_TypeTaxe1,DL_Taxe2,DL_TypeTaux2,DL_TypeTaxe2,CO_No,cbCO_No,AG_No1,AG_No2,DL_PrixRU,DL_CMUP,DL_MvtStock,DT_No,cbDT_No,AF_RefFourniss,EU_Enumere,EU_Qte,DL_TTC,DE_No,cbDE_No,DL_NoRef,DL_TypePL,DL_PUDevise,DL_PUTTC,DL_No,DO_DateLivr,CA_Num,DL_Taxe3,DL_TypeTaux3,DL_TypeTaxe3,DL_Frais,DL_Valorise,AR_RefCompose,DL_NonLivre,AC_RefClient,DL_MontantHT,DL_MontantTTC,DL_FactPoids,DL_Escompte,DL_PiecePL,DL_DatePL,DL_QtePL,DL_NoColis,DL_NoLink,cbDL_NoLink,RP_Code,DL_QteRessource,DL_DateAvancement,PF_Num,DL_CodeTaxe1,DL_CodeTaxe2,DL_CodeTaxe3,DL_PieceOFProd,cbCreateur)VALUES("+str(DO_Domaine)+","+str(DO_Type)+",'"+str(CT_Num)+"','"+str(DO_Piece)+"','"+str(DL_PieceBC)+"','"+str(DL_PieceBL)+"','"+str(DO_Date)+"','"+str(DL_DateBC)+"','"+str(DL_DateBL)+"',"+str(DL_Ligne)+",'"+str(DO_Ref)+"',"+str(DL_TNomencl)+","+str(DL_TRemPied)+","+str(DL_TRemExep)+",'"+str(AR_Ref)+"','"+str(DL_Design)+"',"+str(DL_Qte)+","+str(DL_QteBC)+","+str(DL_QteBL)+","+str(DL_PoidsNet)+","+str(DL_PoidsBrut)+","+str(DL_Remise01REM_Valeur)+","+str(DL_Remise01REM_Type)+","+str(DL_Remise02REM_Valeur)+","+str(DL_Remise02REM_Type)+","+str(DL_Remise03REM_Valeur)+","+str(DL_Remise03REM_Type)+","+str(DL_PrixUnitaire)+","+str(DL_PUBC)+","+str(DL_Taxe1)+","+str(DL_TypeTaux1)+","+str(DL_TypeTaxe1)+","+str(DL_Taxe2)+","+str(DL_TypeTaux2)+","+str(DL_TypeTaxe2)+","+str(CO_No)+","+str(cbCO_No)+","+str(AG_No1)+","+str(AG_No2)+","+str(DL_PrixRU)+","+str(DL_CMUP)+","+str(DL_MvtStock)+","+str(DT_No)+","+str(cbDT_No)+",'"+str(AF_RefFourniss)+"','"+str(EU_Enumere)+"',"+str(EU_Qte)+","+str(DL_TTC)+","+str(DE_No)+","+str(cbDE_No)+","+str(DL_NoRef)+","+str(DL_TypePL)+","+str(DL_PUDevise)+","+str(DL_PUTTC)+","+str(DL_No)+",'"+str(DO_DateLivr)+"','"+str(CA_Num)+"',"+str(DL_Taxe3)+","+str(DL_TypeTaux3)+","+str(DL_TypeTaxe3)+","+str(DL_Frais)+","+str(DL_Valorise)+","+str(AR_RefCompose)+","+str(DL_NonLivre)+",'"+str(AC_RefClient)+"',"+str(DL_MontantHT)+","+str(DL_MontantTTC)+","+str(DL_FactPoids)+","+str(DL_Escompte)+",'"+str(DL_PiecePL)+"','"+str(DL_DatePL)+"',"+str(DL_QtePL)+",'"+str(DL_NoColis)+"',"+str(DL_NoLink)+","+str(cbDL_NoLink)+","+str(RP_Code)+","+str(DL_QteRessource)+",'"+str(DL_DateAvancement)+"','"+str(PF_Num)+"',"+str(DL_CodeTaxe1)+","+str(DL_CodeTaxe2)+","+str(DL_CodeTaxe3)+","+str(DL_PieceOFProd)+",'"+str(cbCreateur)+"')")
				_logger.error('ffffffffffffffffffffff')
				_logger.error(opii)
				
				cursor.execute("INSERT INTO F_DOCLIGNE (DO_Domaine,DO_Type,CT_Num,DO_Piece,DL_PieceBC,DL_PieceBL,DO_Date,DL_DateBC,DL_DateBL,DL_Ligne,DO_Ref,DL_TNomencl,DL_TRemPied,DL_TRemExep,AR_Ref,DL_Design,DL_Qte,DL_QteBC,DL_QteBL,DL_PoidsNet,DL_PoidsBrut,DL_Remise01REM_Valeur,DL_Remise01REM_Type,DL_Remise02REM_Valeur,DL_Remise02REM_Type,DL_Remise03REM_Valeur,DL_Remise03REM_Type,DL_PrixUnitaire,DL_PUBC,DL_Taxe1,DL_TypeTaux1,DL_TypeTaxe1,DL_Taxe2,DL_TypeTaux2,DL_TypeTaxe2,CO_No,cbCO_No,AG_No1,AG_No2,DL_PrixRU,DL_CMUP,DL_MvtStock,DT_No,cbDT_No,AF_RefFourniss,EU_Enumere,EU_Qte,DL_TTC,DE_No,cbDE_No,DL_NoRef,DL_TypePL,DL_PUDevise,DL_PUTTC,DL_No,DO_DateLivr,CA_Num,DL_Taxe3,DL_TypeTaux3,DL_TypeTaxe3,DL_Frais,DL_Valorise,AR_RefCompose,DL_NonLivre,AC_RefClient,DL_MontantHT,DL_MontantTTC,DL_FactPoids,DL_Escompte,DL_PiecePL,DL_DatePL,DL_QtePL,DL_NoColis,DL_NoLink,cbDL_NoLink,RP_Code,DL_QteRessource,DL_DateAvancement,PF_Num,DL_CodeTaxe1,DL_CodeTaxe2,DL_CodeTaxe3,DL_PieceOFProd,cbCreateur)VALUES("+str(DO_Domaine)+","+str(DO_Type)+",'"+str(CT_Num)+"','"+str(DO_Piece)+"','"+str(DL_PieceBC)+"','"+str(DL_PieceBL)+"','"+str(DO_Date)+"','"+str(DL_DateBC)+"','"+str(DL_DateBL)+"',"+str(DL_Ligne)+",'"+str(DO_Ref)+"',"+str(DL_TNomencl)+","+str(DL_TRemPied)+","+str(DL_TRemExep)+",'"+str(AR_Ref)+"','"+str(DL_Design)+"',"+str(DL_Qte)+","+str(DL_QteBC)+","+str(DL_QteBL)+","+str(DL_PoidsNet)+","+str(DL_PoidsBrut)+","+str(DL_Remise01REM_Valeur)+","+str(DL_Remise01REM_Type)+","+str(DL_Remise02REM_Valeur)+","+str(DL_Remise02REM_Type)+","+str(DL_Remise03REM_Valeur)+","+str(DL_Remise03REM_Type)+","+str(DL_PrixUnitaire)+","+str(DL_PUBC)+","+str(DL_Taxe1)+","+str(DL_TypeTaux1)+","+str(DL_TypeTaxe1)+","+str(DL_Taxe2)+","+str(DL_TypeTaux2)+","+str(DL_TypeTaxe2)+","+str(CO_No)+","+str(cbCO_No)+","+str(AG_No1)+","+str(AG_No2)+","+str(DL_PrixRU)+","+str(DL_CMUP)+","+str(DL_MvtStock)+","+str(DT_No)+","+str(cbDT_No)+",'"+str(AF_RefFourniss)+"','"+str(EU_Enumere)+"',"+str(EU_Qte)+","+str(DL_TTC)+","+str(DE_No)+","+str(cbDE_No)+","+str(DL_NoRef)+","+str(DL_TypePL)+","+str(DL_PUDevise)+","+str(DL_PUTTC)+","+str(DL_No)+",'"+str(DO_DateLivr)+"','"+str(CA_Num)+"',"+str(DL_Taxe3)+","+str(DL_TypeTaux3)+","+str(DL_TypeTaxe3)+","+str(DL_Frais)+","+str(DL_Valorise)+","+str(AR_RefCompose)+","+str(DL_NonLivre)+",'"+str(AC_RefClient)+"',"+str(DL_MontantHT)+","+str(DL_MontantTTC)+","+str(DL_FactPoids)+","+str(DL_Escompte)+",'"+str(DL_PiecePL)+"','"+str(DL_DatePL)+"',"+str(DL_QtePL)+",'"+str(DL_NoColis)+"',"+str(DL_NoLink)+","+str(cbDL_NoLink)+","+str(RP_Code)+","+str(DL_QteRessource)+",'"+str(DL_DateAvancement)+"','"+str(PF_Num)+"',"+str(DL_CodeTaxe1)+","+str(DL_CodeTaxe2)+","+str(DL_CodeTaxe3)+","+str(DL_PieceOFProd)+",'"+str(cbCreateur)+"')")
				conn.commit()  
				
				
				
				

class SaleOrderLine(models.Model):
	_inherit = 'sale.order.line'
	
	
	
	
	qty1 = fields.Integer('qte 1' ,default= 1)
	qty2 = fields.Integer('qte 2' ,default= 0)
	qty3 = fields.Integer('qte 3'  ,default= 0 )
	qty4 = fields.Integer('qte 4'  ,default= 0 )
	prix1 = fields.Float('prix 1')
	prix2 = fields.Float('prix 2')
	prix3 = fields.Float('prix 3')
	prix4 = fields.Float('prix 4')
	barcode = fields.Char('barcode')
	qty_annuelle = fields.Integer('quantité annuelle')
	famille = fields.Char(string= 'Ref article commande')
	condition = fields.Char('Exigence Conditonnement')
	cliche = fields.Float('Cliché')
	outils = fields.Char ('Outils')
	exigence = fields.Char('Exigences qualité')
	dimension = fields.Char('Dimension')
	couleur = fields.Char('Couleur'  , size=7)
	reference = fields.Char(string= 'Ref article ODP')
	code_famille = fields.Char(string= 'Code famille sage')
	unite_de_vente = fields.Char(string= 'Unité de ventes')
	presentation = fields.Char(string= 'Présentation')
	exigence_technique = fields.Many2many('exigence.technique',string= 'Exigence technique')
	exigence_qualite = fields.Many2many('exigence.qualite',string= 'Exigence qualite')
	exigence_conditionnement = fields.Many2many('exigence.conditionnement',string= 'Exigence conditionnement')
	format = fields.Char(string= 'Format')
	matiere = fields.Many2many('matiere',string = 'Matiére')
	frais = fields.Float(string = 'Frais')
	wizard_deviss = fields.One2many('wizard.devis', 'devis_line', 'Related Packing Operations') 
	remarque = fields.Text(string = 'Remarque', compute= 'product_id_note' , store = True)
	default_name = fields.Char()
	delai = fields.Char('delai 1ére commande')
	@api.one
	@api.depends('product_id')
	def product_id_note(self):
		_logger.error("aazaza")
		
		self.remarque =  self.product_id.description_sale
		_logger.error(self.product_id.description_sale)
		
		_logger.error(self.remarque)
	
	
	@api.multi
	def get_action_exignece(self):
		action_ctx = dict(self.env.context)
		
		view_id = self.env.ref('crm_simsoft_sage.view_devis_wizard').id
		return {
			'name': _('Devis/'), 
			'type': 'ir.actions.act_window',
			'view_type': 'form',
			'view_mode': 'form',
			'res_model': 'sale.order.line',
			'views': [(view_id, 'form')],
			'view_id': view_id,
			'target': 'new',
			'res_id': self.ids[0],
			'context': action_ctx}
	wizard_devis = get_action_exignece
	
	@api.multi
	@api.onchange('product_id')
	def onchange_picking_type_id_product(self):
		self.famille = self.product_id.categ_id.name
		self.reference = self.product_id.default_code
		self.prix1 = self.product_id.list_price
		self.cliche = self.product_id.cliche
		self.presentation = self.product_id.presentation.name
		self.couleur = self.product_id.couleur.name
		self.dimension = self.product_id.dimension
		self.format = self.product_id.format
		self.matiere = [(6, 0, self.product_id.matiere.ids)] 
		self.frais = self.product_id.frais
		self.unite_de_vente=self.product_id.uom_id.name
		self.barcode=self.product_id.barcode
		self.default_name=self.product_id.name
		
		
		


	
class matiere_crm(models.Model):
	_name = 'matiere.crm'
	
	name = fields.Char('Nom')
	
class exigence_technique(models.Model):
	_name = 'exigence.technique'
	
	name = fields.Char('Nom')
	
class exigence_qualite(models.Model):
	_name = 'exigence.qualite'
	
	name = fields.Char('Nom')
	
class exigence_conditionnement(models.Model):
	_name = 'exigence.conditionnement'
	
	name = fields.Char('Nom')

	
