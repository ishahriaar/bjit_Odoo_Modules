# -*- coding: utf-8 -*-
# from odoo import http


# class ProjectModule(http.Controller):
#     @http.route('/project_module/project_module/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/project_module/project_module/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('project_module.listing', {
#             'root': '/project_module/project_module',
#             'objects': http.request.env['project_module.project_module'].search([]),
#         })

#     @http.route('/project_module/project_module/objects/<model("project_module.project_module"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('project_module.object', {
#             'object': obj
#         })
