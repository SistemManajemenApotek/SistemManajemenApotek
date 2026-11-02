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

#==================
#Hapus Data Obat
#==================
def hapus_obat():
    print("┌────────────────────────────────────────┐")
    print("│             HAPUS DATA OBAT  🗑️         │")
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
            kode = input("Masukkan kode obat yang ingin dihapus: ")
        except KeyboardInterrupt:
            print("Jangan tekan Ctrl+C bro!")
            continue

        data_ditemukan = None
        for data in obat:
            if data["kode"] == kode:
                data_ditemukan = data
                break

        if data_ditemukan is not None:
            break

        print("Kode obat tidak ditemukan. Silakan masukkan kembali.")

    print(f"Kode obat: {data_ditemukan['kode']}")
    print(f"Nama obat: {data_ditemukan['nama']}")

    try:
        konfirmasi = input("Apakah Anda yakin ingin menghapus obat ini? (y/n): ")
    except KeyboardInterrupt:
        print("Jangan tekan Ctrl+C bro!")
        return

    if konfirmasi == "y":
        obat.remove(data_ditemukan)
        simpan_data(file_obat, obat)
        print("Obat berhasil dihapus.")
        time.sleep(1)

    elif konfirmasi == "n":
        print("Penghapusan dibatalkan.")

    else:
        print("Pilihan tidak valid. Penghapusan dibatalkan.")

#====================
#Riwayat Transaksi
#====================
def riwayat_transaksi(username=None):
    print("┌────────────────────────────────────────┐")
    print("│          📜 RIWAYAT TRANSAKSI          │")
    print("└────────────────────────────────────────┘")

    tabel = PrettyTable()
    tabel.field_names = [
        "Kode Transaksi",
        "Pelanggan",
        "Nama Obat",
        "Jumlah",
        "Total",
        "Waktu"
    ]

    ada_transaksi = False

    for data in transaksi:
        if username is not None:
            if data["username"] != username:
                continue

        tabel.add_row([
            data["kode_transaksi"],
            data["nama_pelanggan"],
            data["nama_obat"],
            data["jumlah"],
            f"Rp{data['total']:,}".replace(",", "."),
            data["waktu"]
        ])

        ada_transaksi = True

    if ada_transaksi:
        print(tabel)
    else:
        print("Belum ada transaksi yang dapat ditampilkan.")

#============================
#Ringkasan Transaksi Admin
#============================
def rekap_transaksi():
    print("\n========== REKAP TRANSAKSI ==========")

    if len(transaksi) == 0:
        print("Belum ada transaksi yang tercatat.")
        return

    jumlah_transaksi = len(transaksi)
    total_pendapatan = 0
    total_obat_terjual = 0
    penjualan_obat = {}

    for data in transaksi:
        total_pendapatan += data["total"]
        total_obat_terjual += data["jumlah"]

        nama_obat = data["nama_obat"]

        if nama_obat in penjualan_obat:
            penjualan_obat[nama_obat] += data["jumlah"]
        else:
            penjualan_obat[nama_obat] = data["jumlah"]

    obat_terlaris = max(penjualan_obat, key=penjualan_obat.get)

    print(f"Jumlah transaksi : {jumlah_transaksi}")
    print(f"Total obat terjual: {total_obat_terjual}")
    print(
        f"Total pendapatan : Rp{total_pendapatan:,}"
        .replace(",", ".")
    )
    print(
        f"Obat terlaris    : {obat_terlaris} "
        f"({penjualan_obat[obat_terlaris]} unit)"
    )
    print("=====================================")

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

            elif pilihan == 5:
                riwayat_transaksi()

            elif pilihan == 6:
                rekap_transaksi()

            elif pilihan == 7:
                print("Logout berhasil.")
                break
                time.sleep(1)

            else:
                print("Pilihan tidak valid. Silakan pilih 1 sampai 7.")

        except ValueError:
            print("Input harus berupa angka.")
            continue
        except KeyboardInterrupt:
            print("Jangan tekan Ctrl+C bro!")
            continue

#========================
#Lihat Saldo Pelanggan
#========================
def lihat_saldo(username):
    print("┌────────────────────────────────────────┐")
    print("│           💳 SALDO PELANGGAN           │")
    print("├────────────────────────────────────────┤")
    print(f"Nama pelanggan: {akun[username]['nama']}")
    print(f"Saldo saat ini: Rp{akun[username]['saldo']:,}".replace(",", "."))
    print("└────────────────────────────────────────┘")
    time.sleep(1)   

#=========================
#Top Up Saldo Pelanggan
#=========================
def top_up(username):
    print("┌────────────────────────────────────────┐")
    print("│            💰 TOP UP SALDO             │")
    print("└────────────────────────────────────────┘")

    while True:
        try:
            jumlah = int(input("Masukkan jumlah top-up (Minimal Rp5000): Rp"))

            if jumlah <= 5000:
                print("Jumlah top-up harus lebih dari Rp5.000.")
                continue

            akun[username]["saldo"] += jumlah

            simpan_data(file_akun, akun)

            print("Top-up berhasil!")
            print(f"Saldo saat ini: Rp{akun[username]['saldo']:,}".replace(",", "."))
            time.sleep(1)
            break

        except ValueError:
            print("Jumlah top-up harus berupa angka.")
            continue
        except KeyboardInterrupt:
            print("Jangan tekan Ctrl+C bro!")
            continue

