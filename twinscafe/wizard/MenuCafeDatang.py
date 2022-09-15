from odoo import api, fields, models


class MenuCafeDatang(models.TransientModel):
    _name = 'twinscafe.menucafedatang'

    menucafe_id = fields.Many2one(comodel_name='twinscafe.menucafe', 
                                string='Nama Menu Cafe',
                                required='True')
    

    jumlah = fields.Integer(string='Jumlah',
                            required='False')

    def button_menucafe_datang(self):
        for rec in self:
            self.env['twinscafe.menucafe'].search([('id', '=', rec.menucafe_id.id)]).write({'stok' : rec.menucafe_id.stok + rec.jumlah})