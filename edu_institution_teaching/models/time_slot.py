# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ei_teaching_time_slot(models.Model):
    _name = 'ei_teaching.time_slot'
    _description = "上课时间设置"
    _order = 'hour_from'

    hour_from = fields.Float(string='From', required=True, index=True, help="Start and End time of class.")
    hour_to = fields.Float(string='To', required=True)

    def hours_time_string(hours):
        """ convert a number of hours (float) into a string with format '%H:%M' """
        minutes = int(round(hours * 60))
        return "%02d:%02d" % divmod(minutes, 60)


class time_slots_in_day(models.Model):
    _name = 'ei_teaching.time_slots_in_day'
    _order = 'dayofweek'

    dayofweek = fields.Selection([
        ('0', 'Monday'),
        ('1', 'Tuesday'),
        ('2', 'Wednesday'),
        ('3', 'Thursday'),
        ('4', 'Friday'),
        ('5', 'Saturday'),
        ('6', 'Sunday')
        ], 'Day of Week', required=True, index=True, default='0')

    time_slots = fields.Many2one("ei_teaching.time_slot", string="time_slots")
