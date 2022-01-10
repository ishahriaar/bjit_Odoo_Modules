from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
import datetime
from datetime import timedelta
from odoo.exceptions import ValidationError


class BjitProjectHistory(models.Model):
    _name = 'bjit.project.history'
    _description = 'BJIT Project History'

    bjit_project_id = fields.Many2one('hr.employee', string="Bjit Project")
    project_id = fields.Many2one('bjit.project', string="Project")
    project_role_id = fields.Many2one('bjit.role', string="Role")
    responsibility = fields.Char(string="Responsibility", related="project_role_id.role_respon")
    # responsibility = fields.Char(string="Responsibility")
    invoice = fields.Char(string='Invoice')
    bjit_process = fields.Many2one('bjit.process', string="Process")

    assigned_from = fields.Date(string="Assigned From")
    assigned_to = fields.Date(string="Assigned To")
    notes = fields.Char(string='Notes')
    no_of_member = fields.Integer(string="No. of Members")

    @api.constrains('assigned_from', 'assigned_to')
    def _check_end_date(self):
        if self.assigned_to < self.assigned_from:
            raise ValidationError('Assigned From Date Should Be Less Than Assigned To Date!')
