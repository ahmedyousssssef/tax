# -*- coding: utf-8 -*-
{
    'name': "Tax Calculation",

    'summary': """
        Salary Tax Computation For Employee""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Joo",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'hr',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr_payroll','mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/hr_payslip_config_view.xml',
        'views/tax_rule_view.xml',
        'views/salary_tax_view.xml',
        'views/salary_rule_view.xml',
        'data/data_tax_view.xml',
        'data/mail_template_data.xml',
        'views/hr_payroll_view.xml',
        'views/hr_view.xml',
    ],
}
