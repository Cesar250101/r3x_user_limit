# Part of RU3IX licensing
# See __manifest__.py file for full copyright and licensing details.

from odoo import models, fields, api,_
from odoo.exceptions import UserError

class Users(models.Model):
    _inherit = "res.users"

    @api.model_create_multi
    def create(self, vals_list):
        icp = self.env['ir.config_parameter']
        user_limit = icp.get_param('user_counts')
        users = self.search([('active','=',True)] )
        active_users = len(users)  - 1
        if active_users >= int(user_limit):
            raise UserError(_("Su plan incluye hasta '%s'. Por favor comuniquese con pablo@method.cl!")% (user_limit,))
        return super(Users, self).create(vals_list)


