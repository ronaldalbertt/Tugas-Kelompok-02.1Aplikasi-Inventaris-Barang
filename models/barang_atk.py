from models.item import Item

class BarangATK(Item):
    def __init__(self, id_barang, nama, jumlah, jenis):
        super().__init__(id_barang, nama, jumlah)
        self.__jenis = jenis

    def get_jenis(self):
        return self.__jenis
    
    def display_info(self):
        return f"ID: {self.get_id()}, Name: {self.get_nama()}, Jumlah: {self.get_jumlah()}, Jenis: {self.__jenis}"