#=================
#Pembelian Obat
#=================
def beli_obat(username):
    print("┌────────────────────────────────────────┐")
    print("│          🛒 PEMBELIAN OBAT             │")
    print("└────────────────────────────────────────┘")
    lihat_obat()

    if len(obat) == 0:
        print("Belum ada obat yang tersedia.")
        return

    while True:
        try:
            kode_obat = input("Masukkan kode obat yang ingin dibeli : ")
        except KeyboardInterrupt:
            print("Jangan tekan Ctrl+C bro!")
            continue

        if kode_obat == "":
            print("Kode obat tidak boleh kosong.")
            continue

        index_obat = -1

        for i in range(len(obat)):
            if obat[i]["kode"] == kode_obat:
                index_obat = i
                break

        if index_obat == -1:
            print("Kode obat tidak ditemukan.")
            continue
        break
    
    while True:
        try:
            jumlah = int(input("Masukkan jumlah yang ingin dibeli: "))

        except ValueError:
            print("Jumlah pembelian harus berupa angka.")
            continue
        except KeyboardInterrupt:
            print("Jangan tekan Ctrl+C bro!")
            continue

        if jumlah <= 0:
            print("Jumlah pembelian harus lebih dari 0.")
            continue

        if jumlah > obat[index_obat]["stok"]:
            print("Stok obat tidak mencukupi.")
            continue
        break

    try:
        harga = obat[index_obat]["harga"]
        total = harga * jumlah
        waktu_transaksi = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if total > akun[username]["saldo"]:
            print("Saldo tidak mencukupi.")
            print(f"Total pembelian Anda: Rp{total:,}".replace(",", "."))
            print(f"Saldo Anda saat ini hanya: Rp{akun[username]['saldo']:,}".replace(",", "."))
            print("Silakan top-up saldo Anda terlebih dahulu.")
            return

        nomor_transaksi = len(transaksi) + 1
        kode_transaksi = f"TRX{nomor_transaksi:03d}"

        print("┌────────────────────────────────────────┐")
        print("│          🧾 INVOICE PEMBELIAN          │")
        print("├────────────────────────────────────────┤")
        print(  f"  Kode transaksi  : {kode_transaksi}")
        print(  f"  Tanggal         : {waktu_transaksi}")
        print(  f"  Nama obat       : {obat[index_obat]['nama']}")
        print(  f"  Harga satuan    : Rp{harga:,}".replace(",", "."))
        print(  f"  Jumlah          : {jumlah}")
        print(  f"  Total harga     : Rp{total:,}".replace(",", "."))
        print(  f"  Saldo setelah pembelian: "f"Rp{akun[username]['saldo'] - total:,}".replace(",", "."))
        print("└────────────────────────────────────────┘")
        time.sleep(1)

        konfirmasi = input("Lanjutkan pembayaran? (y/n): ")

        if konfirmasi != "y" and konfirmasi != "Y":
            print("Pembelian dibatalkan.")
            return

        akun[username]["saldo"] -= total
        obat[index_obat]["stok"] -= jumlah

        data_transaksi = {
            "kode_transaksi": kode_transaksi,
            "username": username,
            "nama_pelanggan": akun[username]["nama"],
            "kode_obat": obat[index_obat]["kode"],
            "nama_obat": obat[index_obat]["nama"],
            "harga": harga,
            "jumlah": jumlah,
            "total": total,
            "waktu": waktu_transaksi
        }

        transaksi.append(data_transaksi)

        simpan_data(file_akun, akun)
        simpan_data(file_obat, obat)
        simpan_data(file_transaksi, transaksi)

        print("\nPembelian berhasil!")
        print(f"Kode transaksi: {kode_transaksi}")
        print(f"Total pembayaran: Rp{total:,}".replace(",", "."))
        print(f"Sisa saldo: Rp{akun[username]['saldo']:,}".replace(",", "."))
        print(f"Sisa stok obat: {obat[index_obat]['stok']}")
        time.sleep(1)   

    except ValueError:
        print("Jumlah pembelian harus berupa angka.")

#=================
#Menu Pelanggan
#=================
def menu_pelanggan(username):
    while True:
        print("┌────────────────────────────────────────┐")
        print("│      ⚕️  MENU PELANGGAN APOTEK  ⚕️       │")
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

            elif pilihan == 2:
                lihat_saldo(username)

            elif pilihan == 3:
                top_up(username)

            elif pilihan == 4:
                beli_obat(username)

            elif pilihan == 5:
                riwayat_transaksi(username)

            elif pilihan == 6:
                print("Logout berhasil.")
                break
                time.sleep(1)   

            else:
                print("Pilihan tidak valid. Silakan pilih 1 sampai 6.")

        except ValueError:
            print("Input harus berupa angka.")
            continue
        except KeyboardInterrupt:
            print("Jangan tekan Ctrl+C bro!")
            continue

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
            continue
        except KeyboardInterrupt:
            print("Jangan tekan Ctrl+C bro!")
            continue

#============================
#Menjalankan Program Utama
#============================
menu_utama()
