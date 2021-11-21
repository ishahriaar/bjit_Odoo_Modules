# -*- coding: utf-8 -*-
# from odoo import http


# class BjitSetting(http.Controller):
#     @http.route('/bjit_setting/bjit_setting/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bjit_setting/bjit_setting/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('bjit_setting.listing', {
#             'root': '/bjit_setting/bjit_setting',
#             'objects': http.request.env['bjit_setting.bjit_setting'].search([]),
#         })

#     @http.route('/bjit_setting/bjit_setting/objects/<model("bjit_setting.bjit_setting"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bjit_setting.object', {
#             'object': obj
#         })
