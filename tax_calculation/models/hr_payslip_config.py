# -*- coding: utf-8 -*-

from openerp import models, fields, api


class HrPayslipConfig(models.TransientModel):
    _inherit = 'hr.payroll.config.settings'

    payslip_tax_type = fields.Selection(string="Tax Type", help="Compute Tax For Employee On Payslip",
                                selection=[ ('annual', 'Annually'), ('month', 'Monthly'),], required=False,
                                default='month')

    @api.multi
    def set_payslip_defaults(self):
        return self.env['ir.values'].sudo().set_default(
            'hr.payroll.config.settings', 'payslip_tax_type', self.payslip_tax_type)
