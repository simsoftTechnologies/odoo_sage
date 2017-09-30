# -*- coding: utf-8 -*-
from openerp import http

# class StructureCommercialSimsoft(http.Controller):
#     @http.route('/structure_commercial_simsoft/structure_commercial_simsoft/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/structure_commercial_simsoft/structure_commercial_simsoft/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('structure_commercial_simsoft.listing', {
#             'root': '/structure_commercial_simsoft/structure_commercial_simsoft',
#             'objects': http.request.env['structure_commercial_simsoft.structure_commercial_simsoft'].search([]),
#         })

#     @http.route('/structure_commercial_simsoft/structure_commercial_simsoft/objects/<model("structure_commercial_simsoft.structure_commercial_simsoft"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('structure_commercial_simsoft.object', {
#             'object': obj
#         })