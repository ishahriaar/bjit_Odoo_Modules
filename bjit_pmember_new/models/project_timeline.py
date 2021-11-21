# -*- coding: utf-8 -*-

from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
from odoo.exceptions import ValidationError
from datetime import datetime, date


class ProjectTimeLine(models.Model):
    _inherit = "project.project"

    last_modified_on = fields.Datetime(
        string="Last Modified on", default=lambda self: fields.Datetime.now())
    created_on = fields.Datetime(
        string="Created on", default=lambda self: fields.Datetime.now())
    start_date = fields.Date(
        string='Start Date', default=lambda self: fields.Datetime.now())
    project_closure_date = fields.Date(
        string='Project Close Date', default=lambda self: fields.Datetime.now())

    @api.onchange('created_on', 'start_date', 'project_closure_date')
    def _change_last_modified(self):
        # set auto-changing field
        self.last_modified_on = datetime.now()

    @api.constrains('start_date', 'project_closure_date')
    def _check_project_closure_date(self):

        if self.project_closure_date < self.start_date:

            raise ValidationError(
                "In project timeline tab Project Closure date must be greater than Project Start date")
