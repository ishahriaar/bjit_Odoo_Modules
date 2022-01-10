from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
import datetime
from datetime import timedelta


class TechSkill(models.Model):
    _name = 'tech.skill'
    _description = 'Technical Skill'

    tech_skill_id = fields.Many2one('hr.employee', string="Tech Skill")
    tech_test = fields.Char("Test")
    tech_categ_id = fields.Many2one("tech.categ", string="Category")
    tech_history_line = fields.One2many('tech.history', 'tech_hist_id', string="Technical History")


class TechCateg(models.Model):
    _name = 'tech.categ'
    _description = 'Technical Category'

    categ_name = fields.Char(string="Category")


class TechHistory(models.Model):
    _name = 'tech.history'
    _description = 'Technical History'

    tech_hist_id = fields.Many2one("tech.skill", string="Technical History")
    technology_id = fields.Many2one('bjit.technology', string="Technology")
    emp_comment = fields.Char("Employee Comment")
    yr_exper = fields.Float("Years of Experience")
    skill_level = fields.Selection([('a', 'A'),
                                    ('b', 'B'),
                                    ('c', 'C'),
                                    ('d', 'D')
                                    ], string="Skill Level")
    reviewer_cmnt = fields.Char("Reviewer Comment")
    no_project = fields.Integer("No of Project")
    target = fields.Char("Target")
    due_date = fields.Date("Due Date")
    achieve = fields.Char("Achieve")
