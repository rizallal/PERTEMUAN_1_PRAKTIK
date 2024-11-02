class Produk:
    def __init__(self, kode_produk, nama_produk, jenis_produk):
        self.kode_produk = kode_produk
        self.nama_produk = nama_produk
        self.jenis_produk = jenis_produk

    def get_info(self):
        return f"Produk: {self.nama_produk} (Kode: {self.kode_produk}, Jenis: {self.jenis_produk})"

    def get_harga(self):
        return 0 

class Snack(Produk):
    def __init__(self, kode_produk, nama_snack, harga):
        super().__init__(kode_produk, nama_snack, "Snack")
        self.harga = harga

    def get_harga(self):
        return self.harga

    def get_info(self):
        return f"Snack: {self.nama_produk}, Harga: {self.harga}"



class Makanan(Produk):
    def __init__(self, kode_produk, nama_makanan, harga):
        super().__init__(kode_produk, nama_makanan, "Makanan")
        self.harga = harga

    def get_harga(self):
        return self.harga

    def get_info(self):
        return f"Makanan: {self.nama_produk}, Harga: {self.harga}"



class Minuman(Produk):
    def __init__(self, kode_produk, nama_minuman, harga):
        super().__init__(kode_produk, nama_minuman, "Minuman")
        self.harga = harga


    def get_harga(self):
        return self.harga

    def get_info(self):
        return f"Minuman: {self.nama_produk}, Harga: {self.harga}"



class Pegawai:
    def __init__(self, nik, nama, alamat):
        self.nik = nik
        self.nama = nama
        self.alamat = alamat

    def get_info(self):
        return f"Pegawai: {self.nama} (NIK: {self.nik}), Alamat: {self.alamat}"



class Transaksi:
    def __init__(self, no_transaksi, detail_transaksi):
        self.no_transaksi = no_transaksi
        self.detail_transaksi = detail_transaksi 

    def get_total_harga(self):
        return sum(produk.get_harga() for produk in self.detail_transaksi)

    def get_info(self):
        produk_list = [produk.get_info() for produk in self.detail_transaksi]
        return f"Transaksi No: {self.no_transaksi}\nDetail: {', '.join(produk_list)}\nTotal Harga: {self.get_total_harga()}"


class Struk:
    def __init__(self, no_transaksi, nama_pegawai, transaksi):
        self.no_transaksi = no_transaksi
        self.nama_pegawai = nama_pegawai
        self.transaksi = transaksi

    def print_struk(self):
        print(f"\n--- Struk Transaksi No: {self.no_transaksi} ---")
        print(f"Nama Pegawai: {self.nama_pegawai}")
        print(self.transaksi.get_info())
        print("---------------------------\n")


def submenu():
    produk_list = []
    pegawai_list = []
    transaksi_list = []

    while True:
        print("\n============ MENU UTAMA ============")
        print("1. Tambah Produk")
        print("2. Tambah Pegawai")
        print("3. Buat Transaksi")
        print("4. Cetak Struk")
        print("5. Keluar")
        print("=====================================")
        pilihan = input("Pilih Opsi (1-5): ")

        if pilihan == "1":
            print("\n--- Tambah Produk ---")
            jenis = input("Jenis produk (Snack/Makanan/Minuman): ").lower()
            kode_produk = input("Kode Produk: ")
            nama_produk = input("Nama Produk: ")
            harga = int(input("Harga: "))

            if jenis == "snack":
                produk = Snack(kode_produk, nama_produk, harga)
            elif jenis == "makanan":
                produk = Makanan(kode_produk, nama_produk, harga)
            elif jenis == "minuman":
                produk = Minuman(kode_produk, nama_produk, harga)
            else:
                print("Jenis produk tidak valid!")
                continue

            produk_list.append(produk)
            print(f"Produk {nama_produk} berhasil ditambahkan.")

        elif pilihan == "2":
            print("\n--- Tambah Pegawai ---")
            nik = input("NIK: ")
            nama = input("Nama Pegawai: ")
            alamat = input("Alamat: ")

            pegawai = Pegawai(nik, nama, alamat)
            pegawai_list.append(pegawai)
            print(f"Pegawai {nama} berhasil ditambahkan.")

        elif pilihan == "3":
            print("\n--- Buat Transaksi ---")
            if not produk_list or not pegawai_list:
                print("Produk atau Pegawai belum tersedia.")
                continue

            no_transaksi = input("No Transaksi: ")
            nama_pegawai = input("Nama Pegawai: ")
            pegawai = next((p for p in pegawai_list if p.nama == nama_pegawai), None)

            if pegawai is None:
                print("Pegawai tidak ditemukan!")
                continue

            detail_transaksi = []
            while True:
                kode_produk = input("Masukkan kode produk (atau 'selesai' untuk selesai): ")
                if kode_produk.lower() == "selesai":
                    break
                produk = next((p for p in produk_list if p.kode_produk == kode_produk), None)
                if produk:
                    detail_transaksi.append(produk)
                else:
                    print("Produk tidak ditemukan!")

            transaksi = Transaksi(no_transaksi, detail_transaksi)
            transaksi_list.append((transaksi, pegawai))
            print(f"Transaksi No {no_transaksi} berhasil dibuat.")

        elif pilihan == "4":
            print("\n--- Cetak Struk ---")
            no_transaksi = input("Masukkan No Transaksi: ")
            transaksi_pegawai = next((t for t in transaksi_list if t[0].no_transaksi == no_transaksi), None)

            if transaksi_pegawai:
                transaksi, pegawai = transaksi_pegawai
                struk = Struk(no_transaksi, pegawai.nama, transaksi)
                struk.print_struk()
            else:
                print("Transaksi tidak ditemukan!")

        elif pilihan == "5":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid! Coba lagi.")


submenu()
