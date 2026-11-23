"""Prototype Progres 1 - Sistem Manajemen Distribusi dan Pengiriman Barang.

Catatan: ini adalah prototype tahap analisis/perancangan awal. Pencarian paket
masih menggunakan penelusuran sederhana pada list Python. Implementasi ADT
khusus, BST, Hash Table, Graph, BFS/DFS, integrasi lengkap, dan benchmark
merupakan pekerjaan progres berikutnya.
"""

import argparse
from typing import List, Optional

from models import Paket, Pelanggan, Kurir, Pengiriman, Lokasi, STATUS_PAKET


class SistemDistribusi:
    """Kelas utama yang menampung data simulasi awal dan operasi prototype."""

    def __init__(self):
        # List Python digunakan sebagai penyimpanan sementara pada prototype.
        self.daftar_paket: List[Paket] = []
        self.daftar_pelanggan: List[Pelanggan] = []
        self.daftar_kurir: List[Kurir] = []
        self.daftar_pengiriman: List[Pengiriman] = []
        self.daftar_lokasi: List[Lokasi] = []
        self.muat_data_awal()

    def muat_data_awal(self):
        """Memuat beberapa record contoh; bukan dataset final 100 record."""
        self.daftar_pelanggan = [
            Pelanggan("PLG0001", "Alya Pratama", "08XX-SIM-0001"),
            Pelanggan("PLG0002", "Bima Saputra", "08XX-SIM-0002"),
            Pelanggan("PLG0003", "Citra Lestari", "08XX-SIM-0003"),
        ]
        self.daftar_kurir = [
            Kurir("KUR001", "Andi Kurir", "Pekanbaru Barat"),
            Kurir("KUR002", "Dewi Kurir", "Pekanbaru Timur"),
        ]
        self.daftar_lokasi = [
            Lokasi("LOK001", "Gudang Pusat"),
            Lokasi("LOK002", "Pekanbaru Barat"),
            Lokasi("LOK003", "Pekanbaru Timur"),
            Lokasi("LOK004", "Tampan"),
        ]
        self.daftar_paket = [
            Paket("PKT000001", "Buku kuliah", 1.2, "Pekanbaru Barat", "Menunggu"),
            Paket("PKT000002", "Aksesori komputer", 0.8, "Pekanbaru Timur", "Diproses"),
            Paket("PKT000003", "Peralatan rumah", 2.5, "Tampan", "Dalam Pengiriman"),
        ]

    def tampilkan_dashboard(self):
        print("\n========== DASHBOARD PROGRES 1 ==========")
        print(f"Jumlah paket       : {len(self.daftar_paket)}")
        print(f"Jumlah pelanggan   : {len(self.daftar_pelanggan)}")
        print(f"Jumlah kurir       : {len(self.daftar_kurir)}")
        print(f"Jumlah pengiriman  : {len(self.daftar_pengiriman)}")
        print(f"Jumlah lokasi      : {len(self.daftar_lokasi)}")
        print("Catatan: data di atas adalah data contoh sementara untuk prototype.")

    def tampilkan_paket(self):
        print("\n================ DAFTAR PAKET ================")
        if not self.daftar_paket:
            print("Belum ada data paket.")
            return
        print(f"{'ID PAKET':<13} {'DESKRIPSI':<24} {'BERAT':>8}  {'TUJUAN':<20} STATUS")
        print("-" * 92)
        for paket in self.daftar_paket:
            print(
                f"{paket.id_paket:<13} {paket.deskripsi[:23]:<24} "
                f"{paket.berat:>6.1f} kg  {paket.tujuan[:19]:<20} {paket.status}"
            )

    def tambah_paket(self, paket: Paket) -> bool:
        """Menambahkan paket; ID harus unik."""
        if self.cari_paket(paket.id_paket) is not None:
            return False
        self.daftar_paket.append(paket)
        return True

    def cari_paket(self, id_paket: str) -> Optional[Paket]:
        """Pencarian sementara secara linear; BST belum diimplementasikan."""
        key = id_paket.strip().upper()
        for paket in self.daftar_paket:
            if paket.id_paket == key:
                return paket
        return None

    def ubah_status_paket(self, id_paket: str, status_baru: str) -> bool:
        paket = self.cari_paket(id_paket)
        if paket is None or status_baru not in STATUS_PAKET:
            return False
        paket.status = status_baru
        return True

    def tampilkan_pelanggan(self):
        print("\n============= DAFTAR PELANGGAN =============")
        for item in self.daftar_pelanggan:
            print(f"{item.id_pelanggan:<10} | {item.nama:<20} | {item.kontak}")

    def tampilkan_kurir(self):
        print("\n================ DAFTAR KURIR ================")
        for item in self.daftar_kurir:
            print(f"{item.id_kurir:<8} | {item.nama:<18} | {item.wilayah_tugas}")

    def tampilkan_lokasi(self):
        print("\n================ DAFTAR LOKASI ================")
        for item in self.daftar_lokasi:
            print(f"{item.id_lokasi:<8} | {item.nama_wilayah}")

    @staticmethod
    def tampilkan_rancangan_struktur_data():
        print("\n======= PEMETAAN STRUKTUR DATA (RENCANA) =======")
        rows = [
            ("Array/List", "Penyimpanan daftar paket"),
            ("Linked List", "Riwayat perubahan status paket"),
            ("Stack", "Undo perubahan status terakhir (LIFO)"),
            ("Queue", "Antrean paket yang akan diproses (FIFO)"),
            ("BST", "Pencarian paket berdasarkan ID Paket"),
            ("Hash Table", "Pencarian pelanggan berdasarkan ID Pelanggan"),
            ("Graph", "Jaringan lokasi; direncanakan BFS dan DFS"),
        ]
        for nomor, (nama, fungsi) in enumerate(rows, start=1):
            print(f"{nomor}. {nama:<13} : {fungsi}")
        print("\nStatus: pemetaan desain awal. Implementasi struktur data khusus dilakukan pada progres berikutnya.")

    def menu_tambah_paket(self):
        print("\n----------- TAMBAH PAKET (PROTOTYPE) -----------")
        try:
            id_paket = input("ID paket             : ").strip().upper()
            deskripsi = input("Deskripsi barang     : ").strip()
            berat = float(input("Berat (kg)           : "))
            tujuan = input("Tujuan/wilayah       : ").strip()
            paket = Paket(id_paket, deskripsi, berat, tujuan)
            if self.tambah_paket(paket):
                print("Paket berhasil ditambahkan ke penyimpanan sementara.")
            else:
                print("Gagal: ID paket sudah digunakan.")
        except ValueError as error:
            print(f"Input tidak valid: {error}")

    def menu_cari_paket(self):
        id_paket = input("Masukkan ID paket: ").strip()
        paket = self.cari_paket(id_paket)
        if paket is None:
            print("Paket tidak ditemukan.")
        else:
            print("\nPaket ditemukan:")
            print(f"ID          : {paket.id_paket}")
            print(f"Deskripsi   : {paket.deskripsi}")
            print(f"Berat       : {paket.berat:.1f} kg")
            print(f"Tujuan      : {paket.tujuan}")
            print(f"Status      : {paket.status}")
            print("Metode pencarian: linear/sequential search pada list sementara.")

    def menu_ubah_status(self):
        id_paket = input("Masukkan ID paket: ").strip()
        print("Status tersedia: " + ", ".join(STATUS_PAKET))
        status = input("Status baru: ").strip().title()
        if self.ubah_status_paket(id_paket, status):
            print("Status paket berhasil diperbarui pada prototype.")
        else:
            print("Gagal mengubah status. Periksa ID paket dan pilihan status.")

    def jalankan(self):
        while True:
            print("\n" + "=" * 68)
            print(" SISTEM MANAJEMEN DISTRIBUSI DAN PENGIRIMAN BARANG")
            print(" PROGRES 1 - KELOMPOK 3")
            print("=" * 68)
            print("1. Dashboard dan ringkasan data")
            print("2. Tampilkan daftar paket")
            print("3. Tambah paket (prototype)")
            print("4. Cari paket berdasarkan ID (pencarian sementara)")
            print("5. Ubah status paket (prototype)")
            print("6. Tampilkan daftar pelanggan")
            print("7. Tampilkan daftar kurir")
            print("8. Tampilkan daftar lokasi")
            print("9. Lihat rancangan pemetaan struktur data")
            print("0. Keluar")
            pilihan = input("Pilih menu: ").strip()

            if pilihan == "1":
                self.tampilkan_dashboard()
            elif pilihan == "2":
                self.tampilkan_paket()
            elif pilihan == "3":
                self.menu_tambah_paket()
            elif pilihan == "4":
                self.menu_cari_paket()
            elif pilihan == "5":
                self.menu_ubah_status()
            elif pilihan == "6":
                self.tampilkan_pelanggan()
            elif pilihan == "7":
                self.tampilkan_kurir()
            elif pilihan == "8":
                self.tampilkan_lokasi()
            elif pilihan == "9":
                self.tampilkan_rancangan_struktur_data()
            elif pilihan == "0":
                print("Program prototype Progres 1 selesai. Terima kasih.")
                break
            else:
                print("Pilihan tidak valid. Silakan pilih menu 0 sampai 9.")


