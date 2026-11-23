# Kode Python Progres 1 - Kelompok 3

**Project:** Sistem Manajemen Distribusi dan Pengiriman Barang  
**Mata Kuliah:** Struktur Data (PIF251315)  
**Kelompok:** 3  
**Anggota:**
- MHD ICHSANUL AMIRULAH / 12550111538
- FAUZAN DJOHAN AKBAR / 12550111405

## Tujuan paket ini

Paket ini merupakan **prototype untuk Progres 1**, yang berfokus pada analisis kebutuhan, pemodelan entitas, rancangan awal OOP, dan alur menu CLI. Program ini memperlihatkan kelas Paket, Pelanggan, Kurir, Pengiriman, dan Lokasi serta operasi awal untuk menampilkan, menambahkan, mencari, dan mengubah status paket.

## Isi folder

- `main.py` - program CLI prototype dan pemeriksaan dasar.
- `models.py` - definisi kelas entitas menggunakan dataclass.
- `JALANKAN_PROGRAM.bat` - menjalankan program melalui Windows.

## Cara menjalankan melalui PowerShell

1. Jalankan:

```powershell
python main.py
```

Untuk pemeriksaan dasar:

```powershell
python main.py --self-test
```

Alternatif: klik dua kali `JALANKAN_PROGRAM.bat`.

## Menu prototype

1. Dashboard dan ringkasan data.
2. Tampilkan daftar paket.
3. Tambah paket.
4. Cari paket dengan penelusuran linear sementara.
5. Ubah status paket.
6. Tampilkan pelanggan.
7. Tampilkan kurir.
8. Tampilkan lokasi.
9. Lihat pemetaan tujuh struktur data yang direncanakan.
0. Keluar.