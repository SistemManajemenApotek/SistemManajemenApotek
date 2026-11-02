import json
import os
import pwinput
import time
from datetime import datetime
from prettytable import PrettyTable

os.system("cls")

role_akun = ("admin", "user")

file_akun = "akun.json"
file_obat = "obat.json"
file_transaksi = "transaksi.json"

#=================
#Muat Data JSON  
#=================
def muat_data(nama_file, data_awal):
    try:
        with open(nama_file, "r") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        with open(nama_file, "w") as file:
            json.dump(data_awal, file, indent=4)

        return data_awal

    except json.JSONDecodeError:
        print(f"File {nama_file} kosong atau format JSON tidak valid.")
        print("Periksa dan perbaiki isi file JSON tersebut.")
        raise

#======================
#Simpan Data ke JSON  
#======================
def simpan_data(nama_file, data):
    with open(nama_file, "w") as file:
        json.dump(data, file, indent=4)

akun = muat_data(file_akun, {})
obat = muat_data(file_obat, [])
transaksi = muat_data(file_transaksi, [])

#======================
#Regitrasi Pelanggan
#======================

def registrasi():
    while True:
        print("┌────────────────────────────────────────┐")
        print("│         REGISTRASI PELANGGAN📝         │")
        print("└────────────────────────────────────────┘")

        try:
            nama = input("Masukkan nama lengkap: ")

        except KeyboardInterrupt:
            print("Jangan tekan Ctrl+C bro!")
            continue

        while True:
            try:
                username = input("Masukkan username: ")

            except KeyboardInterrupt:
                print("Jangan tekan Ctrl+C bro!")
                continue

            if username in akun:
                print("Username sudah digunakan.")
                continue

            if len(username) < 4:
                print("Username minimal 4 karakter biar ga pendek-pendek amat.")
                continue

            #Keluar dari perulangan username jika valid
            break

        #Perulangan untuk input password
        while True:
            try:
                password = pwinput.pwinput("Masukkan password: ")

            except KeyboardInterrupt:
                print("Jangan tekan Ctrl+C bro!")
                continue

            if len(password) < 6:
                print("Password minimal 6 karakter biar aman.")
                continue

            #Keluar dari perulangan password jika valid
            break

        akun[username] = {
            "nama": nama,
            "password": password,
            "role": "user",
            "saldo": 0
        }

        simpan_data(file_akun, akun)

        print("Registrasi berhasil!")
        print("Silakan login menggunakan akun yang telah dibuat.")
        time.sleep(1)
        return

    print("Registrasi gagal.")
#========
#Login
#========
def login():
    kesempatan = 3

    while kesempatan > 0:
        print("┌────────────────────────────────────────┐")
        print("│            LOGIN PENGGUNA 🔑           │")
        print("└────────────────────────────────────────┘")


        try:
            username = input("Masukkan username: ")
            password = pwinput.pwinput("Masukkan password: ")

        except KeyboardInterrupt:
            print("Jangan tekan Ctrl+C bro!. Silakan masukkan username dan password kembali.")
            continue

        if username in akun:
            if password == akun[username]["password"]:
                role = akun[username]["role"]

                if role not in role_akun:
                    print("Role akun tidak valid.")
                    return None, None

                print("\nLogin berhasil!")
                print(f"Selamat datang, {akun[username]['nama']}!")

                if role == "admin":
                    print("Anda login sebagai Admin.")
                    time.sleep(1)
                else:
                    print("Anda login sebagai Pelanggan.")
                    time.sleep(1)

                return username, role

            else:
                print("Password salah.")

        else:
            print("Username tidak ditemukan.")

        kesempatan -= 1

        if kesempatan > 0:
            print(f"Sisa kesempatan login: {kesempatan}")
        else:
            print("Kesempatan login habis.")

    return None, None

#=============
#Lihat Obat
#=============
def lihat_obat():
    print("┌────────────────────────────────────────┐")
    print("│         💊 DAFTAR OBAT APOTEK 💊       │")
    print("└────────────────────────────────────────┘")

    if len(obat) == 0:
        print("Belum ada data obat.")
        return

    tabel = PrettyTable()
    tabel.field_names = [
        "Kode", "Nama Obat", "Harga", "Stok", "Kedaluwarsa"
    ]

    for data in obat:
        tabel.add_row([
            data["kode"],
            data["nama"],
            f"{data['harga']:,}".replace(',', '.'),
            data["stok"],
            data["kedaluwarsa"]
        ])

    print(tabel)
