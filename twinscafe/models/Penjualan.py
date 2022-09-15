from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError




class Penjualan(models.Model):
    _name = 'twinscafe.penjualan'
    _description = 'New Description'

    name = fields.Char(string='No. Meja')
    nama_pembeli = fields.Char(string='Nama Pembeli')
    tgl_penjualan = fields.Datetime(string='Tgl. Transaksi', default = fields.Datetime.now())
    total_bayar = fields.Integer(compute='_compute_totalbayar', string='Total Pembayaran')
    detailpenjualan_ids = fields.One2many(
        comodel_name='twinscafe.detailpenjualan', 
        inverse_name='penjualan_id', 
        string='Detail Penjualan')
    state = fields.Selection(
        string='Status',
        selection=[('draft', 'Draft'),
                   ('confirm', 'Confirm'),
                   ('done', 'Done'),
                   ('cancelled', 'Cancelled'),
                   ],
        required=True, readonly=True, default='draft')

    def action_confirm(self):
        self.write({'state': 'confirm'})

    def action_done(self):
        self.write({'state': 'done'})

    def action_cancel(self):
        self.write({'state': 'cancelled'})

    def action_draft(self):
        self.write({'state': 'draft'})

    @api.depends('detailpenjualan_ids')
    def _compute_totalbayar(self):
        for rec in self:
            a = sum(self.env['twinscafe.detailpenjualan'].search([('penjualan_id','=',rec.id)]).mapped('subtotal'))
            rec.total_bayar = a

    @api.ondelete(at_uninstall=False)
    def _ondelete_penjualan(self):
        if self.filtered(lambda line: line.state != 'draft'):
            raise UserError("Tdak dapat menghapus jika status BUKAN DRAFT")
        else:
            if self.detailpenjualan_ids:
                a=[]
                for rec in self:
                    a = self.env['twinscafe.detailpenjualan'].search([('penjualan_id','=',rec.id)])
                    print(a)
                for ob in a:
                    print(str(ob.menucafe_id.name) + ' ' + str(ob.qty))
                    ob.menucafe_id.stok += ob.qty

    def write(self,vals):
        for rec in self:
            a = self.env['twinscafe.detailpenjualan'].search([('penjualan_id','=',rec.id)])
            print(a)
            for data in a:
                print(str(data.menucafe_id.name)+' '+str(data.qty)+' '+str(data.menucafe_id.stok))
                data.menucafe_id.stok += data.qty
        record = super(Penjualan,self).write(vals)
        for rec in self:
            b = self.env['twinscafe.detailpenjualan'].search([('penjualan_id','=',rec.id)])
            print(a)
            print(b)
            for databaru in b:
                if databaru in a:
                    print(str(databaru.menucafe_id.name)+' '+str(databaru.qty)+' '+str(databaru.menucafe_id.stok))
                    databaru.menucafe_id.stok -= databaru.qty
                else:
                    pass
        return record

    _sql_constraints = [
        ('no_meja_unik','unique(name)','Nomor Meja Sudah Penuh !!!')
    ]
    

class DetailPenjualan(models.Model):
    _name = 'twinscafe.detailpenjualan'
    _description = 'New Description'

    name = fields.Char(string='Nama')
    penjualan_id = fields.Many2one(comodel_name='twinscafe.penjualan', string='Detail Penjualan')
    menucafe_id = fields.Many2one(comodel_name='twinscafe.menucafe', string='List Menu Cafe')
    harga_satuan = fields.Integer(string='Harga Satuan')
    qty = fields.Integer(string='Quantity')
    subtotal = fields.Integer(compute='_compute_subtotal', string='Subtotal')
    
    @api.depends('harga_satuan','qty')
    def _compute_subtotal(self):
        for rec in self:
            rec.subtotal = rec.qty * rec.harga_satuan
    
    @api.onchange('menucafe_id')
    def _onchange_menucafe_id(self):
        if (self.menucafe_id.harga):
            self.harga_satuan = self.menucafe_id.harga

    @api.model
    def create(self,vals):
        record = super(DetailPenjualan,self).create(vals)
        if record.qty:
            self.env['twinscafe.menucafe'].search([('id','=',record.menucafe_id.id)]).write({'stok' : record.menucafe_id.stok - record.qty})
        return record  

    @api.constrains('qty')
    def check_Quantity(self):
        for rec in self:
            if rec.qty <1:
                raise ValidationError("Mau beli {} berapa banyak sih..".format(rec.menucafe_id.name))
            elif (rec.menucafe_id.stok < rec.qty):
                raise ValidationError('Stok {} tidak mencukupi, hanya tersedia {}'.format(rec.menucafe_id.name,rec.menucafe_id.stok))
    
    
    
