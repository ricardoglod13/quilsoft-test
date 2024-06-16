import json
from odoo import http
from odoo.http import request, Response

class PacientController(http.Controller):

    @http.route('/pacientes/consulta/<string:sequence>', type='http', auth="none")
    def get_pacient(self, sequence):
        pacients = request.env['hospital.pacient'].search_read(domain=[('sequence', '=', sequence)], fields=['sequence', 'name', 'dni', 'state'])
        return Response(json.dumps(pacients), content_type='application/json;charset=utf-8', status=200)
