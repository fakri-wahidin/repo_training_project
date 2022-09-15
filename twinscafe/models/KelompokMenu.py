from odoo import api, fields, models


class KelompokMenu(models.Model):
    _name = 'twinscafe.kelompokmenu'
    _description = 'New Description'

    name = fields.Selection([
        ('maincourse', 'Main Course'),
        ('ricebowls', 'Rice Bowls'),
        ('dessert', 'Dessert'),
        ('snack', 'Snack'),
        ('drinks', 'Drinks'),
        ('coffee', 'Coffee'),
        ('flavortea', 'Flavor Tea')
    ], string='Nama Kelompok')
    
    kode_kelompok = fields.Char(string='Kode Kelompok')
    
        
    @api.onchange('name')
    def _onchange_kode_kelompok(self):
        if (self.name == 'maincourse'):
            self.kode_kelompok = 'mc01'
        elif (self.name == 'ricebowls'):
            self.kode_kelompok = 'rb01'
        elif (self.name == 'dessert'):
            self.kode_kelompok = 'ds01'
        elif (self.name == 'snack'):
            self.kode_kelompok = 'sk01'
        elif (self.name == 'drinks'):
            self.kode_kelompok = 'dk01'
        elif (self.name == 'coffee'):
            self.kode_kelompok = 'cf01'
        elif (self.name == 'flavortea'):
            self.kode_kelompok = 'ft01'


    kode_menu = fields.Char(string='Kode Menu')
    menucafe_ids = fields.One2many(comodel_name='twinscafe.menucafe', 
                                  inverse_name='kelompokmenu_id', 
                                  string='Daftar Menu Cafe')
    jml_item = fields.Char(compute='_compute_jml_item', string='Jumlah Item')
    
    @api.depends('menucafe_ids')
    def _compute_jml_item(self):
        for rec in self:
            a = self.env['twinscafe.menucafe'].search([('kelompokmenu_id','=', rec.id)]).mapped('name')
            b = len(a)
            rec.jml_item = b
            rec.daftar = a

    daftar = fields.Char(string='Daftar Isi')
    
    
