# -*- coding: utf-8 -*-
# from odoo import http


# class CostumerQueueExtend(http.Controller):
#     @http.route('/costumer_queue_extend/costumer_queue_extend', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/costumer_queue_extend/costumer_queue_extend/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('costumer_queue_extend.listing', {
#             'root': '/costumer_queue_extend/costumer_queue_extend',
#             'objects': http.request.env['costumer_queue_extend.costumer_queue_extend'].search([]),
#         })

#     @http.route('/costumer_queue_extend/costumer_queue_extend/objects/<model("costumer_queue_extend.costumer_queue_extend"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('costumer_queue_extend.object', {
#             'object': obj
#         })
