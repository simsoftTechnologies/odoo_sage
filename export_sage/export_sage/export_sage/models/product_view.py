# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models

# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import itertools
import psycopg2

import odoo.addons.decimal_precision as dp

from odoo import api, fields, models, tools, _
from odoo.exceptions import ValidationError, except_orm

import logging
_logger = logging.getLogger(__name__)

class product_category(models.Model):
	_inherit = "product.category"	

	code_famille= fields.Char(string="Code famille", required=True)	

class ProductUom(models.Model):
	_inherit = "product.uom"
	
	number = fields.Char(
	'Numero')
	

class ProductTemplate(models.Model):
	_inherit = "product.template"
	_description = "Product Template"
	_order = "name"

	
	  

  
	@api.depends('product_variant_ids', 'product_variant_ids.default_code')
	def _compute_default_code(self):
		unique_variants = self.filtered(lambda template: len(template.product_variant_ids) == 1)
		for template in unique_variants:
			template.default_code = template.product_variant_ids.default_code
		for template in (self - unique_variants):
			template.default_code = self.default_code25
	
	@api.multi
	@api.onchange('default_code')
	def default_code25r(self):
		self.default_code25 =  self.default_code
		_logger.error("zzzzzzzzzzzzzdsdsdsdzzzzzzzzzzzzzz")
		_logger.error(self.default_code25 )   
		
	@api.multi
	@api.onchange('barcode')
	def default_barcode25r(self): 
		self.barcode25 = self.barcode
		_logger.error("zzzzzzzzzzzzzzzzzzzzzzzzzzz")
		_logger.error(self.barcode25 ) 
		
	  
	@api.multi
	def create_variant_ids(self):
		
		Product = self.env["product.product"]
		for tmpl_id in self.with_context(active_test=False):
			# adding an attribute with only one value should not recreate product
			# write this attribute on every product to make sure we don't lose them
			variant_alone = tmpl_id.attribute_line_ids.filtered(lambda line: len(line.value_ids) == 1).mapped('value_ids')
			for value_id in variant_alone:
				updated_products = tmpl_id.product_variant_ids.filtered(lambda product: value_id.attribute_id not in product.mapped('attribute_value_ids.attribute_id'))
				updated_products.write({'attribute_value_ids': [(4, value_id.id)]})

			# list of values combination
			existing_variants = [set(variant.attribute_value_ids.ids) for variant in tmpl_id.product_variant_ids]
			variant_matrix = itertools.product(*(line.value_ids for line in tmpl_id.attribute_line_ids if line.value_ids and line.value_ids[0].attribute_id.create_variant))
			variant_matrix = map(lambda record_list: reduce(lambda x, y: x+y, record_list, self.env['product.attribute.value']), variant_matrix)
			to_create_variants = filter(lambda rec_set: set(rec_set.ids) not in existing_variants, variant_matrix)

			# check product
			variants_to_activate = self.env['product.product']
			variants_to_unlink = self.env['product.product']
			for product_id in tmpl_id.product_variant_ids:
				if not product_id.active and product_id.attribute_value_ids in variant_matrix:
					variants_to_activate |= product_id
				elif product_id.attribute_value_ids not in variant_matrix:
					variants_to_unlink |= product_id
			if variants_to_activate:
				variants_to_activate.write({'active': True})
			
			# create new product
			for variant_ids in to_create_variants:
				default_codre = ''
				barecode = ''
				for var in variant_ids:
					
					barecode +=str(self.barcode25)+ "-" + var.name  
					_logger.error(barecode)
					default_codre += str(self.default_code25) + "-" + var.name  
				new_variant = Product.create({
					'product_tmpl_id': tmpl_id.id,
					'default_code' : default_codre,
					'barcode': barecode,  
					'attribute_value_ids': [(6, 0, variant_ids.ids)]
					  
					
				})
			# unlink or inactive product
			for variant in variants_to_unlink:
				try:
					with self._cr.savepoint(), tools.mute_logger('odoo.sql_db'):
						variant.unlink()
				# We catch all kind of exception to be sure that the operation doesn't fail.
				except (psycopg2.Error, except_orm):
					variant.write({'active': False})
					pass
		return True

	default_code = fields.Char('Internal Reference',	compute = '_compute_default_code', inverse='_set_default_code', store=True )
	default_code25 = fields.Char('Internal Reference' )
	barcode = fields.Char('Barcode' , required = True )
	barcode25 = fields.Char('barcode' )
	dimension = fields.Char('Dimension')
	couleur = fields.Many2one('couleur',string='Couleur')
	presentation = fields.Many2one('presentation',string='Présentation :')
	emballage = fields.Char('Emballage')
	matiere = fields.Many2many('matiere',string='Matiére')
	cliche = fields.Float('Frais de cliché')
	frais = fields.Float('Frais outils')
	format = fields.Char('Format')
	remparque = fields.Char('Remarque')
	qty_vendu1 = fields.Char('quantité vendu n-1')
	qty_vendu2 = fields.Char('quantité vendu n-2')
	qty_vendu = fields.Char('quantité vendu n ')
	qty_previsionnement = fields.Integer('quantité prévisionnement')
	dernier_date_vente = fields.Date('derniere date de vente')
	dernier_date_achat = fields.Date('derniere date de achat')
	dernier_qty_produite = fields.Integer('derniere quantité produite')
	exigence_document_de_qualite1 = fields.Many2one('exigence_document1',string='Exigence document de quantité 1 ')
	exigence_document_de_qualite2 = fields.Many2one('exigence_document2',string='Exigence document de quantité 2 ')
	remise_client = fields.Float(string='Remise client')
	fabrication = fields.Many2many('fabrication.line' , string = 'Process fabrication')
	
class fabrication(models.Model):
	_name = 'fabrication.line'
	
	name = fields.Char('Nom')

	
class Presentation(models.Model):
	_name = "presentation"
	
	
	name = fields.Text('Présenation :')

class Couleur(models.Model):
	_name = "couleur"
	
	
	name = fields.Char('Couleur :')
	
class matiere(models.Model):
	_name = "matiere"
	
	
	name =fields.Char('Matiére')
	
	
	
class exigence_document1(models.Model):
	_name = "exigence_document1"
	
	
	name =fields.Char('Exigence document de quantité')
	
	

	
class exigence_document2(models.Model):
	_name = "exigence_document2"
	
	
	name =fields.Char('Exigence document de quantité')
	

