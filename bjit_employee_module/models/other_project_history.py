from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
import datetime
from datetime import timedelta
from odoo.exceptions import ValidationError


class OtherProjectHistory(models.Model):
    _name = 'other.project.history'
    _description = 'Other Project History'

    other_project_id = fields.Many2one('hr.employee', string="Other Project")
    project_id = fields.Many2one('bjit.project', string="Project")
    project_role_id = fields.Many2one('bjit.role', string="Role")
    responsibility = fields.Char(string="Responsibility", related="project_role_id.role_respon", readonly=False)
    technology_id = fields.Many2one('bjit.technology', string="Technology")
    bjit_process = fields.Many2one('bjit.process', string="Process")

    date_from = fields.Date(string="From")
    date_to = fields.Date(string="To")
    date_duration = fields.Char(string='Duration', compute="_compute_duration")
    no_of_member = fields.Integer(string="No. of Members")

    @api.depends("date_from", "date_to")
    def _compute_duration(self):
        for record in self:
            date_from = record.date_from
            date_to = record.date_to
            duration_diff = relativedelta(date_to, date_from)
            months_diff_cal = str(duration_diff.months)
            years_diff_cal = str(duration_diff.years)
            record.date_duration = years_diff_cal + "Y" + " " + months_diff_cal + "M"

    @api.constrains('date_to')
    def _check_end_date(self):
        if self.date_to < self.date_from:
            raise ValidationError('From Date Should Be Less Than To Date!')


class BjitProject(models.Model):
    _name = 'bjit.project'
    _description = 'Project'
    _rec_name = 'project_name'

    project_name = fields.Char(string="Project")


class BjitRole(models.Model):
    _name = 'bjit.role'
    _description = 'Role'
    _rec_name = 'project_role'

    project_role = fields.Char(string="Job Title")
    role_respon = fields.Char(string="Responsibility")


class BjitResponsibility(models.Model):
    _name = 'bjit.responsibility'
    _description = 'Responsibility'

    role_responsibility = fields.Char(string="Responsibility")


class BjitTechnology(models.Model):
    _name = 'bjit.technology'
    _description = 'Technology'
    _rec_name = "bjit_technology"

    bjit_technology = fields.Char(string="Technology Name")
    tech_des = fields.Char(string="Description")


class BjitProcess(models.Model):
    _name = 'bjit.process'
    _description = 'Process'
    _rec_name = 'bjit_process'

    bjit_process = fields.Char(string="Process")
