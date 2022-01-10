from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
import datetime
from datetime import timedelta
from odoo.exceptions import ValidationError


class AcademicQualification(models.Model):
    _name = 'academic.qualification'
    _description = 'Academic Qualification'

    academic_qualification_id = fields.Many2one('hr.employee', string="Academic Qualification")
    aca_degree_id = fields.Many2one('aca.degree', string="Degree")
    aca_institute_id = fields.Many2one('aca.institute', string="Academic Institute")
    aca_major_id = fields.Many2one('aca.major', string="Major")

    start_date = fields.Date()
    end_date = fields.Date()
    duration = fields.Float()

    @api.constrains('start_date', 'end_date')
    def _check_end_date(self):
        if self.end_date < self.start_date:
            raise ValidationError('End date must be after start date!')


class AcaDegree(models.Model):
    _name = 'aca.degree'
    _description = 'Degree'
    _rec_name = 'aca_degree'

    aca_degree = fields.Char(string="Degree")


class AcaInstitute(models.Model):
    _name = 'aca.institute'
    _description = 'Academic Institute'
    _rec_name = 'aca_institute'

    aca_institute = fields.Char(string="Academic Institute")


class AcaMajor(models.Model):
    _name = 'aca.major'
    _description = 'Major'
    _rec_name = 'aca_major'

    aca_major = fields.Char(string="Major")
