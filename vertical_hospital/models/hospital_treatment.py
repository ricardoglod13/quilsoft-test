from odoo import models, api, fields
from odoo.exceptions import UserError

class HospitalTreatment(models.Model):
    _name = 'hospital.treatment'
    _description = 'Tratamiento'

    code = fields.Char(string='Código')
    name = fields.Char(string='Nombre')
    doctor = fields.Char(string='Médico')

    @api.constrains('code')
    def check_code(self):
        for record in self:
            if '026' in record.code:
                raise UserError('El código del tratamiento no puede contener la secuencia "026".')

    