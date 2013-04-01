# -*- coding: utf-8 -*-
from osv import fields, osv

class crmLeadInherit(osv.osv):
    _inherit = "crm.lead"
    
    _columns = {
        'activity': fields.char("Activity", size=128),
        'company_registration_number': fields.char("Company Registration Number", size=64, help="SIREN/SIRET pour la France"),
        'company_professional_code': fields.char("Company Professional Code", size=64, help="Code NAF pour la France"),
    }
