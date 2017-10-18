# -*- coding: utf-8 -*-
from odoo import http

# class EduInstitutionTeaching(http.Controller):
#     @http.route('/edu_institution_teaching/edu_institution_teaching/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/edu_institution_teaching/edu_institution_teaching/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('edu_institution_teaching.listing', {
#             'root': '/edu_institution_teaching/edu_institution_teaching',
#             'objects': http.request.env['edu_institution_teaching.edu_institution_teaching'].search([]),
#         })

#     @http.route('/edu_institution_teaching/edu_institution_teaching/objects/<model("edu_institution_teaching.edu_institution_teaching"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('edu_institution_teaching.object', {
#             'object': obj
#         })