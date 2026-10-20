"""Analisis kalimat: kata, karakter, kata terpanjang, dan title case."""


def analisis_kalimat(kalimat):
    kata = kalimat.split()
    kata_terpanjang = max(kata, key=len) if kata else None
    return {
        "jumlah_kata": len(kata),
        "jumlah_karakter": len(kalimat),
        "kata_terpanjang": kata_terpanjang,
        "title_case": kalimat.title(),
    }


def main():
    kalimat = input("Masukkan sebuah kalimat: ")
    hasil = analisis_kalimat(kalimat)

    print(f"Jumlah kata: {hasil['jumlah_kata']}")
    print(f"Jumlah karakter (termasuk spasi): {hasil['jumlah_karakter']}")
    print(f"Kata terpanjang: {hasil['kata_terpanjang'] or '-'}")
    print(f"Kalimat dalam title case: {hasil['title_case']}")


if __name__ == "__main__":
    main()
