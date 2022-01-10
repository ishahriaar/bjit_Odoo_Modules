from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
import datetime
from datetime import timedelta
from odoo.exceptions import ValidationError


class WorkExperience(models.Model):
    _name = 'work.experience'
    _description = 'Work Experience'

    work_experience_id = fields.Many2one('hr.employee', string="Work Experience")
    bjit_role_id = fields.Many2one('bjit.role', string="Role")
    responsibility = fields.Char(string="Responsibility")
    organization_id = fields.Many2one('work.organization', string="Organization")
    technology_id = fields.Many2one('bjit.technology', string="Technology")

    date_from = fields.Date(string="From")
    date_to = fields.Date(string="To")
    date_duration = fields.Char(string='Duration', compute="_compute_duration")

    @api.constrains('date_to')
    def _check_end_date(self):
        if self.date_to < self.date_from:
            raise ValidationError('From Date Should Be Less Than To Date!')

    @api.depends("date_from", "date_to")
    def _compute_duration(self):
        for record in self:
            date_from = record.date_from
            date_to = record.date_to
            duration_diff = relativedelta(date_to, date_from)
            months_diff_cal = str(duration_diff.months)
            years_diff_cal = str(duration_diff.years)
            record.date_duration = years_diff_cal + "Y" + " " + months_diff_cal + "M"


class WorkOrganization(models.Model):
    _name = 'work.organization'
    _description = 'Organization'

    organization = fields.Char(string="Organization")
