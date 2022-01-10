from odoo import models, fields, api


class StockList(models.Model):
    _name = 'stock.mover'
    _description = 'Stock Moves'
    _rec_name = 'stock_pid'

    stock_pid = fields.Many2one('product.list', string='Product Name')
    prod_demand = fields.Integer(string='Demand')
    prod_done = fields.Integer(string='Done Product')

    stock_in = fields.Many2one('transfer.list', string='')

    @api.onchange('prod_done')
    def change_stock(self):
        for rec in self:
            stage_name = self.env['product.status'].search([])
            if rec.stock_in.op_type == 'dv001':
                rec.stock_pid.on_hand = rec.stock_pid.on_hand - rec.prod_done
                if rec.stock_pid.on_hand == 0:
                    rec.stock_pid.stage_update = stage_name[0]
            if rec.stock_in.op_type == 'back01':
                rec.stock_pid.on_hand = rec.stock_pid.on_hand + rec.prod_done
                if rec.stock_pid.on_hand > 0:
                    rec.stock_pid.stage_update = stage_name[1]
            if rec.stock_in.op_type == 'pur001':
                rec.stock_pid.on_hand = rec.stock_pid.on_hand + rec.prod_done
                if rec.stock_pid.on_hand > 0:
                    rec.stock_pid.stage_update = stage_name[1]
