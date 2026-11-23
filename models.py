from dataclasses import dataclass


@dataclass
class Paket:
    id_paket: str
    deskripsi: str
    berat: float
    tujuan: str
    status: str = "Menunggu"

    def __post_init__(self):
        self.id_paket = self.id_paket.strip().upper()
        self.deskripsi = self.deskripsi.strip()
        self.tujuan = self.tujuan.strip()
        self.status = self.status.strip().title()
        if not self.id_paket:
            raise ValueError("ID paket tidak boleh kosong.")
        if not self.deskripsi:
            raise ValueError("Deskripsi barang tidak boleh kosong.")
        if self.berat <= 0:
            raise ValueError("Berat paket harus lebih dari 0 kg.")
        if not self.tujuan:
            raise ValueError("Tujuan paket tidak boleh kosong.")


@dataclass
class Pelanggan:
    id_pelanggan: str
    nama: str
    kontak: str

    def __post_init__(self):
        self.id_pelanggan = self.id_pelanggan.strip().upper()
        self.nama = self.nama.strip()
        self.kontak = self.kontak.strip()


@dataclass
class Kurir:
    id_kurir: str
    nama: str
    wilayah_tugas: str

    def __post_init__(self):
        self.id_kurir = self.id_kurir.strip().upper()
        self.nama = self.nama.strip()
        self.wilayah_tugas = self.wilayah_tugas.strip()


@dataclass
class Pengiriman:
    id_pengiriman: str
    id_paket: str
    id_kurir: str
    tanggal: str
    status: str


@dataclass
class Lokasi:
    id_lokasi: str
    nama_wilayah: str


STATUS_PAKET = (
    "Menunggu",
    "Diproses",
    "Dalam Pengiriman",
    "Terkirim",
    "Dibatalkan",
)
