# -*- coding: utf-8 -*-

from odoo import models, fields, api

class op_channel(models.Model):
    _name = 'open_academy.op_channel'

    name = fields.Char('运营渠道', translate=True, required=True)

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Tag name already exists !"),
    ]

class market_channel(models.Model):
    _name = 'open_academy.market_channel'

    channel_type = fields.Selection([
        ('Online', '线上'),
        ('Offline', '线下')
    ])

    op_channel_id = fields.Many2one(
        'open_academy.op_channel', '运营渠道',
        copy=False, readonly=False, track_visibility="onchange",
        help="运营渠道")
    info_source = fields.Char()
    address = fields.Char()
    fee = fields.Float()
    is_active = fields.Boolean() # 是否激活
    note = fields.Text()


# # TODO: 继承公司
# class center(models.Model):
#     _name = 'open_academy.center'
#     name = fields.Char('中心', translate=True, required=True)

    


# class open_academy(models.Model):
#     _name = 'open_academy.open_academy'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100