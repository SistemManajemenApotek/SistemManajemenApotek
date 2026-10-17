import json
import os
import pwinput
import time
from datetime import datetime
from prettytable import PrettyTable 

def bersihkan_layar():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def muat_data(nama_file, data_awal):
    try:
        with open(nama_file, "r") as file:
            data = json.load(file)
            return data

    except FileNotFoundError:
        with open(nama_file, "w") as file:
            json.dump(data_awal,file, indent=4)
            time.sleep(1)

            return data_awal


def simpan_data(nama_file, data):
    with open(nama_file, "w") as file:
        json.dump(data, file, indent=4)
        time.sleep(1)

file_akun = "akun.json"
file_obat = "obat.json"
file_transaksi = "transaksi.json"

akun = muat_data(file_akun, {})
obat = muat_data(file_obat, [])
transaksi = muat_data(file_transaksi, [])

print("========================================")
print("       SISTEM MANAJEMEN APOTEK")
print("========================================")
print("Data akun, obat, dan transaksi berhasil dimuat.")
print(f"Jumlah akun: {len(akun)}")
print(f"Jumlah jenis obat: {len(obat)}")
print(f"Jumlah transaksi: {len(transaksi)}")