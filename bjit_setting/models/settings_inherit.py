from odoo import models, fields, api


class InheritProjectSetting(models.TransientModel):
    _inherit = 'res.config.settings'
    _description = 'Project Setting'

    project_id_prefix = fields.Char("Prefix", config_parameter='erp_project.project_id_prefix')
    project_id_suffix = fields.Char("Suffix", config_parameter='erp_project.project_id_suffix')

