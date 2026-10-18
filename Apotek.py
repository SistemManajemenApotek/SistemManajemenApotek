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


    kode = input("Masukkan kode obat: ")

    for data in obat:
        if data["kode"] == kode:
            print("Kode obat sudah digunakan.")
            return

    nama = input("Masukkan nama obat: ")

    try:
        harga = int(input("Masukkan harga obat: "))
        stok = int(input("Masukkan stok obat: "))

        if harga <= 0 or stok < 0:
            print("Harga harus lebih dari 0 dan stok tidak boleh negatif.")
            return

    except ValueError:
        print("Harga dan stok harus berupa angka.")
        return

    kedaluwarsa = input("Masukkan tanggal kedaluwarsa (YYYY-MM-DD): ")

    try:
        datetime.strptime(kedaluwarsa, "%Y-%m-%d")
    except ValueError:
        print("Format tanggal tidak valid.")
        return

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
    print("│             EDIT DATA OBAT  ⚙️          │")
    print("└────────────────────────────────────────┘")

    kode = input("Masukkan kode obat yang ingin diedit: ")

    for data in obat:
        if data["kode"] == kode:
            print(f"Nama obat saat ini: {data['nama']}")
            print(f"Harga saat ini: {data['harga']}")
            print(f"Stok saat ini: {data['stok']}")
            print(f"Kedaluwarsa saat ini: {data['kedaluwarsa']}")

            nama_baru = input("Masukkan nama baru: ")

            try:
                harga_baru = int(input("Masukkan harga baru: "))
                stok_baru = int(input("Masukkan stok baru: "))

                if harga_baru <= 0 or stok_baru < 0:
                    print("Harga harus lebih dari 0 dan stok tidak boleh negatif.")
                    return

            except ValueError:
                print("Harga dan stok harus berupa angka.")
                return

            kedaluwarsa_baru = input("Masukkan tanggal kedaluwarsa baru (YYYY-MM-DD): ")

            try:
                datetime.strptime(kedaluwarsa_baru, "%Y-%m-%d")
            except ValueError:
                print("Format tanggal tidak valid.")
                return

            data["nama"] = nama_baru
            data["harga"] = harga_baru
            data["stok"] = stok_baru
            data["kedaluwarsa"] = kedaluwarsa_baru

            simpan_data(file_obat, obat)

            print("Data obat berhasil diperbarui.")
            return

    print("Kode obat tidak ditemukan.")

#==================
#Hapus Data Obat
#==================
def hapus_obat():
    print("┌────────────────────────────────────────┐")
    print("│             HAPUS DATA OBAT  🗑️         │")
    print("└────────────────────────────────────────┘")

    kode = input("Masukkan kode obat yang ingin dihapus: ")

    for data in obat:
        if data["kode"] == kode:
            print(f"Kode obat: {data['kode']}")
            print(f"Nama obat: {data['nama']}")

            konfirmasi = input("Apakah Anda yakin ingin menghapus obat ini? (y/n): ")

            if konfirmasi == "y":
                obat.remove(data)
                simpan_data(file_obat, obat)
                print("Obat berhasil dihapus.")

            elif konfirmasi == "n":
                print("Penghapusan dibatalkan.")

            else:
                print("Pilihan tidak valid. Penghapusan dibatalkan.")

            return

    print("Kode obat tidak ditemukan.")

#=============
#Menu Admin
#=============
def menu_admin():
    while True:
        print("┌────────────────────────────────────────┐")
        print("│       ⚕️  MENU ADMIN APOTEK ⚕️           │")
        print("├────────────────────────────────────────┤")
        print("│ 1. Lihat Daftar Obat                   │")
        print("│ 2. Tambah Obat                         │")
        print("│ 3. Edit data obat                      │")
        print("│ 4. Hapus Obat                          │")
        print("│ 5. Riwayat Seluruh Transaksi           │")
        print("│ 6. Ringkasan Transaksi                 │")   
        print("│ 7. Logout                              │")                    
        print("└────────────────────────────────────────┘")

        try:
            pilihan = int(input("Pilih menu Admin: "))

            if pilihan == 1:
                lihat_obat()

            elif pilihan == 2:
                tambah_obat()

            elif pilihan == 3:
                edit_obat()

            elif pilihan == 4:
                hapus_obat()

            elif pilihan == 7:
                print("Logout berhasil.")
                break
                time.sleep(1)

            else:
                print("Pilihan tidak valid. Silakan pilih 1 sampai 7.")

        except ValueError:
            print("Input harus berupa angka.")

#=================
#Menu Pelanggan
#=================
def menu_pelanggan(username):
    while True:
        print("┌────────────────────────────────────────┐")
        print("│      ⚕️  MENU PELANGGAN APOTEK ⚕️        │")
        print("├────────────────────────────────────────┤")
        print("│ 1. Lihat Daftar Obat                   │")
        print("│ 2. Cek Saldo E-Money                   │")
        print("│ 3. Top up Saldo                        │")
        print("│ 4. Beli Obat                           │")
        print("│ 5. Riwayat Transaksi Saya              │")
        print("│ 6. Logout                              │")                     
        print("└────────────────────────────────────────┘")

        try:
            pilihan = int(input("Pilih menu Pelanggan: "))

            if pilihan == 1:
                lihat_obat()

            elif pilihan == 6:
                print("Logout berhasil.")
                break
                time.sleep(1)   

            else:
                print("Pilihan tidak valid. Silakan pilih 1 sampai 6.")

        except ValueError:
            print("Input harus berupa angka.")

#=============
#Menu Utama
#=============
def menu_utama():
    while True:
        print("┌────────────────────────────────────────┐")
        print("│      🏥 SISTEM MANAJEMEN APOTEK 🏥     │")
        print("├────────────────────────────────────────┤")
        print("│ 1. Login                               │")
        print("│ 2. Registrasi                          │")
        print("│ 3. Keluar                              │")
        print("└────────────────────────────────────────┘")

        try:
            pilihan = int(input("Pilih menu: "))

            if pilihan == 1:
                username, role = login()

                if role == "admin":
                    menu_admin()

                elif role == "user":
                    menu_pelanggan(username)

            elif pilihan == 2:
                registrasi()

            elif pilihan == 3:
                print("Terima kasih telah menggunakan Sistem Manajemen Apotek Kami🤗.")
                break

            else:
                print("Pilihan tidak valid. Silakan pilih 1, 2, atau 3.")

        except ValueError:
            print("Input harus berupa angka.")

#============================
#Menjalankan Program Utama
#============================
menu_utama()
