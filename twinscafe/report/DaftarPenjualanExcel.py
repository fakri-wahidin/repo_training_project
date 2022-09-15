from dataclasses import fields
from odoo import models, fields
from datetime import timedelta


class PartnerXlsx(models.AbstractModel):
    _name = 'report.twinscafe.report_penjualan_xlsx'
    _inherit = 'report.report_xlsx.abstract'
    
    tgl_lap = fields.Date.today()
    

    def generate_xlsx_report(self, workbook, data, penjualan):
        sheet = workbook.add_worksheet('Daftar Penjualan')
        bold = workbook.add_format({'bold': True})
        sheet.write(0, 0, str(self.tgl_lap))
        sheet.write(1, 0, 'No. Meja')
        sheet.write(1, 1, 'Nama Pembeli')
        sheet.write(1, 2, 'Tgl. Transaksi')
        sheet.write(1, 3, 'Total Pembayaran')
        row = 2
        col = 0
        for obj in penjualan:
            col = 0
            sheet.write(row, col, obj.name)
            sheet.write(row, col+1, obj.nama_pembeli)
            sheet.write(row, col+2, (obj.tgl_penjualan+ timedelta(hours=7)).strftime("%d/%m/%Y, %H:%M:%S"))
            sheet.write(row, col+3, obj.total_bayar)
            row += 1