# -*- coding: utf-8 -*-
from odoo import http

# class EduInstitutionFinance(http.Controller):
#     @http.route('/edu_institution_finance/edu_institution_finance/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/edu_institution_finance/edu_institution_finance/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('edu_institution_finance.listing', {
#             'root': '/edu_institution_finance/edu_institution_finance',
#             'objects': http.request.env['edu_institution_finance.edu_institution_finance'].search([]),
#         })

#     @http.route('/edu_institution_finance/edu_institution_finance/objects/<model("edu_institution_finance.edu_institution_finance"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('edu_institution_finance.object', {
#             'object': obj
#         })