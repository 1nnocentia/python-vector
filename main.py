from func_addition import plus
from func_subtraction import mines
from func_multiplication import times
from func_length import length
from func_unit import unit
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
        print(f"Hasil pengurangan Vektor A dan B adalah", mines(a, b))

    elif pilihan == "3":
        a = list(map(int, input("Masukkan Vektor A : ").split(",")))
        b = list(map(int, input("Masukkan Vektor B : ").split(",")))
        print(f"Hasil perkalian Vektor A dan B adalah", times(a, b))

    elif pilihan == "4":
        a = list(map(int, input("Masukkan Vektor A : ").split(",")))
        print(f"Hasil panjang Vektor A adalah", length(a))

    elif pilihan == "5":
        a = list(map(int, input("Masukkan Vektor A : ").split(",")))
        print(f"Hasil unit Vector A adalah", unit(a))
        
    else:
        print("Pilihan tidak valid.")
        time.sleep(1)
        continue

    lanjut = input("\nMau hitung lagi? (y/n) ").lower()
    if lanjut == "y":
        continue
    else:
        break
