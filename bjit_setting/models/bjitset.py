from odoo import models, fields, api


class BjitSetting(models.Model):
    _inherit = 'project.project'
    _description = 'Inherited Project Details'

    project_id = fields.Char(string='Project ID', required=True, readonly=True, index=True, copy=False, default='new')

    @api.model
    def create(self, vals):
        if vals.get('project_id', 'new') == 'new':
            vals['project_id'] = self.env['ir.sequence'].next_by_code('project.id.serial') or 'new'
        pre_new = self.env['res.config.settings'].search([])[-1].project_id_prefix
        suff_new = self.env['res.config.settings'].search([])[-1].project_id_suffix
        print(pre_new)
        vals['project_id'] = str(pre_new) + str(vals['project_id']) + str(suff_new)

        result = super(BjitSetting, self).create(vals)

        return result
    pro_status = fields.Selection([('option1', 'In Progress'),
                                   ('option2', 'Completed'), ('option3', 'Suspended'),
                                   ('option4', 'Other')], string='Project status')
    dept = fields.Many2one('hr.department', string="Department")
    pro_manager = fields.Many2one('hr.employee', string="Project Manager")
    sqa_manager = fields.Many2one('hr.employee', string="SQA Manager")
    customer = fields.Many2one('res.partner', string="Customer")
    pro_owner = fields.Many2one('res.partner', string="Project Owner")
    link = fields.Char(string='Redmine Link')
    gerrit_link = fields.Char(string='Gerrit Link')
    des = fields.Text(string='Description')
    pro_type = fields.Selection([('option1', 'Small size & easy'),
                                   ('option2', 'Mid Size & Average'),
                                   ('option3', 'Large size & High Complexity')], string='Project Type')
    eas_effort = fields.Float(string='Estimated Effort(MM)')
    actual_effort = fields.Float(string='Actual Effort(MM)')
    invoice_effort = fields.Float(string='Invoiced Effort(MM)')
    cocomo_effort = fields.Float(string='COCOMO Effort(MM)')


class BjitInherit(models.Model):
    _inherit = 'hr.employee'
    _description = 'Inherited Employee Details'




class ResPartner(models.Model):
    _inherit = 'res.partner'
    _description = 'Inherited Partner Details'






