from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale


class WebProduct(http.Controller):

    # @http.route('/warehouse_form', type="http", auth="user", website=True)
    # def product_webform(self, **kw):
    #     print("Execution Here.........................")
    #     # return http.request.render('mini_project_01.create_warehouse', {'name': 'Mohakhali101'})
    #
    #     teachers = request.env['warehouse.list'].sudo().search([])
    #
    #     return http.request.render('mini_project_01.create_warehouse', {
    #         'teachers': teachers
    #     })
    #
    # @http.route('/create/warehouse', type="http", auth="user", website=True)
    # def create_webproduct(self, **kw):
    #     print("Data Received.....", kw)
    #     request.env['product.list'].sudo().create(kw)
    #     return request.render("mini_project_01.lockheed_thanks", {})


    #product view

    @http.route('/product_view', website=True, auth='public')
    def product_view(self, **kw):
        products = request.env['product.list'].sudo().search([])
        return request.render("i_inventory.product_page", {
            'product': products
        })

    @http.route('/form_product', type='http', auth='public')
    def form_product(self):
        print("Yes here entered")
        exams_rec = request.env['product.list'].search([])
        products = []
        for rec in exams_rec:
            vals = {
                'name': rec.name,
            }
            products.append(vals)
        print("Product List--->", products)
        data = {'status': 200, 'response': products, 'message': 'Final Exam is Over'}
        return data
