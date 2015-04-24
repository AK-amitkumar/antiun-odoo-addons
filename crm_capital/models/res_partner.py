# -*- encoding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __openerp__.py file in root directory
##############################################################################
from openerp import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    capital_country = fields.Many2one(
        'res.country', string="Capital country",
        help="Country of origin of the capital of this company")
    capital_registered = fields.Integer(string="Capital registered")
    turnover_range = fields.Many2one(comodel_name='crm.turnover_range')
    turnover_number = fields.Integer()
    company_size = fields.Selection(
        string="Company size",
        selection=[('micro', 'Micro'), ('small', 'Small'),
                   ('medium', 'Medium'), ('big', 'Big')])
