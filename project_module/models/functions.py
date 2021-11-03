from odoo import models, fields, api


class FunData(models.Model):
    _name = 'function.name'
    _description = 'functions details'
    _rec_name = 'function_name'

    function_name = fields.Many2one('function.add')
    fun_effort = fields.Float(string='Estimated Effort')
    fun_ac = fields.Float(string='Actual Effort')

    module_in = fields.Many2one('project.module', string='')


class FunAdd(models.Model):
    _name = 'function.add'
    _description = ''

    name = fields.Char(string='')

