"""Membandingkan penerima dua beasiswa menggunakan operasi set."""


def daftar_id(teks):
    return {id_mahasiswa.strip() for id_mahasiswa in teks.split(",") if id_mahasiswa.strip()}


def bandingkan_penerima(penerima_a, penerima_b):
    return {
        "keduanya": penerima_a & penerima_b,
        "hanya_a": penerima_a - penerima_b,
        "hanya_b": penerima_b - penerima_a,
        "semua_unik": penerima_a | penerima_b,
    }


def main():
    penerima_a = daftar_id(input("Masukkan ID penerima beasiswa A (pisahkan dengan koma): "))
    penerima_b = daftar_id(input("Masukkan ID penerima beasiswa B (pisahkan dengan koma): "))
    hasil = bandingkan_penerima(penerima_a, penerima_b)

    print(f"Menerima kedua beasiswa: {sorted(hasil['keduanya'])}")
    print(f"Hanya menerima beasiswa A: {sorted(hasil['hanya_a'])}")
    print(f"Menerima beasiswa B tetapi tidak A: {sorted(hasil['hanya_b'])}")
    print(f"Semua mahasiswa unik penerima beasiswa: {sorted(hasil['semua_unik'])}")


if __name__ == "__main__":
    main()
