
from odoo import api, fields, models, _


class EmployeeType(models.Model):
    _name = "hr.employee.type"
    _description = "HR Employee Type"

    name = fields.Char(string='Job Title')
    responsibility = fields.Char(string='Responsibility')


class EmployeeType(models.Model):
    _name = "employee.tag"
    _description = "HR Employee Type"

    name = fields.Char(string='Tags')


class EmployeeViewEdit(models.Model):
    _inherit = 'hr.employee'

    skype_id = fields.Char(string='Skype')
    job_position = fields.Char(string='Job Position')
    platform = fields.Many2many('employee.tag', string='Platform')

    employee_role = fields.Many2one('hr.employee.type', string='Employee Type')
    
    
