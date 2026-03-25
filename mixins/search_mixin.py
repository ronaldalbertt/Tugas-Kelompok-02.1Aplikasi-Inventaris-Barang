class SearchMixin:

    def cari_barang(self, daftar_barang, keyword):
        hasil = []
        for barang in daftar_barang:
            if keyword.lower() in barang.get_nama().lower():
                hasil.append(barang)
        return hasil