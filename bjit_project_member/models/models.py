
from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
from odoo.exceptions import ValidationError
from datetime import datetime, date


class ProjectTeam(models.Model):
    _name = "project.team"
    _description = "Project Team"

    name = fields.Char("Team", required=True)


class ProjectPhase(models.Model):
    _name = "project.phase"
    _description = "Project Phase"

    name = fields.Char("Phase", required=True)


class ProjectProcess(models.Model):
    _name = "project.process"
    _description = "Project Process"

    name = fields.Char("Process", required=True)


class ProjectMonthlyInvoice(models.Model):
    _name = "project.monthly.invoice"
    _description = "Project Monthly Invoice"

    month = fields.Date(
        string='Month', default=lambda self: fields.Datetime.now())
    invoice_status = fields.Boolean(
        string='Is Invoiced', default=lambda self: False)
    invoiced_percent = fields.Integer(
        "Invoiced Percent(%)", default=lambda self: 100)
    assign_percent = fields.Integer(
        "Assignment Percent(%)", default=lambda self: 100)
    notes = fields.Text(string="Notes")

    project_members = fields.Many2one('project.member', string='Member')


class ProjectMember(models.Model):
    _name = "project.member"
    _description = "Project Member"

    project_member_id = fields.Many2one('hr.employee', string='Member')
    project_member_role = fields.Many2one('hr.employee.type', string='Role')
    team_id = fields.Many2one('project.team', string='Team')
    manager_status = fields.Boolean(
        string='Is Manager', default=lambda self: False)

    responsibility = fields.Text()
    # assigned_from = fields.Float(compute="_value_pc", store=True)
    assigned_from = fields.Date(
        string='Assigned from', default=lambda self: fields.Datetime.now())
    assigned_to = fields.Date(string='Assigned to',
                              default=lambda self: fields.Datetime.now())

    project_phase = fields.Many2one('project.phase', string='Phase')
    project_process = fields.Many2one('project.process', string='Process')
    notes = fields.Text(string="Notes")

    monthly_invoice_id = fields.One2many(
        'project.monthly.invoice', 'project_members')

    project_ids = fields.Many2one('project.project', string='Member')

    @api.constrains('assigned_to', 'assigned_from')
    def _check_assigned_from(self):

        if self.assigned_to < self.assigned_from:

            raise ValidationError(
                "Assigned from date should be less then assigned to date")

    @api.onchange('project_member_id')
    def _onchange_price(self):
        # set auto-changing field
        self.project_member_role = self.project_member_id.employee_role
        

class ProjectTask(models.Model):
    _inherit = "project.project"

    project_member_ids = fields.One2many('project.member', 'project_ids')

    
