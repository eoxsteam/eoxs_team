# coding: utf-8

from odoo import api, fields, models


class res_partner(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    sources = fields.Char(string='Sources', index=True)
    revenue_range = fields.Char(string='Revenue Range', index=True)
    sic_codes = fields.Char(string='Sic Codes', index=True)
    buckets = fields.Char(string='Buckets', index=True)
    personas = fields.Char(string='Personas', index=True)


