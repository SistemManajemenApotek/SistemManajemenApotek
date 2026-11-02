# PROJECT AKHIR KELOMPOK 5 SISTEM MANAJEMEN APOTEK GADA OBAT

Sistem Informasi Kelas B 26'

Anggota Kelompok dan Peran
1. Mirza Asra Ataya (2609116043): 
2. Laila Mufida (2609116046):
3. Muh. Faisal (2609116075):
4. Saniyyatul Aqilah (2609116080):

# DESKRIPSI DAN TUJUAN PROGRAM

## Deskripsi Program

Sistem Manajemen Apotek adalah program berbasis Python yang dibuat untuk membantu proses pengelolaan data obat dan transaksi pembelian di apotek. Program ini menyediakan dua jenis pengguna, yaitu admin dan pelanggan, yang memiliki hak akses berbeda sesuai dengan perannya.

Admin dapat mengelola data obat, seperti menambahkan, melihat, mengubah, dan menghapus data obat. Selain itu, admin dapat melihat riwayat transaksi serta rekapitulasi penjualan. Sementara itu, pelanggan dapat melihat daftar obat, melakukan registrasi dan login, mengisi saldo e-money, membeli obat menggunakan saldo yang tersedia, serta melihat informasi transaksi pembelian.

Program ini menggunakan file JSON untuk menyimpan data akun, data obat, dan riwayat transaksi agar data tetap tersedia ketika program dijalankan kembali. Program juga dilengkapi dengan validasi input dan penanganan error untuk membantu mencegah kesalahan selama penggunaan.

## Tujuan Program

Tujuan pembuatan Sistem Manajemen Apotek adalah:

1. Membantu pengelolaan data obat, termasuk informasi harga dan stok obat.
2. Mempermudah proses transaksi pembelian obat menggunakan saldo e-money.
3. Menerapkan pembagian hak akses antara admin dan pelanggan.
4. Menyimpan data akun, obat, dan transaksi agar dapat digunakan kembali.
5. Menerapkan konsep dasar pemrograman Python, seperti fungsi, percabangan, perulangan, list, tuple, dictionary, serta penanganan error.

# FLOWCHART

## Halaman Utama
<img width="2443" height="1690" alt="Flowchart PA Halaman Utama drawio" src="https://github.com/user-attachments/assets/b6d8bec9-afdf-4b50-988b-fb56d80a93d9" />

## Menu Admin
<img width="3533" height="3140" alt="Flowchart PA Menu Admin drawio(1)" src="https://github.com/user-attachments/assets/146d8674-a996-46e6-a044-fb8ace1c7256" />

## Menu Pelanggan
<img width="2786" height="2557" alt="Flowchart PA Menu Pelanggan drawio" src="https://github.com/user-attachments/assets/c0625c61-64a4-4795-94c8-6139aa6a47c1" />

# DAFTAR FITUR PER ROLE

## Fitur Menu Utama
1. Login
2. Registrasi
3. Keluar

## Fitur Role Admin

Admin memiliki akses untuk mengelola data obat dan melihat seluruh data transaksi pelanggan serta ringkasan penjualan apotek:
1. Lihat Obat
2. Tambah Obat
3. Edit Obat
4. Hapus Obat
5. Lihat Riwayat Transaksi (seluruh pelanggan)
6. Lihat Ringkasan Penjualan Apotek
7. Logout

## Fitur Role Pelanggan

Pelanggan memiliki akses untuk:
1. Lihat Daftar Obat
2. Cek Saldo E-Money
3. Top Up Saldo E-Money
4. Beli Obat
5. Lihat Riwayat Transaksi
6. Logout

# OUTPUT (MENU UTAMA, MENU ADMIN, MENU PELANGGAN) 

## Menu Utama

1. Tampilan menu utama dan login sebagai admin
<img width="322" height="302" alt="Screenshot 2026-10-29 145844" src="https://github.com/user-attachments/assets/72e235c8-22ae-4a8c-8c4f-b0eaf9f0865e" />

2. Tampilan menu utama dan registrasi akun baru
<img width="362" height="287" alt="Screenshot 2026-10-29 150116" src="https://github.com/user-attachments/assets/117f29b6-f49f-4b0d-aa85-546185ca00a7" />

