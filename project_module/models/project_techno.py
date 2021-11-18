from odoo import models, fields, api


class AllTech(models.Model):
    _name = 'project.tech'
    _description = 'Technology Details'

    tech_cat = fields.Many2one('tech.category', string='Category')

    tech_value = fields.Many2one('tech.add', string='Technology')

    tech_desc = fields.Text(string='Description')

    owner_category = fields.Many2one('project.project', string='')


class AddCat(models.Model):
    _name = 'tech.category'
    _description = 'Technology Category'

    name = fields.Char()




