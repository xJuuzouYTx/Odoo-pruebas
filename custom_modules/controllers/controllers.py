# -*- coding: utf-8 -*-
# from odoo import http


# class CustomModules(http.Controller):
#     @http.route('/custom_modules/custom_modules', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_modules/custom_modules/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_modules.listing', {
#             'root': '/custom_modules/custom_modules',
#             'objects': http.request.env['custom_modules.custom_modules'].search([]),
#         })

#     @http.route('/custom_modules/custom_modules/objects/<model("custom_modules.custom_modules"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_modules.object', {
#             'object': obj
#         })
