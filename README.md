# PROJECT AKHIR KELOMPOK 5 SISTEM MANAJEMEN APOTEK OBAT CODING

**Sistem Informasi Kelas B 26'**

Anggota Kelompok dan Peran
1. Mirza Asra Ataya (2609116043): Konsep, Flowchart, Coding, Pengecekan, Laporan, README
2. Laila Mufida (2609116046): Konsep, Coding, Flowchart, Laporan, README
3. Muh. Faisal (2609116075): Konsep, Coding, Flowchart, Laporan, Readme
4. Saniyyatul Aqilah (2609116080): Coding, Flowchart, Laporan

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
Penjelasan alur flowchart menu utama.

1. **Menu Utama**: Program menampilkan tiga pilihan, yaitu Login, Registrasi, dan Keluar.
2. **Input Pilihan Menu Halaman Utama**: Pengguna memasukkan pilihan sesuai menu yang tersedia.
3. **Pemeriksaan Pilihan Menu**: Program memeriksa pilihan pengguna:
    * Jika memilih 1, program menjalankan proses login.
    * Jika memilih 2, program menjalankan proses registrasi.
    * Jika memilih 3, program menjalankan proses keluar dari sistem.
    * Jika pilihan tidak sesuai, program menampilkan pesan bahwa pilihan tidak valid dan kembali ke menu utama.
4. **Proses Login**: Pengguna diminta memasukkan username dan password.
5. **Proses Memeriksa Username dan Password**: Program memeriksa apakah data login sesuai dengan akun yang tersimpan.
6. **Pemeriksaan Kesesuaian Login**:
    * Jika username dan password tidak sesuai, program menampilkan pesan kesalahan dan menambah jumlah percobaan login.
    * Jika login berhasil, program melanjutkan pemeriksaan role akun.
7. **Pemeriksaan Batas Percobaan Login**: Jika login gagal sebanyak tiga kali, program menampilkan pesan bahwa batas percobaan telah tercapai, kemudian kembali ke menu utama. Jika belum mencapai tiga kali, pengguna dapat mencoba login kembali.
8. **Pemeriksaan Role Akun**: Setelah login berhasil, program memeriksa jenis akun pengguna.
9. **Pengalihan Menu Berdasarkan Role**:
    * Jika role akun adalah admin, program masuk ke Menu Admin.
    * Jika role akun adalah user, program masuk ke Menu Pelanggan.
10. **Proses Registrasi**: Jika pengguna memilih registrasi, program meminta nama lengkap, username, dan password sesuai ketentuan yang ditampilkan pada flowchart.
11. **Validasi Username**: Program memeriksa apakah username memenuhi minimal empat karakter dan belum digunakan. Jika tidak memenuhi, program menampilkan pesan kesalahan dan meminta input kembali.
12. **Validasi Password**: Program memeriksa apakah password memenuhi minimal enam karakter. Jika belum memenuhi, program meminta input kembali.
13. **Penyimpanan Akun Baru**: Jika seluruh validasi berhasil, program menyimpan data akun ke file JSON.
14. **Output Registrasi Berhasil**: Program menampilkan pesan bahwa registrasi berhasil.
15. **Menu Utama Kembali**: Setelah registrasi selesai, pengguna diarahkan kembali ke menu utama.
16. **Proses Keluar dari Sistem**: Jika pengguna memilih menu Keluar, program menampilkan pesan bahwa pengguna telah keluar dari sistem.
17. **End**: Program mengakhiri proses.


## Menu Admin
<img width="3533" height="3140" alt="Flowchart PA Menu Admin drawio(1)" src="https://github.com/user-attachments/assets/146d8674-a996-46e6-a044-fb8ace1c7256" />
Penjelasan Alur Flowchart Menu Admin

1. **Menu Admin**: Setelah login berhasil dan role akun teridentifikasi sebagai admin, program menampilkan menu admin.
2. **Input Pilihan Menu Admin**: Admin memilih salah satu dari tujuh pilihan yang tersedia.
3. **Pemeriksaan Pilihan Menu**: Program memeriksa pilihan admin dan menjalankan proses sesuai menu yang dipilih.

