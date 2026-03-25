import unittest
from services.inventaris import Inventaris
from models.barang_elektronik import BarangElektronik

class TestInventaris(unittest.TestCase):

    def setUp(self):
        self.inventaris = Inventaris()
        self.barang = BarangElektronik("E001", "Laptop", 10, 65)
        self.inventaris.tambah_barang(self.barang)

    def test_tambah_barang(self):
        self.assertEqual(len(self.inventaris.get_semua_barang()), 1)

    def test_update_barang(self):
        self.inventaris.update_barang("E001", 20)
        self.assertEqual(self.barang.get_jumlah(), 20)

    def test_hapus_barang(self):
        self.inventaris.hapus_barang("E001")
        self.assertEqual(len(self.inventaris.get_semua_barang()), 0)

    def test_barang_tidak_ditemukan(self):
        with self.assertRaises(ValueError):
            self.inventaris.update_barang("x999", 5)

if __name__ == '__main__':
    unittest.main()