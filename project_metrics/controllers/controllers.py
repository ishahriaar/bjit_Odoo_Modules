# -*- coding: utf-8 -*-
# from odoo import http


# class BjitProject(http.Controller):
#     @http.route('/bjit_project/bjit_project/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bjit_project/bjit_project/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('bjit_project.listing', {
#             'root': '/bjit_project/bjit_project',
#             'objects': http.request.env['bjit_project.bjit_project'].search([]),
#         })

#     @http.route('/bjit_project/bjit_project/objects/<model("bjit_project.bjit_project"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bjit_project.object', {
#             'object': obj
#         })