#### A. Menu 1: Lihat Daftar Obat
1. **Mengakses Data Obat**: Program membaca data obat dari file `obat.json`.
2. **Memproses Data Obat**: Program mengambil data obat yang tersimpan.
3. **Output Daftar Obat**: Program menampilkan daftar obat beserta informasi yang tersedia.
4. **Kembali ke Menu Admin**: Setelah daftar obat ditampilkan, admin dapat memilih menu lainnya.

#### B. Menu 2: Tambah Data Obat
1. **Input Kode Obat**: Admin memasukkan kode untuk obat yang akan ditambahkan.
2. **Validasi Kode Obat**: Program memeriksa apakah kode obat sudah digunakan dan tidak boleh kosong. Jika kode tidak valid, program menampilkan pesan kesalahan dan meminta input kembali.
3. **Input Nama Obat**: Admin memasukkan nama obat. Jika nama kosong, program meminta input kembali.
4. **Input Harga Obat**: Admin memasukkan harga obat yang harus lebih dari nol. Jika tidak valid, program meminta input kembali.
5. **Input Stok Obat**: Admin memasukkan jumlah stok yang harus memenuhi ketentuan pada flowchart, yaitu tidak boleh negatif.
6. **Input Tanggal Kedaluwarsa**: Admin memasukkan tanggal kedaluwarsa dengan format DD-MM-YYYY.
7. **Validasi Format Tanggal**: Program memeriksa apakah format tanggal sesuai. Jika tidak sesuai, admin diminta memasukkan tanggal kembali.
8. **Proses Tambah Data Obat**: Jika semua input valid, program menambahkan data obat baru.
9. **Penyimpanan Data**: Data obat disimpan ke file `obat.json`.
10. **Output Obat Berhasil Ditambahkan**: Program menampilkan pesan keberhasilan dan kembali ke Menu Admin.

#### C. Menu 3: Ubah Data Obat
1. **Input Kode Obat yang Ingin Diubah**: Admin memasukkan kode obat yang datanya ingin diperbarui.
2. **Validasi Kode Obat**: Program memeriksa apakah kode obat ditemukan. Jika tidak ditemukan, program menampilkan pesan kesalahan dan meminta kode kembali.
3. **Input Nama Obat Baru**: Admin memasukkan nama obat baru. Nama tidak boleh kosong.
4. **Input Harga Baru**: Admin memasukkan harga baru yang harus lebih dari nol.
5. **Input Stok Baru**: Admin memasukkan stok baru sesuai ketentuan, yaitu tidak boleh negatif.
6. **Input Tanggal Kedaluwarsa Baru**: Admin memasukkan tanggal kedaluwarsa dengan format DD-MM-YYYY.
7. **Validasi Tanggal**: Program memeriksa format tanggal. Jika tidak sesuai, admin diminta memasukkan tanggal kembali.
8. **Proses Perubahan Data**: Program memperbarui informasi obat berdasarkan kode yang dipilih.
9. **Penyimpanan Data**: Perubahan disimpan ke `obat.json`.
10. **Output Obat Berhasil Diperbarui**: Program menampilkan pesan keberhasilan dan kembali ke Menu Admin.

#### D. Menu 4: Hapus Data Obat
1. **Input Kode Obat yang Ingin Dihapus**: Admin memasukkan kode obat yang ingin dihapus.
2. **Validasi Kode Obat**: Program memeriksa apakah kode obat ditemukan. Jika tidak ditemukan, program menampilkan pesan kesalahan.
3. **Output Tampilan Detail Obat**: Jika kode ditemukan, program menampilkan detail obat yang akan dihapus.
4. **Konfirmasi Penghapusan**: Admin diminta mengonfirmasi penghapusan dengan pilihan y/n.
5. **Pemeriksaan Konfirmasi**:
   - Jika admin memilih `y`, program melanjutkan proses penghapusan.
   - Jika admin memilih `n`, penghapusan dibatalkan dan program kembali ke Menu Admin.
