# -*- coding: utf-8 -*-
from osv import fields, osv

class crmLeadInherit(osv.osv):
    _inherit = "crm.lead"
    
    _columns = {
        'activity': fields.char("Activity", size=128),
        'company_registration_number': fields.char("Company Registration Number", size=64),
    }