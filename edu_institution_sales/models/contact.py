# coding=utf-8

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class contact(models.Model):
    _name = 'edu_institution_sales.contact'
    _inherits = {'res.partner': 'partner_id'}
    _order = 'sequence, id'

    sequence = fields.Integer(help="Determine the display order", default=10, string="自动生成")
    english_name = fields.Char('English Name', size=128)
    gender = fields.Selection(
        [('m', '男'), ('f', '女'),
         ('o', '其他')], 'Gender')
    birth_date = fields.Date('Birth Date')
    contact_parent_name = fields.Char('Parent Name', size=128)
    other_mobile =  fields.Char('Other Mobile', size=128)
    school =  fields.Char('Home Number', size=128)
    memo1 =  fields.Text('Memo 1')
    memo2 =  fields.Text('Memo 2')

    @api.multi
    @api.constrains('birth_date')
    def _check_birthdate(self):
        for record in self:
            if record.birth_date > fields.Date.today():
                raise ValidationError(_(
                    "Birth Date can't be greater than current date!"))

