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

#==============
#Tambah Obat
#==============
def tambah_obat():
    print("┌────────────────────────────────────────┐")
    print("│             TAMBAH OBAT 📥             │")
    print("└────────────────────────────────────────┘")

    while True:

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

        try:
            kode = input("Masukkan kode obat (contoh: OB001): ")
        except KeyboardInterrupt:
            print("Jangan tekan Ctrl+C bro!. Silakan masukkan kode kembali.")
            continue

        if kode == "":
            print("Kode obat tidak boleh kosong.")
            continue

        kode_ditemukan = False
        for data in obat:
            if data["kode"] == kode:
                kode_ditemukan = True
                break

        if kode_ditemukan:
            print("Kode obat sudah digunakan.")
            continue

        break

    while True:
        try:
            nama = input("Masukkan nama obat: ")
        except KeyboardInterrupt:
            print("Jangan tekan Ctrl+C bro!. Silakan masukkan nama kembali.")
            continue

        if nama == "":
            print("Nama obat tidak boleh kosong.")
        else:
            break

    while True:
        try:
            harga = int(input("Masukkan harga obat: "))

            if harga > 0:
                break
            else:
                print("Harga harus lebih dari 0.")

        except ValueError:
            print("Harga harus berupa angka.")
            continue
        except KeyboardInterrupt:
            print("Jangan tekan Ctrl+C bro!")
            continue

    while True:
        try:
            stok = int(input("Masukkan stok obat: "))

            if stok <= 0:
                print("Stok tidak boleh nol atau negatif.")
                continue
        
            else:
                break
        except ValueError:
            print("Stok harus berupa angka.")
            continue
        except KeyboardInterrupt:
            print("Jangan tekan Ctrl+C bro!")
            continue

    while True:
        try:
            kedaluwarsa = input("Masukkan tanggal kedaluwarsa (DD-MM-YYYY): ")
        except KeyboardInterrupt:
            print("Jangan tekan Ctrl+C bro!")
            continue

        try:
            tanggal = datetime.strptime(kedaluwarsa, "%d-%m-%Y")
            kedaluwarsa = tanggal.strftime("%Y-%m-%d")
            break
        except ValueError:
            print("Format tanggal tidak valid. Gunakan format DD-MM-YYYY.")
            continue
        except KeyboardInterrupt:
            print("Jangan tekan Ctrl+C bro!")
            continue

    data_baru = {
        "kode": kode,
        "nama": nama,
        "harga": harga,
        "stok": stok,
        "kedaluwarsa": kedaluwarsa
    }

    obat.append(data_baru)
    simpan_data(file_obat, obat)

    print("Obat berhasil ditambahkan.")

#=================
#Edit Data Obat
#=================
def edit_obat():
    print("┌────────────────────────────────────────┐")
    print("│             EDIT DATA OBAT ⚙️          │")
    print("└────────────────────────────────────────┘")

    while True:

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

        try:
            kode = input("Masukkan kode obat yang ingin diedit: ")
        except KeyboardInterrupt:
            print("Jangan tekan Ctrl+C bro!")
            continue

        if kode == "":
            print("Kode obat tidak boleh kosong.")
            continue

        data_ditemukan = None
        for data in obat:
            if data["kode"] == kode:
                data_ditemukan = data
                break

        if data_ditemukan is not None:
            break

        print("Kode obat tidak ditemukan.")

    print(f"Nama obat saat ini: {data_ditemukan['nama']}")
    print(f"Harga saat ini: {data_ditemukan['harga']}")
    print(f"Stok saat ini: {data_ditemukan['stok']}")
    print(f"Kedaluwarsa saat ini: {data_ditemukan['kedaluwarsa']}")

    while True:
        try:
            nama_baru = input("Masukkan nama baru: ")
        except KeyboardInterrupt:
            print("Jangan tekan Ctrl+C bro!")
            continue

        if nama_baru == "":
            print("Nama obat tidak boleh kosong.")
        else:
            break

    while True:
        try:
            harga_baru = int(input("Masukkan harga baru: "))

            if harga_baru > 0:
                break
            else:
                print("Harga harus lebih dari 0.")

        except ValueError:
            print("Harga harus berupa angka.")
            continue
        except KeyboardInterrupt:
            print("Jangan tekan Ctrl+C bro!")
            continue

    while True:
        try:
            stok_baru = int(input("Masukkan stok baru: "))

            if stok_baru >= 0:
                break
            else:
                print("Stok tidak boleh negatif.")

        except ValueError:
            print("Stok harus berupa angka.")
            continue
        except KeyboardInterrupt:
            print("Jangan tekan Ctrl+C bro!")
            continue

    while True:
        try:
            tanggal_baru = input("Masukkan tanggal kedaluwarsa baru (DD-MM-YYYY): ")
        except KeyboardInterrupt:
            print("Jangan tekan Ctrl+C bro!")
            continue

        try:
            tanggal = datetime.strptime(tanggal_baru, "%d-%m-%Y")
            kedaluwarsa_baru = tanggal.strftime("%Y-%m-%d")
            break
        except ValueError:
            print("Format tanggal tidak valid. Gunakan format DD-MM-YYYY.")
            continue
        except KeyboardInterrupt:
            print("Jangan tekan Ctrl+C bro!")
            continue

    data_ditemukan["nama"] = nama_baru
    data_ditemukan["harga"] = harga_baru
    data_ditemukan["stok"] = stok_baru
    data_ditemukan["kedaluwarsa"] = kedaluwarsa_baru

    simpan_data(file_obat, obat)

    print("Data obat berhasil diperbarui.")
    time.sleep(1)
