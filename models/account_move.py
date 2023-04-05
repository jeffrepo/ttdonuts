# -*- coding: utf-8 -*-
from odoo import api, fields, models, Command, _

import logging

class AccountMove(models.Model):
    _inherit = "account.move"

    def calcular(self):
        logging.warning('a jeff')

    def _post(self, soft=True):
        res = super()._post(soft=True)
        logging.warning('el res')
        logging.warning(res)
        if res:
            res.action_process_edi_web_services(with_commit=False)
        return res

class PosORder(models.Model):
    _inherit = "pos.order"

    def _create_invoice(self, move_vals):
        res = super()._create_invoice(move_vals)
        logging.warning('create inmvoice')
        logging.warning(res)
        logging.warning(res.state)
        return res

    def _generate_pos_order_invoice(self):
        res = super()._generate_pos_order_invoice()
        logging.warning('_generate_pos_order_invoice')
        logging.warning(res)
        move_id = self.env['account.move'].search([('id','=', res['res_id'])])
        logging.warning('move_id_encontrado')
        logging.warning(move_id)
        logging.warning(move_id.state)
        if move_id:
            move_id.action_process_edi_web_services(with_commit=False)
        return res
