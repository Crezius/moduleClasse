# -*- coding: utf-8 -*-
{
    'name': "Lycée",

    'summary': """
        Juste un truc d'emploi du temps""",

    'description': """
        Long description of module's purpose
    """,

    'author': "moi",
    'website': "http://www.team-dsi.fr",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views/cours.xml',
        'views/classe.xml',
        'views/professeur.xml',
        'views/etudiant.xml',
        'views/menu.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}