from odoo import models, fields, api


class MyProject(models.Model):
    _inherit = 'project.project'
    _description = 'Property Details'

    custom_module = fields.One2many('project.module', 'owner_module')

    custom_cat = fields.One2many('project.tech', 'owner_category')