3. Tampilan menu utama dan login sebagai pelanggan + percobaan jika salah memasukkan yang salaah
<img width="273" height="230" alt="Screenshot 2026-11-02 105219" src="https://github.com/user-attachments/assets/16a09bf2-15d2-47c4-ab86-0a31d9abd177" />

## Menu Admin

1. Tampilan menu admin
<img width="306" height="211" alt="Screenshot 2026-10-29 151527" src="https://github.com/user-attachments/assets/e375d677-e448-4d47-afd9-6505bbfb49f9" />

2. Tampilan menu admin 1 (Lihat Daftar Obat)
<img width="343" height="186" alt="Screenshot 2026-11-02 111339" src="https://github.com/user-attachments/assets/17bea19d-3622-40a0-892e-639cbb8a8a32" />

3. Tampilan menu admin 2 (Tambah Obat)
<img width="432" height="550" alt="Screenshot 2026-11-02 102408" src="https://github.com/user-attachments/assets/cab4a1e5-c9b8-44fa-bce1-90ffa32164a5" />

4. Tampilan menu admin 3 (Edit Data Obat)
<img width="317" height="565" alt="Screenshot 2026-11-02 103140" src="https://github.com/user-attachments/assets/594c8901-97d2-45ab-8477-ed265ac14773" />

5. Tampilan menu admin 4 (Hapus Data Obat)
<img width="346" height="457" alt="Screenshot 2026-11-02 103405" src="https://github.com/user-attachments/assets/dab9dd10-0972-47ec-ac63-0b19f07c336e" />

6. Tampilan menu admin 5 (Lihat Riwayat Transaksi Pelanggan)
<img width="577" height="677" alt="Screenshot 2026-11-02 103816" src="https://github.com/user-attachments/assets/750d3527-1ca7-4b53-a5e6-e1a5ee59f928" />

7. Tampilan menu admin 6 (Lihat Ringkasan Apotek)
<img width="277" height="270" alt="Screenshot 2026-11-02 104123" src="https://github.com/user-attachments/assets/03c53f11-946a-45bb-a7bd-6c4d7739fda9" />

8. Tampilan menu admin 7 (Logout)
<img width="272" height="301" alt="Screenshot 2026-11-02 104254" src="https://github.com/user-attachments/assets/72371749-8568-479c-beec-453f8fc3a5b1" />

## Tampilan Menu Pelanggan

1. Tampilan menu pelanggan
<img width="272" height="157" alt="Screenshot 2026-11-02 110139" src="https://github.com/user-attachments/assets/3ca34ef5-a2c3-4281-b8c9-60797ba582f4" />

2. Tampilan menu pelanggan 1 (Lihat Daftar Obat)
<img width="337" height="342" alt="Screenshot 2026-11-02 110201" src="https://github.com/user-attachments/assets/8f13c751-d7ca-4f22-8eb8-373c86b16857" />

3. Tampilan menu pelanggan 2 (Cek Saldo E-Money)
<img width="273" height="85" alt="Screenshot 2026-11-02 110303" src="https://github.com/user-attachments/assets/3dc0df36-96ff-4a3f-b4c8-7e51486c7e84" />

4. Tampilan menu pelanggan 3 (Top Up Saldo E-Money)
<img width="312" height="142" alt="Screenshot 2026-11-02 110933" src="https://github.com/user-attachments/assets/1be241a2-3589-4fe4-8411-8119c6c68d0c" />

5. Tampilan menu pelanggan 4 (Beli Obat)
<img width="345" height="590" alt="Screenshot 2026-11-02 111752" src="https://github.com/user-attachments/assets/5b21e968-ba3f-42bd-9a2c-a3e7e11c5fb8" />

6. Tampilan menu pelanggan 5 (Lihat Riwayat Transaksi)
<img width="566" height="127" alt="Screenshot 2026-11-02 112259" src="https://github.com/user-attachments/assets/11af5a99-72ed-488e-b623-cbbbea96d5b6" />

7. Tampilan menu pelanggan 6 (Logout)
<img width="272" height="286" alt="Screenshot 2026-11-02 112336" src="https://github.com/user-attachments/assets/e76ba2a2-4717-4223-ac06-9292e34bab44" />










