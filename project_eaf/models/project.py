from odoo import models, fields, api


class EafProject(models.Model):
    _inherit = 'project.project'
    _description = 'Eaf View'

    inverse_eaf = fields.One2many('project.eaf', 'custom_eaf', string='Invest EAF')







