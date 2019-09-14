# -*- coding: utf-8 -*-

from openerp import models, fields, api

class SalaryTax(models.Model):
    _inherit = 'hr.salary.rule'

    taxable = fields.Boolean(string="Under Tax", )
    currency_id = fields.Many2one('res.currency', string='Currency', required=False,
                                  default=lambda self: self.env.user.company_id.currency_id, track_visibility='always')

    _sql_constraints = [('sequence_unique', 'unique(sequence)', 'This sequence is already exist')]





