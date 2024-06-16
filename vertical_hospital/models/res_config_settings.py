# -*- coding: utf-8 -*-
from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    hospital_pacient_endpoint = fields.Char(string='Endpoint Consulta de Pacientes')

    @api.model
    def set_values(self):
        res = super(ResConfigSettings, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param('hospital_pacient_endpoint', self.hospital_pacient_endpoint)
        return res

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        hospital_pacient_endpoint = self.env['ir.config_parameter'].sudo().get_param('hospital_pacient_endpoint')
        res.update({
            'hospital_pacient_endpoint': eval(hospital_pacient_endpoint) if hospital_pacient_endpoint else False,
        })
        return res