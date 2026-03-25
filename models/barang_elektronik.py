from models.item import Item

class BarangElektronik(Item):
    def __init__(self, id_barang, nama, jumlah, daya):
        super().__init__(id_barang, nama, jumlah)
        self.__daya = daya

    # GETTER (Enkapsulasi)
    def get_daya(self):
        return self.__daya

    # Abstract Method
    def display_info(self):
        return f"ID: {self.get_id()}, Nama: {self.get_nama()}, Jumlah: {self.get_jumlah()}, Daya: {self.__daya} Watt"