from odoo import models, fields, api


class ProjectEaf(models.Model):
    _name = "project.eaf"
    _description = "Project EAF"
    _rec_name = "attr_name"

    attr_name = fields.Many2one('pro.attr', string="Attributes", required=True)

    details_table = fields.One2many('attr.cat', 'all_details')

    custom_eaf = fields.Many2one('project.project')


class AttrCat(models.Model):
    _name = "attr.cat"
    _description = "Attribute Criteria Value"

    name = fields.Many2one('new.cat', string="Attribute Criteria", required=True)
    very_low = fields.Float(string="Very Low")
    low = fields.Float(string="Low")
    normal = fields.Float(string="Normal")
    high = fields.Float(string="High")
    very_high = fields.Float(string="Very High")
    extra_high = fields.Float(string="Extra High")

    all_details = fields.Many2one('project.eaf')


class NewName(models.Model):
    _name = "pro.attr"
    _description = "Attribute Name"

    name = fields.Char(string='Name')


class NewCat(models.Model):
    _name = "new.cat"
    _description = "Attributes Criteria"

    name = fields.Char(string='Name')



