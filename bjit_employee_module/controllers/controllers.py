# -*- coding: utf-8 -*-
# from odoo import http


# class ErpEmployee(http.Controller):
#     @http.route('/erp_employee/erp_employee/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/erp_employee/erp_employee/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('erp_employee.listing', {
#             'root': '/erp_employee/erp_employee',
#             'objects': http.request.env['erp_employee.erp_employee'].search([]),
#         })

#     @http.route('/erp_employee/erp_employee/objects/<model("erp_employee.erp_employee"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('erp_employee.object', {
#             'object': obj
#         })
