"""Menganalisis frekuensi kata dalam file teks."""

import re
import sys
from collections import Counter
from pathlib import Path


def analisis_teks(teks):
    kata = re.findall(r"[^\W_]+(?:['’][^\W_]+)*", teks.lower(), flags=re.UNICODE)
    frekuensi = Counter(kata)
    total_kata = len(kata)
    total_unik = len(set(kata))
    kata_sekali = {kata_item for kata_item, jumlah in frekuensi.items() if jumlah == 1}

    return {
        "frekuensi": frekuensi,
        "sepuluh_teratas": sorted(frekuensi.items(), key=lambda item: (-item[1], item[0]))[:10],
        "kata_sekali": kata_sekali,
        "rasio_type_token": total_unik / total_kata if total_kata else 0.0,
        "total_kata": total_kata,
        "total_unik": total_unik,
    }


def main():
    if len(sys.argv) > 2:
        print("Penggunaan: python latihan5_analisis_teks.py [nama_file.txt]")
        return

    nama_file = sys.argv[1] if len(sys.argv) == 2 else input("Masukkan path file teks: ").strip()
    try:
        teks = Path(nama_file).read_text(encoding="utf-8")
    except (OSError, UnicodeError) as error:
        print(f"Gagal membaca file '{nama_file}': {error}")
        return

    hasil = analisis_teks(teks)
    print(f"Total kata: {hasil['total_kata']}")
    print(f"Total kata unik: {hasil['total_unik']}")
    print("10 kata paling sering muncul:")
    if hasil["sepuluh_teratas"]:
        for kata, jumlah in hasil["sepuluh_teratas"]:
            print(f"  {kata}: {jumlah}")
    else:
        print("  (tidak ada kata)")
    print(f"Kata yang hanya muncul sekali: {sorted(hasil['kata_sekali'])}")
    print(f"Type-token ratio: {hasil['rasio_type_token']:.4f}")


if __name__ == "__main__":
    main()
