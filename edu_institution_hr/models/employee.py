from odoo import models, api


class EIEmployee(models.Model):
    _inherit = 'hr.employee'
    _name = 'ei_hr.employee'

    @api.onchange('user_id')
    def onchange_user(self):
        if self.user_id:
            self.user_id.partner_id.supplier = True
            self.work_email = self.user_id.email
            self.identification_id = False

    @api.onchange('address_id')
    def onchange_address_id(self):
        if self.address_id:
            self.work_phone = self.address_id.phone
            self.mobile_phone = self.address_id.mobile
