# -*- coding: utf-8 -*-

from openerp import models, fields, api, exceptions

class HR(models.Model):
    _inherit = 'hr.employee'

    is_warning = fields.Boolean(string="Salary Hold")