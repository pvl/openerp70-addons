# -*- coding: utf-8 -*-
{
    'name': "CRM Plus",
    'version': "1.0",
    'author': "EL2DE SARL",
    'category': "CRM",
    'summary': 'CRM, More',
    'description': """
Add CRM functionnalities for OpenERP 7.0 (developped by David DRAPEAU <david.drapeau@el2de.com.com>)
    """,
    
    'website': 'https://github.com/ddrapeau/openerp70-addons',
    'images': [],
    'depends': [
        'crm',
    ],
    'data': [
        "view/crm_lead_view.xml",
    ],
    'css': [],
    'demo': [],
    'test': [],
    'application': False,
    'installable': True,
    'auto_install': False,
    'web': True,
    #'certificate': '',
}
