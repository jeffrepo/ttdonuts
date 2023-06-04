# -*- coding: utf-8 -*-
from odoo import api, fields, models, Command, _

import logging

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

    def _add_mail_attachment(self, name, ticket):
        attachment = super()._add_mail_attachment(name, ticket)
        logging.warning('_add_mail_attachment inherit don')
        logging.warning(res)
        if res:
            if self.mapped('account_move'):
                edi_documentos = self.env['account.edi.document'].search([('move_id', '=', self.account_move.ids[0]),('edi_format_name','=','CFDI (4.0)')])
                if edi_documentos:
                    logging.warning('encontró edi documentos 33')
                    logging.warning(edi_documentos)
                    xml = edi_documentos.attachment_id
                    logging.warning(xml)
                    attachment += [(4, xml.id)]
        logging.warning('final res')
        return attachment
