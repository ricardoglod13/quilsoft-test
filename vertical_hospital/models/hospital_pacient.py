from datetime import datetime
from odoo import models, api, fields
from odoo.exceptions import UserError

class HospitalPacient(models.Model):
    _name = 'hospital.pacient'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Paciente'

    sequence = fields.Char(string='Secuencia', default='/')
    name = fields.Char(string='Nombre y Apellido')
    dni = fields.Char(string='DNI', tracking=True)
    treatment_ids = fields.Many2many(comodel_name='hospital.treatment', string='Tratamientos')
    discharge_date = fields.Datetime(string='Fecha de Alta')
    state = fields.Selection(selection=[('draft', 'Borrador'), ('discharge', 'Alta'), ('charge', 'Baja')],
                default='draft',
                string='Estado',
                tracking=True)
    
    @api.constrains('dni')
    def check_dni(self):
        for record in self:
            if not record.dni.isdigit():
                raise UserError('El DNI solo puede contener numeros.')
    
    @api.onchange('state')
    def _onchange_state(self):
        for record in self:
            if record.state == 'discharge':
                record.discharge_date = datetime.now()

    @api.model_create_multi
    def create(self, vals_list):
        res = super().create(vals_list)
        for record in res:
            if record.sequence == '/':
                record.sequence = self.env['ir.sequence'].next_by_code('hospital.pacient.sequence')
        return res

    def _get_state(self):
        self.ensure_one()
        selection = self._fields['state']._description_selection(self.env)
        return list(filter(lambda s: s[0] == self.state, selection))[0][1]

    def print_report(self):
        return self.env.ref('vertical_hospital.action_hospital_pacient_report').report_action(self)
    