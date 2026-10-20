"""Menghitung statistik nilai dan mengelompokkan nilai mahasiswa."""


def kategori_nilai(nilai):
    if not 0 <= nilai <= 100:
        raise ValueError("Nilai harus berada pada rentang 0 sampai 100.")
    if nilai >= 85:
        return "A"
    if nilai >= 75:
        return "B"
    if nilai >= 65:
        return "C"
    if nilai >= 50:
        return "D"
    return "E"


def analisis_nilai(nilai_mahasiswa):
    if not nilai_mahasiswa:
        raise ValueError("Daftar nilai tidak boleh kosong.")

    kelompok = {huruf: [] for huruf in "ABCDE"}
    for nilai in nilai_mahasiswa:
        kelompok[kategori_nilai(nilai)].append(nilai)

    return {
        "rata_rata": sum(nilai_mahasiswa) / len(nilai_mahasiswa),
        "tertinggi": max(nilai_mahasiswa),
        "terendah": min(nilai_mahasiswa),
        "kelompok": kelompok,
    }


def main():
    teks_nilai = input("Masukkan nilai (pisahkan dengan koma): ")
    try:
        nilai_mahasiswa = [float(nilai.strip()) for nilai in teks_nilai.split(",")]
        hasil = analisis_nilai(nilai_mahasiswa)
    except ValueError as error:
        print(f"Input tidak valid: {error}")
        return

    print(f"Rata-rata: {hasil['rata_rata']:.2f}")
    print(f"Nilai tertinggi: {hasil['tertinggi']:g}")
    print(f"Nilai terendah: {hasil['terendah']:g}")
    print("Kategori nilai:")
    for kategori, daftar_nilai in hasil["kelompok"].items():
        print(f"  {kategori}: {daftar_nilai}")


if __name__ == "__main__":
    main()
