# -*- coding: utf-8 -*-
# from odoo import http


# class CustomProject(http.Controller):
#     @http.route('/custom_project/custom_project/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_project/custom_project/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_project.listing', {
#             'root': '/custom_project/custom_project',
#             'objects': http.request.env['custom_project.custom_project'].search([]),
#         })

#     @http.route('/custom_project/custom_project/objects/<model("custom_project.custom_project"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_project.object', {
#             'object': obj
#         })
