from odoo import models, fields, api, _

# Questa classe estende il modello esistente 'counter.counter'
class CounterCounterExtend(models.Model):
    _inherit = 'counter.counter'

    # Aggiunge il campo 'state' che la tua vista XML cerca
    state = fields.Selection([
        ('unused', 'Inattivo'),
        ('in_progress', 'In Sessione'),
    ], string='Stato', default='unused', required=True)

    # Aggiunge i metodi per i bottoni nella vista Kanban
    def action_start_processing(self):
        self.ensure_one()
        self.state = 'in_progress'

    def action_close_session(self):
        self.ensure_one()
        self.state = 'unused'

# Se il tuo file conteneva anche la classe 'customer.queue.service', lasciala.
# La classe sopra è quella che risolve l'errore attuale.