def run_self_test():
    """Pemeriksaan sederhana untuk model dan operasi dasar prototype."""
    sistem = SistemDistribusi()
    assert len(sistem.daftar_paket) == 3
    assert sistem.cari_paket("PKT000001") is not None
    assert sistem.cari_paket("PKT-TIDAK-ADA") is None
    assert sistem.tambah_paket(Paket("PKT000010", "Mouse", 0.3, "Tampan")) is True
    assert sistem.tambah_paket(Paket("PKT000010", "Duplikat", 0.4, "Tampan")) is False
    assert sistem.ubah_status_paket("PKT000010", "Diproses") is True
    assert sistem.cari_paket("PKT000010").status == "Diproses"
    try:
        Paket("PKTERR", "Berat salah", 0, "Pekanbaru")
    except ValueError:
        pass
    else:
        raise AssertionError("Validasi berat tidak berjalan.")
    return "LULUS: model entitas, validasi dasar, tambah, cari, dan ubah status prototype."


def main():
    parser = argparse.ArgumentParser(description="Prototype Progres 1 Kelompok 3")
    parser.add_argument("--self-test", action="store_true", help="jalankan pemeriksaan dasar prototype")
    args = parser.parse_args()
    if args.self_test:
        print(run_self_test())
    else:
        SistemDistribusi().jalankan()


if __name__ == "__main__":
    main()