6. **Proses Menghapus Data Obat**: Program menghapus data obat yang dipilih.
7. **Penyimpanan Data**: Perubahan disimpan ke `obat.json`.
8. **Output Obat Berhasil Dihapus**: Program menampilkan pesan keberhasilan dan kembali ke Menu Admin.

#### E. Menu 5: Lihat Riwayat Transaksi
1. **Mengakses Data Transaksi**: Program membaca data transaksi dari file `transaksi.json`.
2. **Pemeriksaan Ketersediaan Transaksi**: Program memeriksa apakah terdapat data transaksi.
3. **Jika Tidak Ada Transaksi**: Program menampilkan pesan bahwa belum ada transaksi, kemudian kembali ke Menu Admin.
4. **Jika Ada Transaksi**: Program menampilkan seluruh riwayat transaksi yang tersimpan.
5. **Kembali ke Menu Admin**: Setelah riwayat ditampilkan, admin dapat memilih menu lainnya.

#### F. Menu 6: Lihat Ringkasan Apotek
1. **Mengakses Data Transaksi**: Program membaca data transaksi yang tersimpan.
2. **Pemeriksaan Ketersediaan Transaksi**: Program memeriksa apakah data transaksi tersedia.
3. **Jika Tidak Ada Transaksi**: Program menampilkan pesan bahwa belum ada transaksi, kemudian kembali ke Menu Admin.
4. **Jika Ada Transaksi**: Program melanjutkan proses perhitungan ringkasan penjualan.
5. **Proses Menghitung Pendapatan**: Program menghitung total pendapatan berdasarkan transaksi yang tercatat.
6. **Proses Menghitung Jumlah Penjualan**: Program menghitung jumlah penjualan setiap obat berdasarkan data transaksi.
7. **Proses Menentukan Obat Terlaris**: Program menentukan obat yang paling banyak terjual.
8. **Output Ringkasan Apotek**: Program menampilkan hasil ringkasan, seperti pendapatan, jumlah penjualan, dan obat terlaris.
9. **Kembali ke Menu Admin**: Setelah ringkasan ditampilkan, admin dapat memilih menu lainnya.

#### G. Menu 7: Logout
1. **Proses Logout Admin**: Program menjalankan proses keluar dari akun admin.
2. **Output Logout Berhasil**: Program menampilkan pesan bahwa logout berhasil.
3. **Kembali ke Menu Halaman Utama**: Admin diarahkan kembali ke halaman utama untuk login kembali, melakukan registrasi, atau keluar dari sistem.

---

# Penjelasan Alur Flowchart Menu Pelanggan

<img width="2786" height="2557" alt="Flowchart PA Menu Pelanggan drawio" src="https://github.com/user-attachments/assets/c0625c61-64a4-4795-94c8-6139aa6a47c1" />
Penjelasan alur flowchart menu pelanggan

1. **Menu Pelanggan**: Setelah login berhasil dan role akun teridentifikasi sebagai pelanggan, program menampilkan menu pelanggan.
2. **Input Pilihan Menu Pelanggan**: Pelanggan memilih salah satu dari enam pilihan yang tersedia.
3. **Pemeriksaan Pilihan Menu**: Program memeriksa pilihan pelanggan dan menjalankan proses sesuai menu yang dipilih.

#### A. Menu 1: Lihat Daftar Obat
1. **Mengakses Data Obat**: Program membaca data obat dari file `obat.json`.
2. **Memproses Data Obat**: Program mengambil informasi obat yang tersimpan.
3. **Output Daftar Obat**: Program menampilkan daftar obat beserta informasi yang tersedia.
4. **Kembali ke Menu Pelanggan**: Setelah daftar obat ditampilkan, pelanggan dapat memilih menu lainnya.

#### B. Menu 2: Cek Saldo E-Money
1. **Mengakses Data Akun**: Program membaca data akun dari file `akun.json`.
2. **Memproses Data Saldo**: Program mengambil saldo dari akun pelanggan yang sedang login.
3. **Output Saldo E-Money**: Program menampilkan jumlah saldo yang dimiliki pelanggan.
4. **Kembali ke Menu Pelanggan**: Setelah saldo ditampilkan, pelanggan dapat memilih menu lainnya.

