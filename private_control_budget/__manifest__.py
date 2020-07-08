{
    'name': 'Control Budget For Private',
    'author': 'OPTESIS SA',
    'version': '1.4.0',
    'category': 'Tools',
    'description': """
Ce module permet de faire le control budgetairepour le secteur privé
""",
    'summary': 'Comptabilite',
    'sequence': 9,
    'depends': ['base','account','account_reports','analytic','account_budget','purchase','report_xlsx'],
    'data': [
        'data/approve_mail_template.xml',
        'data/refuse_mail_template.xml',
        'security/ir.model.access.csv',
        'security/purchase_security.xml',
        'reports/reports.xml',
        'views/account_budget_view.xml',
        'views/account_analytic_account_view.xml',
        'views/purchase_view.xml',
        'views/account_invoice_view.xml',
        'views/account_move_view.xml',
        'views/res_company_view.xml',
    ],
    'test': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
