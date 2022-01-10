from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
import datetime
from datetime import timedelta
from odoo.exceptions import ValidationError


class ErpTraining(models.Model):
    _name = 'erp.training'
    _description = 'Training Section'

    erp_training_id = fields.Many2one('hr.employee', string="Training")
    training_org_id = fields.Many2one('training.org', string="Organization Name")
    course_name_id = fields.Many2one('training.course', string="Course Name")
    start_date = fields.Date(string="Training Start Date")
    end_date = fields.Date(string="Training End Date")
    progress = fields.Integer(string="Progress(%)")

    @api.constrains('start_date', 'end_date')
    def _check_end_date(self):
        if self.end_date < self.start_date:
            raise ValidationError('End date must be after start date!')


class TrainingOrg(models.Model):
    _name = 'training.org'
    _description = 'Training Organization'

    training_org = fields.Char(string="Organization Name")


class TrainingCourse(models.Model):
    _name = 'training.course'
    _description = 'Training Course'

    course_name = fields.Char(string="Course Name")