#### C. Menu 3: Top-Up Saldo
1. **Mengakses Data Akun**: Program membaca data akun pelanggan dari `akun.json`.
2. **Input Nominal Top-Up**: Pelanggan memasukkan nominal saldo yang ingin ditambahkan.
3. **Validasi Nominal Top-Up**: Program memeriksa apakah nominal top-up memenuhi ketentuan (nominal harus lebih dari nol).
4. **Jika Nominal Tidak Valid**: Program menampilkan pesan bahwa nominal top-up tidak valid, kemudian meminta input kembali.
5. **Jika Nominal Valid**: Program melanjutkan proses penambahan saldo.
6. **Proses Menyimpan Saldo**: Program menambahkan nominal top-up ke saldo pelanggan.
7. **Penyimpanan Data Akun**: Saldo terbaru disimpan ke file `akun.json`.
8. **Output Saldo Berhasil Ditambah**: Program menampilkan informasi bahwa saldo berhasil ditambahkan.
9. **Kembali ke Menu Pelanggan**: Setelah top-up selesai, pelanggan dapat memilih menu lainnya.

#### D. Menu 4: Beli Obat
1. **Mengakses Data Obat**: Program membaca daftar obat dari `obat.json`.
2. **Output Daftar Obat**: Program menampilkan obat yang tersedia untuk dibeli.
3. **Input Kode Obat**: Pelanggan memasukkan kode obat yang ingin dibeli.
4. **Validasi Kode Obat**: Program memeriksa apakah kode obat ditemukan. Jika tidak ditemukan, program menampilkan pesan kesalahan dan meminta kode kembali.
5. **Input Jumlah Obat**: Pelanggan memasukkan jumlah obat yang ingin dibeli.
6. **Validasi Jumlah Pembelian**: Program memeriksa apakah jumlah yang dimasukkan lebih dari nol. Jika tidak valid, pelanggan diminta memasukkan jumlah kembali.
7. **Pemeriksaan Ketersediaan Stok**: Program memeriksa apakah stok obat mencukupi untuk jumlah pembelian.
8. **Jika Stok Tidak Mencukupi**: Program menampilkan pesan bahwa stok tidak mencukupi dan meminta pelanggan memasukkan jumlah kembali.
9. **Jika Stok Mencukupi**: Program melanjutkan proses perhitungan transaksi.
10. **Proses Menghitung Total Harga**: Program menghitung total harga berdasarkan harga satuan dan jumlah obat yang dibeli.
11. **Pemeriksaan Saldo Pelanggan**: Program memeriksa apakah saldo pelanggan mencukupi untuk membayar total pembelian.
12. **Jika Saldo Tidak Mencukupi**: Program menampilkan pesan bahwa saldo tidak mencukupi dan mengarahkan pelanggan kembali ke Menu Pelanggan.
13. **Jika Saldo Mencukupi**: Program mengurangi saldo pelanggan dan stok obat sesuai jumlah pembelian.
14. **Penyimpanan Transaksi**: Program menyimpan data pembelian ke `transaksi.json` serta menyimpan perubahan saldo ke `akun.json` dan stok ke `obat.json`.
15. **Output Invoice**: Program menampilkan rincian pembelian sebagai invoice (kode transaksi, tanggal pembelian, nama obat, harga satuan, jumlah, dan total harga).
16. **Kembali ke Menu Pelanggan**: Setelah transaksi selesai, pelanggan dapat memilih menu lainnya.

#### E. Menu 5: Riwayat Transaksi
1. **Mengakses Data Transaksi**: Program membaca data transaksi dari `transaksi.json`.
2. **Memproses Data Transaksi**: Program mengambil riwayat transaksi yang tersimpan.
3. **Memfilter Transaksi Berdasarkan Username**: Program menyaring data agar hanya menampilkan transaksi milik pelanggan yang sedang login.
4. **Pemeriksaan Ketersediaan Transaksi**: Program memeriksa apakah pelanggan memiliki riwayat transaksi.
5. **Jika Belum Ada Transaksi**: Program menampilkan pesan bahwa pelanggan belum memiliki transaksi.
6. **Jika Ada Transaksi**: Program menampilkan riwayat transaksi milik pelanggan tersebut.
7. **Kembali ke Menu Pelanggan**: Setelah riwayat ditampilkan, pelanggan dapat memilih menu lainnya.

