# -*- coding: utf-8 -*-
# from odoo import http


# class Coperativa(http.Controller):
#     @http.route('/coperativa/coperativa/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/coperativa/coperativa/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('coperativa.listing', {
#             'root': '/coperativa/coperativa',
#             'objects': http.request.env['coperativa.coperativa'].search([]),
#         })

#     @http.route('/coperativa/coperativa/objects/<model("coperativa.coperativa"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('coperativa.object', {
#             'object': obj
#         })
