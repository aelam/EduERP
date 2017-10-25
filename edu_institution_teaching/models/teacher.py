from odoo import models, fields, api

class Teacher(models.Model):
    _inherit = "ei_hr.employee"
    _name = "ei_teaching.teacher"
    
    is_foreign_teacher = fields.Boolean(string='Is a Foreign Teacher')