#### F. Menu 6: Logout
1. **Proses Logout Pelanggan**: Program menjalankan proses keluar dari akun pelanggan.
2. **Output Logout Berhasil**: Program menampilkan pesan bahwa logout berhasil.
3. **Kembali ke Menu Halaman Utama**: Pelanggan diarahkan kembali ke halaman utama.

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

1. **Tampilan menu utama dan login sebagai admin**
<img width="322" height="302" alt="Screenshot 2026-10-29 145844" src="https://github.com/user-attachments/assets/72e235c8-22ae-4a8c-8c4f-b0eaf9f0865e" />

Pada tampilann ini admin melakukan login menggunakan akun yang telah dibuat dengan memasukkan username dan password setelah diverifikasi dan cocok maka sistem menampilkan "Loginn  berhasil! selamat datang admin."  

2. **Tampilan menu utama dan registrasi akun baru**
<img width="362" height="287" alt="Screenshot 2026-10-29 150116" src="https://github.com/user-attachments/assets/117f29b6-f49f-4b0d-aa85-546185ca00a7" />

Pada tampilan ini penggguna memilih opsi registrasi, memasukkan nama, username serta password dan sistem menyatakan "Registrasi berhasil!, silahkan login menggunakan akun yang telah di buat".

3. **Tampilan menu utama dan login sebagai pelanggan + percobaan jika salah memasukkan yang salah**
<img width="273" height="230" alt="Screenshot 2026-11-02 105219" src="https://github.com/user-attachments/assets/16a09bf2-15d2-47c4-ab86-0a31d9abd177" />

Pada tampilan ini pengguna memasukkan username dan password sebagai pelanggan. ketika pelanggan salah memasukkan username atau password pelanggan memiliki kesempatan sebanyak 3x untuk memperbaikinya setelah itu sistem menampilkan pesan "login berhasil! selamat datang (pengguna).Anda login sebagai pelanggan"

## Menu Admin

1. **Tampilan menu admin**
<img width="306" height="211" alt="Screenshot 2026-10-29 151527" src="https://github.com/user-attachments/assets/e375d677-e448-4d47-afd9-6505bbfb49f9" />

Pada tampilan menu admin diberikan beberapa pilihan yaitu lihat daftar obat, tambah obat, edit data obat, hapus obat, riwayat seluruh transaksi, ringkasan transaksi dan keluar.

2. **Tampilan menu admin 1 (Lihat Daftar Obat)**
<img width="343" height="186" alt="Screenshot 2026-11-02 111339" src="https://github.com/user-attachments/assets/17bea19d-3622-40a0-892e-639cbb8a8a32" />

Jika admin memilih menu 1 (lihat daftar obat) maka sistem akan menampilkan data obat yang telah tersedia.  Data tersebut mennampilkan kode obat, nama obat, harga, stok dan kadaluwarsa.

3. **Tampilan menu admin 2 (Tambah Obat)**
<img width="432" height="550" alt="Screenshot 2026-11-02 102408" src="https://github.com/user-attachments/assets/cab4a1e5-c9b8-44fa-bce1-90ffa32164a5" />

Jika admin memilih menu 2 (tambah obat). Admin dapat memasukkan kode obat, nama obat, harga, stok dan kadaluwarsa. Dengan syarat nama obat tidak boleh kosong, harga harus lebih dari nol dan harus berupa angka, stok tidak boleh nol atau negatif dan harus berupa angka dan tanggal kedaluwarsa harus sesuai format yaitu dd-mm-yyyy. Jika semua syarat telah terpenuhi maka sistem akan menampilkan pesan “obat berhasil di tambahkan”.

4. **Tampilan menu admin 3 (Edit Data Obat)**
<img width="317" height="565" alt="Screenshot 2026-11-02 103140" src="https://github.com/user-attachments/assets/594c8901-97d2-45ab-8477-ed265ac14773" />

