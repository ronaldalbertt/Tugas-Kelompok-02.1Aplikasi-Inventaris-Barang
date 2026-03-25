from mixins.log_mixin import LogMixin
from mixins.search_mixin import SearchMixin

class Inventaris(LogMixin, SearchMixin):
    def __init__(self):
        self.__daftar_barang = []

    # TAMBAH BARANG
    def tambah_barang(self, barang):
        self.__daftar_barang.append(barang)
    
    # HAPUS BARANG
    def hapus_barang(self, id_barang):
        for barang in self.__daftar_barang:
            if barang.get_id() == id_barang:
                self.__daftar_barang.remove(barang)
                self.log(f"Barang '{barang.get_nama()}' berhasil dihapus")
                return
        raise ValueError(f"Barang dengan ID {id_barang} tidak ditemukan")

    # UPDATE BARANG
    def update_barang(self, id_barang, jumlah_baru):
        for barang in self.__daftar_barang:
            if barang.get_id() == id_barang:
                barang.set_jumlah(jumlah_baru)
                self.log(f"Jumlah barang '{barang.get_nama()}' diperbarui")
                return
        raise ValueError("Barang tidak ditemukan")

    # TAMPILKAN SEMUA
    def tampilkan_semua(self):
        for barang in self.__daftar_barang:
            print(barang.display_info())

    # CARI BARANG
    def cari(self, keyword):
        hasil = self.cari_barang(self.__daftar_barang, keyword)
        return hasil

    # GET DATA (READ ONLY)
    def get_semua_barang(self):
        return self.__daftar_barang