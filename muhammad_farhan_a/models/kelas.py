from odoo import api, fields, models

class KelasERPD(models.Model):
    _name = 'erpd.kelas'
    _description = 'Ini adalah Kantor Kelas ERP D'

    kelas = fields.Char(string="Kelas", required=True)
    kode = fields.Integer(string="Kode")
    jenis = fields.Selection(
        [
        ("wajib", "Wajib"),
        ("pilihan", "Pilihan")
        ], required=True, default="wajib"
    )
    note = fields.Text(string="Deskripsi")
    status = fields.Boolean(string='Status Disetujui')
    tanggal = fields.Date(string='Tanggal Disetujui')
    waktu = fields.Datetime(string="Jadwal")