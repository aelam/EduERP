

from odoo import models, fields, api


class DemoClass(models.Model):
    _name  = 'ei_teaching.demo_class'

    chinese_teacher = fields.Many2one("ei_teaching.teacher", string="chinese_teacher")
    foreign_teacher = fields.Many2one("ei_teaching.teacher", string="foreign_teacher")

    date_start = fields.Date(string='Start Date', help="Default start date")
    classroom = fields.Many2one("ei_teaching.classroom", string="classroom")
    hour_from = fields.Float(string='From', required=True, index=True, help="Start and End time of class.")
    hour_to = fields.Float(string='To', required=True)

    memo = fields.Char("备注")
    active = fields.Boolean("是否启用")

