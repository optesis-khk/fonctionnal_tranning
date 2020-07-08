{
    'name': 'Optimo Account Asset',
    'author': 'OPTESIS SA',
    'version': '1.0.0',
    'category': 'Asset',
    'description': """
Ce module permet de faire l'inventaire des immobilisations de votre entreprise d'une manière structurée, fiable et intuitive
""",
    'summary': 'Module d\'inventaire ',
    'sequence': 9,
    'depends': ['base','account_asset','product', 'account',
    ],
    'data': [
      'security/security.xml',
      'security/ir.model.access.csv',
      'views/optesis_views.xml',
      'views/employee.xml',
      'views/site.xml',
      'views/direction.xml',
      'views/document.xml',
      'views/optesis.xml',
      'views/transfert.xml',
      'security/multi_company_view.xml',
      'views/sequence_control.xml',
      'views/sequence_transfert.xml',

    ],
    'test': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
