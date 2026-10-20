"""Pengelolaan inventaris toko menggunakan dictionary."""


def tambah_barang(inventaris, nama, harga, stok):
    nama = nama.strip()
    if not nama:
        raise ValueError("Nama barang tidak boleh kosong.")
    if nama in inventaris:
        raise ValueError(f"Barang '{nama}' sudah ada.")
    if harga < 0 or stok < 0:
        raise ValueError("Harga dan stok tidak boleh negatif.")
    inventaris[nama] = (harga, stok)


def ubah_stok(inventaris, nama, stok_baru):
    if nama not in inventaris:
        raise KeyError(f"Barang '{nama}' tidak ditemukan.")
    if stok_baru < 0:
        raise ValueError("Stok tidak boleh negatif.")
    harga, _ = inventaris[nama]
    inventaris[nama] = (harga, stok_baru)


def cari_barang_berdasarkan_harga(inventaris, harga_min, harga_maks):
    if harga_min > harga_maks:
        raise ValueError("Harga minimum tidak boleh lebih besar dari harga maksimum.")
    return {
        nama: data
        for nama, data in inventaris.items()
        if harga_min <= data[0] <= harga_maks
    }


def total_nilai_inventaris(inventaris):
    return sum(harga * stok for harga, stok in inventaris.values())


def tampilkan_inventaris(inventaris):
    if not inventaris:
        print("Inventaris masih kosong.")
        return
    for nama, (harga, stok) in inventaris.items():
        print(f"- {nama}: harga Rp{harga:g}, stok {stok}")


def main():
    inventaris = {}
    while True:
        print("\n=== Inventaris Toko ===")
        print("1. Tambah barang")
        print("2. Ubah stok")
        print("3. Cari barang berdasarkan rentang harga")
        print("4. Hitung total nilai inventaris")
        print("5. Tampilkan semua barang")
        print("0. Keluar")
        pilihan = input("Pilih menu: ").strip()

        try:
            if pilihan == "1":
                nama = input("Nama barang: ")
                harga = float(input("Harga: "))
                stok = int(input("Stok: "))
                tambah_barang(inventaris, nama, harga, stok)
                print("Barang berhasil ditambahkan.")
            elif pilihan == "2":
                nama = input("Nama barang: ").strip()
                stok = int(input("Stok baru: "))
                ubah_stok(inventaris, nama, stok)
                print("Stok berhasil diperbarui.")
            elif pilihan == "3":
                harga_min = float(input("Harga minimum: "))
                harga_maks = float(input("Harga maksimum: "))
                hasil = cari_barang_berdasarkan_harga(inventaris, harga_min, harga_maks)
                if hasil:
                    tampilkan_inventaris(hasil)
                else:
                    print("Tidak ada barang dalam rentang harga tersebut.")
            elif pilihan == "4":
                print(f"Total nilai inventaris: Rp{total_nilai_inventaris(inventaris):g}")
            elif pilihan == "5":
                tampilkan_inventaris(inventaris)
            elif pilihan == "0":
                break
            else:
                print("Pilihan tidak tersedia.")
        except (ValueError, KeyError) as error:
            print(f"Operasi gagal: {error}")


if __name__ == "__main__":
    main()
