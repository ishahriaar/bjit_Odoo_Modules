from odoo import models, fields, api


class ProductList(models.Model):
    _name = 'product.list'
    _description = 'Product Details'
    _rec_name = "prod_name"

    sequence = fields.Integer(default=10)

    prod_name = fields.Char(string='Product Name', required=False)

    _sql_constraints = [
        ('unique_name', 'UNIQUE(prod_name)', 'Name already exists!')
    ]

    avail_from = fields.Date(string='Available From')
    description = fields.Char(string='Description')

    sale_price = fields.Float(
        'Price', default=1.0, required=True,
        help="Price at which the product is sold to customers.")

    prod_cost = fields.Float('Cost')

    # @api.depends('prod_cost', 'country')
    # def _total_cost(self):
    #
    #     for prod in self:
    #         # product = self.env['product.list'].search([('id', '=', prod.id)])
    #
    #         if prod.country == 'option1':
    #             prod.sale_price = (prod.prod_cost + (prod.prod_cost * 0.5))
    #         if prod.country == 'option2':
    #             prod.sale_price = (prod.prod_cost + (prod.prod_cost * 0.1))
    #         if prod.country == 'option3':
    #             prod.sale_price = (prod.prod_cost + (prod.prod_cost * 0.7))

    cus_sold = fields.Boolean(string='Can be Sold')
    # cus_purchase = fields.Boolean(string='Can be Purchased')
    product_image = fields.Image(string="Upload", max_width=100, max_height=100, verify_resolution=False)
    # status = fields.Selection([
    #     ('available', 'Available'),
    #     ('unavailable', 'Unavailable')
    #
    # ], required=True)
    country = fields.Selection([('option1', 'Bangladesh'), ('option2', 'United States'), ('option3', 'Canada')],
                               string='Country')

    stock_into = fields.One2many('stock.mover', 'stock_pid', string='')
    # currency_id = fields.Many2one(
    #     'res.currency', 'Currency', compute='_compute_currency_id')
    # cost_currency_id = fields.Many2one(
    #     'res.currency', 'Cost Currency', compute='_compute_cost_currency_id')
    #
    # company_id = fields.Many2one(
    #     'res.company', 'Company', index=1)

    # def update_status(self):
    #     for record in self:
    #         if record.status == 'available':
    #             record.status = 'unavailable'
    #         elif record.status == 'unavailable':
    #             record.status = 'available'


    stage_update = fields.Many2one('product.status', string="Stock Status", group_expand='_read_group_stage_ids')


    # def name_get(self):
    #     stage_list = []
    #     for rec in self.stage_update:
    #
    #         print(rec[0])
    #         print("*******\n\n\n\n")

    on_hand = fields.Integer(string='On Hand')

    warehouse = fields.Many2one('warehouse.list', string='Related Warehouse')

    @api.model
    def _read_group_stage_ids(self, stages, domain, order):
        stage_ids = self.env['product.status'].search([])
        return stage_ids

    # @api.depends_context('company')
    # def _compute_cost_currency_id(self):
    #     self.cost_currency_id = self.env.company.currency_id.id
    #
    # @api.depends('company_id')
    # def _compute_currency_id(self):
    #     main_company = self.env['res.company']._get_main_company()
    #     for template in self:
    #         template.currency_id = template.company_id.sudo().currency_id.id or main_company.currency_id.id


class ProductStatus(models.Model):
    _name = "product.status"
    _description = "Product Status"
    _order = 'sequence'

    name = fields.Char("Stage Name", required=True, translate=True)
    sequence = fields.Integer(
        "Sequence", default=10,
        help="Gives the sequence order when displaying a list of stages.")
    # color_pick = fields.Integer(string='Color')



