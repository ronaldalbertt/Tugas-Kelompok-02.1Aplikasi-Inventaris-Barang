from models.item import Item

class BarangFurniture(Item):
    def __init__(self, id_barang, nama, jumlah, bahan):
        super().__init__(id_barang, nama, jumlah)
        self.__bahan = bahan

    def get_bahan(self):
        return self.__bahan

    def display_info(self):
        return f"ID: {self.get_id()}, Nama: {self.get_nama()}, Jumlah: {self.get_jumlah()}, Bahan: {self.__bahan}"