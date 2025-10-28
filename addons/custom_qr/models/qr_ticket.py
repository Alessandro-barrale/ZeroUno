# custom_qr/models/qr_ticket.py

from odoo import models, fields, api
import qrcode
from io import BytesIO
import base64

# Rimuovi l'import di 'uuid' se presente, non è più necessario.


class CustomQRTicket(models.Model):
    _name = "custom.qr.ticket"
    _description = "Ticket con QR associato a utente"

    name = fields.Char(string="Nome Ticket", required=True)
    user_id = fields.Many2one("res.users", string="Utente", required=True)
    department = fields.Char(string="Dipartimento", default="Pasticceria")
    date_created = fields.Datetime(
        string="Data creazione", default=fields.Datetime.now, readonly=True
    )
    # Imposta default='New' per segnalare la creazione di un nuovo record sequenziale
    token = fields.Char(
        string="Numero Ticket", readonly=True, index=True, copy=False, default="New"
    )
    qr_image = fields.Binary(
        string="QR Code", readonly=True, attachment=True, copy=False
    )

    # Campo calcolato per mostrare l'URL nell'interfaccia (utile per debugging)
    qr_url_display = fields.Char(
        string="URL Pubblico", compute="_compute_qr_url_display", store=False
    )

    @api.depends("token")
    def _compute_qr_url_display(self):
        base_url = self.env["ir.config_parameter"].sudo().get_param("web.base.url")
        for ticket in self:
            if ticket.token:
                ticket.qr_url_display = (
                    f"{base_url}/custom_qr/info?token={ticket.token}"
                )
            else:
                ticket.qr_url_display = False

    @api.model
    def create(self, vals):
        # 1. Genera il token usando la Sequenza Odoo
        vals.setdefault("date_created", fields.Datetime.now())
        if vals.get("token", "New") == "New":
            # 'ticket.sequence' è il codice che definiremo in qr_ticket_views.xml
            vals["token"] = (
                self.env["ir.sequence"].next_by_code("ticket.sequence") or "New"
            )

        # 2. Ottieni l'URL base e costruisci il link completo
        base_url = self.env["ir.config_parameter"].sudo().get_param("web.base.url")
        qr_url = f"{base_url}/custom_qr/info?token={vals['token']}"

        # 3. Genera il QR code come immagine PNG
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
        )
        qr.add_data(qr_url)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")

        # 4. Salva l'immagine in base64
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        vals["qr_image"] = base64.b64encode(buffer.getvalue())
        # Rimosso .decode() per maggiore compatibilità con il campo Binary Odoo
        
        if not vals.get("date_created"):
            vals["date_created"] = fields.Datetime.now()

        return super(CustomQRTicket, self).create(vals)
