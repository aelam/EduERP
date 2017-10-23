# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ei_teaching_time_slot(models.Model):
    _name = 'edu_institution_teaching.time_slot'
    _description = "上课时间设置"
    _order = 'hour_from'

    hour_from = fields.Float(string='From', required=True, index=True, help="Start and End time of working.")
    hour_to = fields.Float(string='To', required=True)

    def hours_time_string(hours):
        """ convert a number of hours (float) into a string with format '%H:%M' """
        minutes = int(round(hours * 60))
        return "%02d:%02d" % divmod(minutes, 60)

