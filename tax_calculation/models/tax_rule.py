# -*- coding: utf-8 -*-
from __future__ import division
from math import floor,ceil
from openerp import api, fields, models,_


class NewModule(models.Model):
    _name = 'salary.tax.rule'
    _rec_name = 'name'
    _order='level'
    _description = 'New Tax Rule'

    name = fields.Char(string= 'Level',translate=True)
    level = fields.Selection(string="Level",
                             selection=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'),('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'),],default='1', required=True, )
    amount_from = fields.Float('From')
    amount_to = fields.Float('To')
    tax_rate = fields.Float('Tax Rate (%)')
    tax_exemption = fields.Float('Tax Exemption (%)')
    total_tax = fields.Float('Total Tax',compute='_compute_tax_amount')
    total_discount = fields.Float('Total Discount' ,compute='_compute_discount_amount')
    counter = fields.Integer(string="counter",compute='_compute_tax_counter')

    @api.one
    def _compute_tax_counter(self):
        records = self.search([])
        self.counter = len(records)



    def normal_round(self,n):
        if n - floor(n) < 0.5:
            return floor(n)
        elif n - floor(n) == 0.5:
            return n
        else:
            return ceil(n)

    @api.one
    def _compute_tax_amount(self):
        if not self.level == str(self.counter):
            total_tax =((self.amount_to - self.amount_from) * (self.tax_rate / 100))
            self.total_tax = self.normal_round(total_tax)

    @api.one
    def _compute_discount_amount(self):
        total_discount = ((self.total_tax) * (self.tax_exemption / 100))
        self.total_discount = self.normal_round(total_discount)



    _sql_constraints = [
        ('level_uniq', 'UNIQUE (level)', 'You can not have two rule with the same Level !')
    ]


