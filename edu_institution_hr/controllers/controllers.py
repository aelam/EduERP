# -*- coding: utf-8 -*-
from odoo import http

# class EduInstitutionHr(http.Controller):
#     @http.route('/edu_institution_hr/edu_institution_hr/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/edu_institution_hr/edu_institution_hr/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('edu_institution_hr.listing', {
#             'root': '/edu_institution_hr/edu_institution_hr',
#             'objects': http.request.env['edu_institution_hr.edu_institution_hr'].search([]),
#         })

#     @http.route('/edu_institution_hr/edu_institution_hr/objects/<model("edu_institution_hr.edu_institution_hr"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('edu_institution_hr.object', {
#             'object': obj
#         })