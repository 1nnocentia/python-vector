from penjumlahan_vector import penjumlahan_vector
from pengurangan_vector import pengurangan_vector
from dot_product import dot_product
from panjang_vector import panjang_vector
from unit_vector import unit_vector
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
        print(f"Hasil penjumlahan Vektor A dan B adalah", penjumlahan_vector(a, b))

    elif pilihan == "2":
        a = list(map(int, input("Masukkan Vektor A : ").split(",")))
        b = list(map(int, input("Masukkan Vektor B : ").split(",")))
        print(f"Hasil pengurangan Vektor A dan B adalah", pengurangan_vector(a, b))

    elif pilihan == "3":
        a = list(map(int, input("Masukkan Vektor A : ").split(",")))
        b = list(map(int, input("Masukkan Vektor B : ").split(",")))
        print(f"Hasil perkalian Vektor A dan B adalah", dot_product(a, b))

    elif pilihan == "4":
        a = list(map(int, input("Masukkan Vektor A : ").split(",")))
        print(f"Hasil panjang Vektor A adalah", panjang_vector(a))

    elif pilihan == "5":
        a = list(map(int, input("Masukkan Vektor A : ").split(",")))
        print(f"Hasil unit Vector A adalah", unit_vector(a))
        
    else:
        print("Pilihan tidak valid.")
        time.sleep(1)
        continue

    lanjut = input("\nMau hitung lagi? (y/n) ").lower()
    if lanjut == "y":
        continue
    else:
        break
