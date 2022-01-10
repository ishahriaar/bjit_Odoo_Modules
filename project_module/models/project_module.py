from odoo import models, fields,api
from odoo.exceptions import ValidationError
from datetime import date, timedelta


class ProjectData(models.Model):
    _name = 'project.module'
    _description = 'modules details'
    _rec_name = 'module_name'

    module_name = fields.Many2one('module.name', string='Module', required=True)
    estimate_effort = fields.Float(string='Estimated Effort', default=0.00)
    actual_effort = fields.Float(string='Actual Effort', default=0.00)


    # Inherited Class For Pages

    function_in = fields.One2many('function.name', 'module_in', string='')
    tech_in = fields.One2many('technology.name', 'module_info', string='')

    owner_module = fields.Many2one('project.project', string='')


class ModuleName(models.Model):
    _name = 'module.name'
    _description = ''

    name = fields.Char(string='Module')
    sequence = fields.Integer(
        "Sequence", default=10,
        help="Gives the sequence order when displaying a list of stages.")

    # project_info = fields.One2many('project.module', 'module_name')
