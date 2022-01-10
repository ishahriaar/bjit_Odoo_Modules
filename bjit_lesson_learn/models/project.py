from odoo import models, fields


class ProjectInherit(models.Model):
    _inherit = 'project.project'
    _description = 'project_task'

    lesson = fields.One2many('lesson.project', 'project', string="name")
