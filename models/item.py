from abc import ABC, abstractmethod

class Item(ABC):
    def __init__(self, id_barang, nama, jumlah):
        self.__id_barang = id_barang
        self.__nama = nama
        self.__jumlah = 0
        self.set_jumlah(jumlah)  # Set jumlah menggunakan Validasi
        
        # GETTER (Enkapsulasi)
    def get_id(self):
        return self.__id_barang

    def get_nama(self):
        return self.__nama

    def get_jumlah(self):
        return self.__jumlah

    # SETTER (Validasi)
    def set_jumlah(self, jumlah):
        if jumlah < 0:
            raise ValueError("Jumlah tidak boleh negatif")
        self.__jumlah = jumlah

    # ABSTRACT METHOD
    @abstractmethod
    def display_info(self):
        pass