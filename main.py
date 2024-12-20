from vector_feature.penjumlahan_vektor import plus
from vector_feature.pengurangan_vector import pengurangan
from vector_feature.dot_product import dot_product
from vector_feature.panjang_vector import panjang_vektor
from vector_feature.unit_vector import unit_vector
import os
import time

while True:
    os.system("cls")
    print("=" * 36)
    print(f"{'Operasi Vektor':^36}")
    pilihan = input(f"{'=' * 36}\n1. Jumlahkan Vektor\n2. Pengurangan Vektor\n3. Dot Product\n4. Panjang Vektor\n5. Vektor Unit\n{'=' * 36}\nMasukkan Pilihan : ")
    print()

    if pilihan == "1":
        a = list(map(int, input("Masukkan Vektor A : ").split(",")))
        b = list(map(int, input("Masukkan Vektor B : ").split(",")))
        print(f"Hasil penjumlahan Vektor A dan B adalah", plus(a, b))

    elif pilihan == "2":
        a = list(map(int, input("Masukkan Vektor A : ").split(",")))
        b = list(map(int, input("Masukkan Vektor B : ").split(",")))
        print(f"Hasil pengurangan Vektor A dan B adalah", pengurangan(a, b))

    elif pilihan == "3":
        a = list(map(int, input("Masukkan Vektor A : ").split(",")))
        b = list(map(int, input("Masukkan Vektor B : ").split(",")))
        print(f"Hasil perkalian Vektor A dan B adalah", dot_product(a, b))

    elif pilihan == "4":
        a = list(map(int, input("Masukkan Vektor : ").split(",")))
        print(f"Hasil panjang Vektor adalah", round(panjang_vektor(a),2))

    elif pilihan == "5":
        a = list(map(int, input("Masukkan Vektor : ").split(",")))
        print(f"Hasil unit Vector adalah", unit_vector(a))
        
    else:
        print("Pilihan tidak valid.")
        time.sleep(1)
        continue

    lanjut = input("\nMau hitung lagi? (y/n) ").lower()
    if lanjut == "y":
        continue
    else:
        break
