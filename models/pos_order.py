# -*- coding: utf-8 -*-
from odoo import api, fields, models, Command, _

import logging

class PosORder(models.Model):
    _inherit = "pos.order"

    def _create_invoice(self, move_vals):
        res = super()._create_invoice(move_vals)
        return res

    def _generate_pos_order_invoice(self):
        res = super()._generate_pos_order_invoice()
        move_id = self.env['account.move'].search([('id','=', res['res_id'])])
        if move_id:
            move_id.action_process_edi_web_services(with_commit=False)
        return res

    def _add_mail_attachment(self, name, ticket):
        attachment = super()._add_mail_attachment(name, ticket)
        logging.warning('_add_mail_attachment inherit don')
        logging.warning(attachment)
        if attachment:
            if self.mapped('account_move'):
                edi_documentos = self.env['account.edi.document'].search([('move_id', '=', self.account_move.ids[0]),('edi_format_name','=','CFDI (4.0)')])
                if edi_documentos:
                    logging.warning('encontró edi documentos inherit')
                    logging.warning(edi_documentos)
                    xml = edi_documentos.attachment_id
                    logging.warning(xml)
                    attachment += [(4, xml.id)]
        logging.warning('final res')
        return attachment
