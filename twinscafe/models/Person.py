from odoo import api, fields, models


class Person(models.Model):
    _name = 'twinscafe.person'
    _description = 'New Description'

    name = fields.Char(string='Nama')
    tgl_lahir = fields.Date(string='Tanggal Lahir')
    alamat = fields.Char(string='Alamat')
    no_hp = fields.Char(string='No. Handphone')
    

class Barista(models.Model):
    _name = 'twinscafe.barista'
    _inherit = 'twinscafe.person'
    _description = 'New Description'

    id_barista = fields.Char(string='ID Barista')


class Chef(models.Model):
    _name = 'twinscafe.chef'
    _inherit = 'twinscafe.person'
    _description = 'New Description'

    id_chef = fields.Char(string='ID Chef')

class Cashier(models.Model):
    _name = 'twinscafe.cashier'
    _inherit = 'twinscafe.person'
    _description = 'New Description'

    id_cashier = fields.Char(string='ID Cashier')


class Waiters(models.Model):
    _name = 'twinscafe.waiters'
    _inherit = 'twinscafe.person'
    _description = 'New Description'

    id_waiters = fields.Char(string='ID Waiters')


class OfficeBoy(models.Model):
    _name = 'twinscafe.officeboy'
    _inherit = 'twinscafe.person'
    _description = 'New Description'

    id_oboy = fields.Char(string='ID OfficeBoy')
    
    
    
