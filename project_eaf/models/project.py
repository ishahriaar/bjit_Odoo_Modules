from odoo import models, fields, api


class EafProject(models.Model):
    _inherit = 'project.project'
    _description = 'Eaf View'

    inverse_eaf = fields.One2many('project.eaf', 'custom_eaf', string='Invest EAF')

    project_checklist_line = fields.One2many('erp.project.checklist', 'project_checklist_id', string="Project Closure")
    project_survey_line = fields.One2many('erp.project.survey', 'project_survey_id', string="Survey")
    project_future_benefits_line = fields.One2many('erp.project.future.benefits', 'project_future_benefit_id', string="Future Benefits")






