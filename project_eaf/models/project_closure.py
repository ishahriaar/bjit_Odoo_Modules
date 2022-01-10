from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
import datetime
from datetime import timedelta
from odoo.exceptions import ValidationError


class ErpProjectChecklist(models.Model):
    _name = 'erp.project.checklist'
    _description = 'Project Checklist'

    project_checklist_id = fields.Many2one('project.project', string="Project Closure")
    checklist_name = fields.Char("Checklist")
    yes_no = fields.Boolean("Yes/No")
    comments = fields.Text("Comments")


class ErpProjectSurvey(models.Model):
    _name = 'erp.project.survey'
    _description = 'Project Survey'

    project_survey_id = fields.Many2one('project.project', string="Project Survey")
    survey_name = fields.Char("Survey")
    answer = fields.Text()
    comments = fields.Text("Comments")


class ErpFutureBenefits(models.Model):
    _name = 'erp.project.future.benefits'
    _description = 'Future Benefits Realization'

    project_future_benefit_id = fields.Many2one('project.project', string="Future Benefits Realization")
    benefit = fields.Char("Benefit")
    measured = fields.Text("How will this be measured?")
    ownership = fields.Text("Who will take ownership?")
    realized = fields.Text("Who will take ownership?")
