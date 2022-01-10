from odoo import models, fields, api

AVAILABLE_PRIORITIES = [
    ('0', 'Normal'),
    ('1', 'Good'),
    ('2', 'Very Good'),
    ('3', 'Excellent')
]


class TransferList(models.Model):
    _name = 'transfer.list'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Transfer Details'
    _rec_name = "ref_number"

    ref_number = fields.Char(string='Reference', readonly=True, required=True, index=True, copy=False, default='New')
    
    @api.model
    def create(self, vals):
        if vals.get('ref_number', 'New') == 'New':
                vals['ref_number'] = self.env['ir.sequence'].next_by_code('transfer.list') or 'New'       

        result = super(TransferList, self).create(vals)       

        return result

    customer_name = fields.Many2one('res.users')
    # email = fields.Char(string='Email')

    # delivery_add = fields.Many2one('res.users', string='Delivery Address')
    # recv_from = fields.Many2one('res.users', string='Received From')
    op_type = fields.Selection([
        ('dv001', 'Delivery'),
        ('pur001', 'Receipts'),
        ('back01', 'Return')
    ], string='Operation Type')

    avail = fields.Date(string='Scheduled Date', default=lambda self: fields.Date.today())
    priority = fields.Selection(AVAILABLE_PRIORITIES, string='Priority', default='0')
    source_doc = fields.Char(string='Source Reference')

    product_in = fields.One2many('stock.mover', 'stock_in', string='')

    ship_policy = fields.Selection([
        ('as01', 'As soon as possible'),
        ('whe001', 'When all products are ready'),

    ], string='Shipping Policy')

    respon_guy = fields.Many2one('hr.employee', string='Responsible')

    prod_check = fields.Selection([
        ('av001', 'Quantity Available'),
        ('notav01', 'Not Available'),
        ('need', 'Need Validation'),

    ], copy=False, default='need', string='Product Availability')

    field_ck = fields.Boolean(default=False)

    state = fields.Selection([
        ('draft', 'Draft'),
        ('waiting', 'Waiting'),
        ('ready', 'Ready'),
        ('done', 'Done'),
        ('cancel', 'Cancelled')
    ], string='Status', default='draft')

    def mark_as_to(self):
        for record in self:
            if record.op_type == 'dv001':
                if record.state == 'draft':
                    record.state = 'ready'
                    record.field_ck = True
            if record.op_type == 'pur001' or record.op_type == 'back01':
                if record.state == 'draft':
                    record.state = 'ready'

    def mark_as_done(self):
        for record in self:
            if record.op_type == 'dv001':
                if record.product_in.prod_demand < record.product_in.stock_pid.on_hand or record.product_in.prod_demand == record.product_in.stock_pid.on_hand:
                    record.prod_check = 'av001'
                    record.state = 'done'
                if record.product_in.prod_demand > record.product_in.stock_pid.on_hand or record.product_in.stock_pid.on_hand == 0:
                    record.prod_check = 'notav01'
            if record.op_type == 'pur001' or record.op_type == 'back01':
                record.state = 'done'







    def mark_as_cancel(self):
        for record in self:
            if record.state == 'done':
                record.state = 'cancel'
            if record.state == 'ready':
                record.state = 'cancel'


class HrLockheed(models.Model):
    _inherit = 'hr.employee'
    _description = 'Employee Details'

    tranfer_name = fields.One2many('transfer.list', 'respon_guy', string='')











