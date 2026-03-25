from services.inventaris import Inventaris
from models.barang_elektronik import BarangElektronik
from models.barang_atk import BarangATK
from models.barang_furniture import BarangFurniture

def main():
    inventaris = Inventaris()

    # TAMBAH BARANG
    b1 = BarangElektronik("E001", "Laptop", 10, 65)
    b2 = BarangATK("A001", "Pensil", 20, "Biru")
    b3 = BarangFurniture("F001", "Meja", 5, "Biru")
    inventaris.tambah_barang(b1)
    inventaris.tambah_barang(b2)
    inventaris.tambah_barang(b3)

    print("\nDaftar barang:")
    inventaris.tampilkan_semua()
    
    print("\n HASIL PENCARIAN 'lap' ")
    hasil = inventaris.cari("lap")
    for barang in hasil:
        print(barang.display_info())

    # Hapus Barang
    inventaris.hapus_barang("E001")

    print("\nDaftar barang setelah dihapus:")
    inventaris.tampilkan_semua()

if __name__ == '__main__':
    main()