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
        return data_awal

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

        nama = input("Masukkan nama lengkap: ")
        username = input("Masukkan username: ")
        password = pwinput.pwinput("Masukkan password: ")

        if nama == "" or username == "" or password == "":
            print("Semua data wajib diisi.")
            continue

        if len(username) < 4:
            print("Username minimal 4 karakter.")
            continue

        if len(password) < 6:
            print("Password minimal 6 karakter.")
            continue

        if username in akun:
            print("Username sudah digunakan.")
            continue

        akun[username] = {
            "nama": nama,
            "password": password,
            "role": "user",
            "saldo": 0
        }

        simpan_data(file_akun, akun)

        print("Registrasi berhasil!")
        print("Silakan login menggunakan akun yang telah dibuat.")
        return
    
#========
#Login
#========
def login():
    kesempatan = 3

    while kesempatan > 0:
        print("┌────────────────────────────────────────┐")
        print("│            LOGIN PENGGUNA 🔑           │")
        print("└────────────────────────────────────────┘")


        username = input("Masukkan username: ")
        password = pwinput.pwinput("Masukkan password: ")

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
                else:
                    print("Anda login sebagai Pelanggan.")

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

