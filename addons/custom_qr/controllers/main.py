from odoo import http
from odoo.http import request
from datetime import datetime
import logging

_logger = logging.getLogger(__name__)  # ✅ aggiungi questo in cima

class CustomQR(http.Controller):

    # CORREZIONE: La rotta DEVE essere '/custom_qr/info' per intercettare l'URL del QR
    @http.route('/custom_qr/info', auth='public', website=True)
    def show_ticket_info(self, token=None, **kwargs):
        
        ticket = request.env['custom.qr.ticket'].sudo().search([('token', '=', token)], limit=1)
        
        if not ticket:
            # Gestione errore per token non trovato
            values = {'error': 'QR non valido o ticket non trovato.', 'token': False}
            return request.render('custom_qr.qr_ticket_template', values)
        
        # 🔍 DEBUG: stampiamo cosa c’è dentro ticket.date_created
        _logger.info("🕒 Ticket trovato: %s", ticket)
        _logger.info("🕒 Data creazione grezza: %s", ticket.date_created)

        # Prepara i valori per il template
        values = {
            'name': ticket.user_id.name,
            'department': ticket.department,
            'token': ticket.token,
            # CORREZIONE: Formatta la data in stringa leggibile per il template
            'date_time': ticket.date_created.strftime("%d/%m/%Y %H:%M:%S") if ticket.date_created else "",
        }
        
        _logger.info("🕒 Valore passato al template: %s", values['date_time'])
        
        # Renderizza il template corretto
        return request.render('custom_qr.qr_ticket_template', values)