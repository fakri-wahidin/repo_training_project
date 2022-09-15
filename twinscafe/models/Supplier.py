from odoo import api, fields, models


class Supplier(models.Model):
    _name = 'twinscafe.supplier'
    _description = 'New Description'

    name = fields.Char(string='Nama Supplier')
    alamat = fields.Char(string='Alamat')
    no_telp = fields.Char(string='No. Telepon')
    menucafe_id = fields.Many2many(comodel_name='twinscafe.menucafe', string='Menu Cafe')
    
    
    
