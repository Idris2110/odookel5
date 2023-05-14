# -*- coding: utf-8 -*-
# from odoo import http


# class MuhammadFarhanA(http.Controller):
#     @http.route('/muhammad_farhan_a/muhammad_farhan_a', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/muhammad_farhan_a/muhammad_farhan_a/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('muhammad_farhan_a.listing', {
#             'root': '/muhammad_farhan_a/muhammad_farhan_a',
#             'objects': http.request.env['muhammad_farhan_a.muhammad_farhan_a'].search([]),
#         })

#     @http.route('/muhammad_farhan_a/muhammad_farhan_a/objects/<model("muhammad_farhan_a.muhammad_farhan_a"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('muhammad_farhan_a.object', {
#             'object': obj
#         })
