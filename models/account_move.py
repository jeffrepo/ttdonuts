# -*- coding: utf-8 -*-
from odoo import api, fields, models, Command, _

import logging

class AccountMove(models.Model):
    _inherit = "account.move"

    def _post(self, soft=True):
        res = super()._post(soft=True)
        logging.warning('el res')
        logging.warning(res)
        if res:
            res.action_process_edi_web_services(with_commit=False)
        return res

    def post(self):
        res = super().post()
        logging.warning('POST TT')
        logging.warning(res)
        if res:
            res.action_process_edi_web_services(with_commit=False)
        return res
