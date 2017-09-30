# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import RedirectWarning, UserError ,ValidationError
import logging

import datetime
_logger = logging.getLogger(__name__)


class wizard_devis(models.Model):

	_name = 'wizard.devis'
	
	@api.one
	@api.depends('devis_line.remarque')
	def product_id_noted(self):
		_logger.error("aazaza")
		
		self.remarque =  self.devis_line.remarque
		_logger.error(self.devis_line.remarque)
		
		_logger.error(self.remarque)

	devis_line = fields.Many2one('sale.order.line','devis',help='Quantity in the default UoM of the product' , readonly= True)

	exigence_technique = fields.Many2many('exigence.technique',string= 'Exigence technique')
	exigence_qualite = fields.Many2many('exigence.qualite',string= 'Exigence qualite')
	exigence_conditionnement = fields.Many2many('exigence.conditionnement',string= 'Exigence conditionnement')
	matiere = fields.Many2many('matiere',string = 'Matiére')  
	remarque = fields.Text(string = 'Remarque' , compute= 'product_id_noted' , store = True)
	outils = fields.Char ('Outils')
	delai = fields.Char('delai 1ére commande')