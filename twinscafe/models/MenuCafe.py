from odoo import api, fields, models


class MenuCafe(models.Model):
    _name = 'twinscafe.menucafe'
    _description = 'New Description'

    name = fields.Char(string='Nama Menu')
    harga = fields.Integer(string='Harga', required=True)
    kelompokmenu_id = fields.Many2one(comodel_name='twinscafe.kelompokmenu', 
                                      string='Kelompok Menu',
                                      ondelete='cascade')
    supplier_id = fields.Many2many(comodel_name='twinscafe.supplier', string='Supplier')
    stok = fields.Integer(string='Stok')
    
    
    
   
    
    