Jika admin memilih menu 3 (edit data obat). Admin harus memasukkan kode obat yang ingin di edit lalu memasukkan nama baru, harga baru, stok baru dan  tanggal kedaluwarsa baru. Dengan syarat nama obat tidak boleh kosong, harga harus lebih dari nol dan harus berupa angka, stok tidak boleh nol atau negatif dan harus berupa angka dan tanggal kedaluwarsa harus sesuai format yaitu dd-mm-yyyy. Jika semua syarat telah terpenuhi maka sistem akan pesan “data obat berhasil di perbarui”.

5. **Tampilan menu admin 4 (Hapus Data Obat)**
<img width="346" height="457" alt="Screenshot 2026-11-02 103405" src="https://github.com/user-attachments/assets/dab9dd10-0972-47ec-ac63-0b19f07c336e" />

Jika admin memilih menu 4 (hapus data obat). Admin harus memasukkan kode obat yang ingin di hapus sesuai dengan kode obat yang telah tersedia jika kode obat tidak tersedia maka sistem akan menampilkan pesan “Kode obat tidak di temukan. Silahkan masukkan Kembali”. Jika kode obbat sesuai maka admin dapat memasukkan kode dan nama obat. Lalu sistem akan menanyakan “apakah anda yakin ingin menghapus obat ini ? (y/n)” jika (y) maka akan menampilkan pesan “obat berhasil di hapus” dan jika (n) maka akan Kembali ke menu admin.

6. **Tampilan menu admin 5 (Lihat Riwayat Transaksi Pelanggan)**
<img width="577" height="677" alt="Screenshot 2026-11-02 103816" src="https://github.com/user-attachments/assets/750d3527-1ca7-4b53-a5e6-e1a5ee59f928" />

Ketika admin memilih 0  maka sistem akan menampilkan “pilihan tidak valid. Silahkan pilih 1 sampai 7”. Dan jika admin tidak memasukkan pilihan apapun maka sistem akan menampilkan pesan “input harus berupa angka”. Jika admin memilih menu 5 (lihat Riwayat transaksi pembeli ). Maka sistem akan menampilkan Riwayat transaksi pelanggan yang isinya kode transaksi, pelanggan, nama obat, jumlah, total dan waaktu.

7. **Tampilan menu admin 6 (Lihat Ringkasan Apotek)**
<img width="277" height="270" alt="Screenshot 2026-11-02 104123" src="https://github.com/user-attachments/assets/03c53f11-946a-45bb-a7bd-6c4d7739fda9" />

Jika admin memilih menu 6 (lihat ringkasan apotek). Maka sistem akan menampilkan rekap transaksi yang isinya yaitu jumlah transaksi, total obat terjual, total pendapatan, obat terlaris.

8. **Tampilan menu admin 7 (Logout)**
<img width="272" height="301" alt="Screenshot 2026-11-02 104254" src="https://github.com/user-attachments/assets/72371749-8568-479c-beec-453f8fc3a5b1" />

Jika admin memilih menu 7 (logout). Maka sistem akan menampilkan pesan “logout berhasil”. Dan admin akan Kembali ke menu utama.

## Tampilan Menu Pelanggan

1. **Tampilan menu pelanggan**
<img width="272" height="157" alt="Screenshot 2026-11-02 110139" src="https://github.com/user-attachments/assets/3ca34ef5-a2c3-4281-b8c9-60797ba582f4" />

Pada tampilan menu pelanggan terdapat beberapa menu pilihan yaitu lihat daftar obat, cek saldo E-Money, top up saldo, beli obat, Riwayat transaksi saya, logout. 

2. **Tampilan menu pelanggan 1 (Lihat Daftar Obat)**
<img width="337" height="342" alt="Screenshot 2026-11-02 110201" src="https://github.com/user-attachments/assets/8f13c751-d7ca-4f22-8eb8-373c86b16857" />

Jika pelanggan memilih menu 1 (lihat daftar obat). maka sistem akan menampilkan data obat yang telah tersedia.  Data tersebut mennampilkan kode obat, nama obat, harga, stok dan kadaluwarsa.

