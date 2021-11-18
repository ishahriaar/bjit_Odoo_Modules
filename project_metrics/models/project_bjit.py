from odoo import models, fields, api
import datetime


class BjitProject(models.Model):
    _inherit = 'project.project'
    _description = 'Project'

    pro_name = fields.One2many('project.metrics', 'name', string="Project")


class ProjectMetrices(models.Model):
    
    _name = 'project.metrics'
    _description = 'Project metrices'

    actual_date = fields.Date(string="Actual Start Date")
    actual_end = fields.Date(string="Actual End Date")
    ac_effort = fields.Float(string="Actual Effort")
    plan_effort = fields.Float(string="Planned Effort")
    schedule = fields.Float(string="Schedule Deviation")
    ef_dev = fields.Float(string="Effort Deviation")
    pro = fields.Float(string="Productivity")
    size = fields.Float(string="Size")
    name = fields.Many2one('project.project', string="Milestone")
    milestone_line_ids=fields.Many2one('project.milestones',string='Milestone')

    # name_id = fields.Many2one('project.milestones')


class ProjectMilestones(models.Model):
    _name = 'project.milestones'
    _description = 'Project Metrices'
    _rec_name='milestone_field'
    


    # milestone=fields.Many2one('project.metrics',string='Project')
    milestone_field=fields.Char(string='Name')

    # line_ids=fields.One2many('project.metrics','milestone_line_ids',string='Milestone')

