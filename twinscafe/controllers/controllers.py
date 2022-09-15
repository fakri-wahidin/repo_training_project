from odoo import http, models, fields
from odoo.http import request
import json

class twinscafe(http.Controller):
    @http.route('/twinscafe/getmenucafe', auth='public', method=['GET'])
    def getmenucafe(self, **kw):
        menucafe = request.env['twinscafe.menucafe'].search([])
        isi = []
        for mc in menucafe:
            isi.append({
                'nama_barang' : mc.name,
                'harga-jual' : mc.harga,
                'stok' : mc.stok
            })
        return json.dumps(isi)

    @http.route('/twinscafe/getsupplier', auth='public', method=['GET'])
    def getSupplier(self, **kw):
        supplier = request.env['twinscafe.supplier'].search([])
        sup = []
        for s in supplier:
            sup.append({
                'nama_perusahaan' : s.name,
                'alamat' : s.alamat,
                'no_telepon' : s.no_telp
            })
        return json.dumps(sup)