3. **Tampilan menu pelanggan 2 (Cek Saldo E-Money)**
<img width="273" height="85" alt="Screenshot 2026-11-02 110303" src="https://github.com/user-attachments/assets/3dc0df36-96ff-4a3f-b4c8-7e51486c7e84" />

Jika pelanggan memilih menu 2 (cek saldo E-Money). Maka sistem akan menampilkan saldo pelanggan yang isinya ada Nama pelanggan dan saldo saat ini 

4. **Tampilan menu pelanggan 3 (Top Up Saldo E-Money)**
<img width="312" height="142" alt="Screenshot 2026-11-02 110933" src="https://github.com/user-attachments/assets/1be241a2-3589-4fe4-8411-8119c6c68d0c" />

Jika pelanggan memilih menu 3 (Top Up Saldo E-Money). Maka sistem akan menampilkan  menu Top Up saldo yang isinya “masukkan jumlah top-up  (minimal Rp.5000)”. Jika jumlah top-up tidak lebih dari 5000 maka sistem akan menampilkan pesan “jumlah top-up harus lebih dari Rp.5000. Ketika pelanggan memasukkan bukan berupa angka maka sistem akan menampilkan pesan “jumlah top-up harus berupa angka”. Selanjutnya kalau pelanggan telah memenuhi syarat tadi maka sistem akan menampilkan pesan “top-up berhasil!. Dan menampilkan jumlah saldo saat ini.

5. **Tampilan menu pelanggan 4 (Beli Obat)**
<img width="345" height="590" alt="Screenshot 2026-11-02 111752" src="https://github.com/user-attachments/assets/5b21e968-ba3f-42bd-9a2c-a3e7e11c5fb8" />

Jika pelanggan memilih menu 4 (beli obat). Maka sistem akan menampilkan daftar obat apotek yang tersedia lalu pelanggan dapat memasukkan  kode obat yang ingin dibeli, ketika pelanggan memasukkan kode obat yang tidak sesuai maka sistem akan menampilkan pesan “kode obat tidak di temukan”. Dan Ketika pelanggan tidak memasukkan kode obat sama sekali maka sistem akan menampilkan pesan “kode obat tidak boleh kosong”. Jika pelanggan memasukkan jumlah yang ingin dibeli 0, maka sistem akan menampilkan pesan “Jumlah pembelian harus lebih dari 0” dan jika pelanggan tidak memasukkan jumlah yang ingin dibeli maka sistem akan menampilkan pesan “Jumlah Pemberian harus berupa angka”. Jika semua syarat sudah sesuai dan pelanggan memasukkan jumlah yang benar maka sistem akan menampilkan invoice pembelian yang berisi kode transaksi, tanggal, nama obat, harga satuan, jumlah, total harga, saldo setelah pembelian. Selanjutnya sistem akan memastikan dengan pesan “Lanjutkan pembayaran (y/n):”. Jika pelanggan memilih (y) maka sistem akan menampilkan pesan “Pembelian berhasil!” dan menampilkan kode transaksi, total pembayaran, sisa saldo, dan sisa stok obat.

6. **Tampilan menu pelanggan 5 (Lihat Riwayat Transaksi)**
<img width="566" height="127" alt="Screenshot 2026-11-02 112259" src="https://github.com/user-attachments/assets/11af5a99-72ed-488e-b623-cbbbea96d5b6" />

Jika pelanggan memilih menu 5 (Lihat Riwayat Transaksi). Maka sistem akan menampilkan Riwayat transaksi yang berisi kode transaksi, pelanggan, nama obat, jumlah, total, dan waktu.

7. **Tampilan menu pelanggan 6 (Logout)**
<img width="272" height="286" alt="Screenshot 2026-11-02 112336" src="https://github.com/user-attachments/assets/e76ba2a2-4717-4223-ac06-9292e34bab44" />

Jika pelanggan memilih menu 6 (logout). Maka sistem akan menampilkan pesan “Logout berhasil!” dan pelanggan akan Kembali ke menu utama.










