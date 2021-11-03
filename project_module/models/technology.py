from odoo import models, fields, api


class AllTech(models.Model):
    _name = 'technology.name'
    _description = 'Technology Details'

    name = fields.Many2one('tech.add', string='Technology/Language')

    source_code_line = fields.Integer(string='Source Code Line')
    comment_line = fields.Integer(string='Comment Line')
    blank_line = fields.Integer(string='Blank Line')
    module_info = fields.Many2one('project.module')

    total_line = fields.Integer(string='Total Line of Code', compute="_count_line", store=True)

    @api.depends('source_code_line', 'comment_line', 'blank_line')
    def _count_line(self):
        for rec in self:
            if rec.comment_line != 0 and rec.blank_line != 0:
                rec.total_line = rec.source_code_line + rec.blank_line + rec.comment_line
            if rec.comment_line == 0 and rec.blank_line == 0:
                rec.total_line = rec.source_code_line
            if rec.comment_line != 0 and rec.blank_line == 0:
                rec.total_line = rec.source_code_line + rec.comment_line
            if rec.comment_line == 0 and rec.blank_line != 0:
                rec.total_line = rec.source_code_line + rec.blank_line

    source_code_per = fields.Float(string='Source Code Line %')
    comment_lin_per = fields.Float(string='Comment Line %')
    blank_line_per = fields.Float(string='Blank Line %')

    @api.onchange('total_line')
    def calculate_per(self):

        for record in self:

            if record.comment_line != 0 and record.blank_line != 0:

                total_code = record.source_code_line + record.blank_line + record.comment_line
                record.source_code_per = (record.source_code_line*100)/total_code
                record.comment_lin_per = (record.comment_line*100)/total_code
                record.blank_line_per = (record.blank_line * 100) / total_code

            if record.comment_line == 0 and record.blank_line == 0:

                total_code1 = record.source_code_line
                record.source_code_per = total_code1
                record.comment_lin_per = 0.00
                record.blank_line_per = 0.00

            if record.comment_line != 0 and record.blank_line == 0:

                total_code2 = record.source_code_line + record.comment_line
                record.source_code_per = (record.source_code_line*100)/total_code2
                record.comment_lin_per = (record.comment_line*100)/total_code2
                record.blank_line_per = 0.00

            if record.comment_line == 0 and record.blank_line != 0:

                total_code3 = record.source_code_line + record.blank_line
                record.source_code_per = (record.source_code_line*100)/total_code3
                record.comment_lin_per = 0.00
                record.blank_line_per = (record.blank_line * 100) / total_code3


class AddTechName(models.Model):
    _name = 'tech.add'
    _description = 'Technology Stack'

    name = fields.Char()




