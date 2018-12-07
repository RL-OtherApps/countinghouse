# -*- coding: utf-8 -*-
from odoo import models


class ResCompany(models.Model):
    _name = 'res.company'
    _inherit = ['countinghouse.legal_id_number', 'res.company']
