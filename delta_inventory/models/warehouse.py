from odoo import models, fields, api
from odoo import api
from odoo.exceptions import ValidationError
import re


class WarehouseList(models.Model):
    _name = 'warehouse.list'

    _description = 'WareHouse Details'
    _rec_name = 'wname'

    wname = fields.Char(string='Warehouse Name', required=True)

    _sql_constraints = [
        ('unique_name', 'UNIQUE(wname)', 'Name already exists!')
    ]

    wtype = fields.Selection([
        ('private', 'Private'),
        ('open', 'Open')
    ], string='Warehouse Type')

    wlocation = fields.Selection([
        ('usa', 'Nevada'),
        ('dhaka', 'Dhaka'),
        ('sweden1', 'Helsingborg'),
        ('belgium', 'Ramillies'),
        ('germany', 'Berlin'),
        ('sweden', 'Stockholm'),
        ('usa1', 'Seattle')

     ], string='Location', required=True)

    wphone = fields.Char(string='Phone')
    email = fields.Char(string='Email Address')

    @api.constrains('email')
    def validate_mail(self):
        if self.email:
            match = re.match('^[_a-z]+[0-9-]*(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', self.email)
            if match is None:
                raise ValidationError('Not a valid E-mail')

    wmanage = fields.Many2one('hr.employee', string='Manager')
    related_product = fields.One2many('product.list', 'warehouse')



