# Kalkulator konsol di Python
# Made by A.R Dilfa Programs

# meng-import library
import colorama # untuk warna teks judul aplikasi dan pembuat
from colorama import Fore, Back, Style # untuk warna teks
colorama.init

def jalankan_kalkulator():

    # teks judul aplikasi, dan pembuat
    print(Fore.GREEN + "******** PROGRAM KALKULATOR KONSOL ********")
    print(Fore.GREEN + "************ BY AIMAR R. DILFA ************")

    # balikkan warna teks ke putih
    print(Fore.WHITE)

    # Pemasukkan data operasi hitung kalkulator
    operasi_hitung = input("Masukkan operasi hitung (+,-,/,*): ")

    # Masukkan nomor kesatu dan kedua
    nomor_1 = float(input("Masukkan nomor kesatu: "))
    nomor_2 = float(input("Masukkan nomor kedua: "))

    # Pengeluaran data input kalkulator
    if operasi_hitung == "+":
        hasil = nomor_1 + nomor_2
        print(hasil)
    elif operasi_hitung == "-":
        hasil = nomor_1 - nomor_2
        print(hasil)
    elif operasi_hitung == "/":
        hasil = nomor_1 / nomor_2
        print(hasil)
    elif operasi_hitung == "*":
        hasil = nomor_1 * nomor_2
        print(hasil)
    else:
        print(f"{operasi_hitung} bukanlah sebuah operasi hitung.")

    # sebuah spasi antara pertanyaan mulai lagi
    print()

# pertanyaan untuk mulai lagi atau tidak.
while True:
    jalankan_kalkulator()
    jalankan_ulang = input(Fore.BLUE + "Mulai lagi? (Y/T): ")
    print(Fore.WHITE)
    if jalankan_ulang.lower() != 'y':
        break

# jika program tidak ingin mulai lagi lalu exit.
print("Program selesai digunakan.")
input()