from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
import datetime
from datetime import timedelta
from odoo.exceptions import ValidationError


class ErpCertification(models.Model):
    _name = 'erp.certification'
    _description = 'Certification Section'

    erp_certification_id = fields.Many2one('hr.employee', string="Certification")
    cert_name_id = fields.Many2one('certification', string="Certification")
    issued_by_id = fields.Many2one('cert.issued', string="Issued By")
    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")
    cert_status = fields.Selection([('complete', 'Complete'),
                                    ('in_progress', 'In Progress'),
                                    ('certified', 'Certified')
                                    ], string="Status")
    cert_image = fields.Image("Upload")

    @api.constrains('start_date', 'end_date')
    def _check_end_date(self):
        if self.end_date < self.start_date:
            raise ValidationError('End date must be after start date!')


class CertificationName(models.Model):
    _name = 'certification'
    _description = 'Certification Name'

    cert_name = fields.Char(string="Certification")


class IssuedBy(models.Model):
    _name = 'cert.issued'
    _description = 'Issued By'

    issued_by = fields.Char(string="Issued By")
