# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class ei_teaching_product_course(models.Model):
#     _name = 'ei_teaching.product_course'
#     _inherit = ['ir.model']
    

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()

#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100