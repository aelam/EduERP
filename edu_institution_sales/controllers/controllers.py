# -*- coding: utf-8 -*-
from odoo import http

# class EduInstitutionSales(http.Controller):
#     @http.route('/edu_institution_sales/edu_institution_sales/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/edu_institution_sales/edu_institution_sales/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('edu_institution_sales.listing', {
#             'root': '/edu_institution_sales/edu_institution_sales',
#             'objects': http.request.env['edu_institution_sales.edu_institution_sales'].search([]),
#         })

#     @http.route('/edu_institution_sales/edu_institution_sales/objects/<model("edu_institution_sales.edu_institution_sales"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('edu_institution_sales.object', {
#             'object': obj
#         })