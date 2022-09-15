{
    'name': 'Theme Training Simon',
    'version': '1.0',
    'summary': 'Training Theme to get used to Odoo Theme Development',
    'description': 'Training Theme to get used to Odoo Theme Development',
    'category': 'Theme',
    'author': 'Auguria',
    'sequence': 3,
    'company': 'Auguria',
    'maintainer': 'Auguria',
    'depends': ['base', 'website'],
    'data': [
        'views/page.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            '/custom-addons/theme_original/static/css/odoo_theme.css',
        ],
    },
    'application': True,
    'license': 'LGPL Version 3',
}