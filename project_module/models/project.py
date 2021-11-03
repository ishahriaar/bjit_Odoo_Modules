from odoo import models, fields, api


class MyProject(models.Model):
    _inherit = 'project.task'
    _description = 'Property Details'

    custom_module = fields.One2many('project.module', 'owner_module')




