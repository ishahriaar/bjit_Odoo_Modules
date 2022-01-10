from odoo import models, fields


class LessonLearned(models.Model):
    _name = 'lesson.project'
    _description = 'project_project'

    # task=fields.Char(string="Name of Task")
    # conf=fields.Boolean(string="Confidential Project")
    mile = fields.Many2one('bjit.mstone', string="Milestone")
    project = fields.Many2one('project.project', string="Name")
    des1 = fields.Text(string='Description')
    fos = fields.Char(string='Factors of Success')
    des2 = fields.Text(string='Description')
    cause = fields.Char(string='Cause & Impact')
    des3 = fields.Text(string='Description')
    mit = fields.Char(string='Possible Mitigation')


class ProMile(models.Model):
    _name = 'bjit.mstone'
    _description = 'project_milestone'
    _rec_name = 'name'

    name = fields.Char(string="Name")
