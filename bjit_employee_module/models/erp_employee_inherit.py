from odoo import models, fields, api


class ErpEmployeeInherit(models.Model):
    _inherit = 'hr.employee'
    _description = 'Employee'

    employee_language_line = fields.One2many('erp.employee.language', 'language_id', string="Language")
    other_project_history_line = fields.One2many('other.project.history', 'other_project_id',
                                                 string="Other Project History")
    bjit_project_history_line = fields.One2many('bjit.project.history', 'bjit_project_id',
                                                 string="BJIT Project History")
    academic_qualification_line = fields.One2many('academic.qualification', 'academic_qualification_id',
                                                  string="Academic Qualification")
    work_experience_line = fields.One2many('work.experience', 'work_experience_id',
                                           string="Work Experience")
    certification_line = fields.One2many('erp.certification', 'erp_certification_id',
                                         string="Certification")
    training_line = fields.One2many('erp.training', 'erp_training_id',
                                    string="Training")
    erp_profile = fields.Text()
    tech_skill_line = fields.One2many('tech.skill', 'tech_skill_id', string="Technical")


class ErpEmployeeLanguage(models.Model):
    _name = 'erp.employee.language'
    _description = 'Language Skill'

    employee_language = fields.Selection([('bangla', 'Bangla'),
                                          ('english', 'English'),
                                          ('japanese', 'Japanese')
                                          ], string="Language")
    language_id = fields.Many2one('hr.employee', string="Language")
    language_history_line = fields.One2many('erp.employee.language.history', 'language_history_id',
                                            string='Language History')


class ErpEmployeeLanguageHistory(models.Model):
    _name = 'erp.employee.language.history'
    _description = 'Language History'

    language_type = fields.Selection([('read', 'Read'),
                                      ('write', 'Write'),
                                      ('talk', 'Talk')])
    grade_level = fields.Selection([('a_grade', 'A'),
                                    ('b_grade', 'B'),
                                    ('c_grade', 'C'),
                                    ('d_grade', 'D')
                                    ])
    language_history_id = fields.Many2one('erp.employee.language', string="Language History")
