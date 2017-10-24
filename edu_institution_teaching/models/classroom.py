# -*- coding: utf-8 -*-

from odoo import models, fields, api


# class Classroom(model.Model):
#     _name = 'ei_teaching.classroom'
#     _description = '教室'

#     name = fields.Char("教室名称", required=True)
#     capacity =  fields.Integer("容纳人数")
#     time_slot_ids =  fields.Many2many(
#         'ei_teaching.time_slot', '上课时间段',
#         copy=False, readonly=False, track_visibility="onchange")
# #     value = fields.Integer()
