# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class muhammad_farhan_a(models.Model):
#     _name = 'muhammad_farhan_a.muhammad_farhan_a'
#     _description = 'muhammad_farhan_a.muhammad_farhan_a'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
