import mysql.connector
from mysql.connector import Error

# Koneksi ke database
try:
    mydb = mysql.connector.connect(
        user="root", password="", host="localhost", database="challenge"
    )
    if mydb.is_connected():
        print("Berhasil terhubung ke database!")
except Error as e:
    print(f"Error: {e}")
    exit()
    
# CRUD Operations
class DatabaseCRUD:
    def __init__(self, connection):
        self.conn = connection
        self.cur = connection.cursor()

    def __del__(self):
        self.cur.close()
        self.conn.close()

    # CRUD Pegawai
    def create_pegawai(self, nik, nama, alamat):
        query = "INSERT INTO pegawai (nik, nama, alamat) VALUES (%s, %s, %s)"
        self.execute_query(query, (nik, nama, alamat))

    def read_pegawai(self):
        query = "SELECT * FROM pegawai"
        return self.fetch_query(query)

    def update_pegawai(self, nik, nama, alamat):
        query = "UPDATE pegawai SET nama = %s, alamat = %s WHERE nik = %s"
        self.execute_query(query, (nama, alamat, nik))

    def delete_pegawai(self, nik):
        query = "DELETE FROM pegawai WHERE nik = %s"
        self.execute_query(query, (nik,))

    # CRUD Produk
    def create_produk(self, kode_produk, nama_produk, jenis_produk, harga):
        query = "INSERT INTO produk (kode_produk, nama_produk, jenis_produk, harga) VALUES (%s, %s, %s, %s)"
        self.execute_query(query, (kode_produk, nama_produk, jenis_produk, harga))

    def read_produk(self):
        query = "SELECT * FROM produk"
        return self.fetch_query(query)

    def update_produk(self, kode_produk, nama_produk, jenis_produk, harga):
        query = "UPDATE produk SET nama_produk = %s, jenis_produk = %s, harga = %s WHERE kode_produk = %s"
        self.execute_query(query, (nama_produk, jenis_produk, harga, kode_produk))

    def delete_produk(self, kode_produk):
        query = "DELETE FROM produk WHERE kode_produk = %s"
        self.execute_query(query, (kode_produk,))

    # CRUD Transaksi
    def create_transaksi(self, no_transaksi, detail_transaksi):
        query = "INSERT INTO transaksi (no_transaksi, detail_transaksi) VALUES (%s, %s)"
        self.execute_query(query, (no_transaksi, detail_transaksi))

    def read_transaksi(self):
        query = "SELECT * FROM transaksi"
        return self.fetch_query(query)

    def update_transaksi(self, no_transaksi, detail_transaksi):
        query = "UPDATE transaksi SET detail_transaksi = %s WHERE no_transaksi = %s"
        self.execute_query(query, (detail_transaksi, no_transaksi))

    def delete_transaksi(self, no_transaksi):
        query = "DELETE FROM transaksi WHERE no_transaksi = %s"
        self.execute_query(query, (no_transaksi,))

    # CRUD Struk
    def create_struk(self, no_transaksi, nama_pegawai, nama_produk, jumlah_produk, total_harga):
        query = """
        INSERT INTO struk (no_transaksi, nama_pegawai, nama_produk, jumlah_produk, total_harga)
        VALUES (%s, %s, %s, %s, %s)
        """
        self.execute_query(query, (no_transaksi, nama_pegawai, nama_produk, jumlah_produk, total_harga))

    def read_struk(self):
        query = "SELECT * FROM struk"
        return self.fetch_query(query)

    def update_struk(self, no_transaksi, nama_pegawai, nama_produk, jumlah_produk, total_harga):
        query = """
        UPDATE struk SET nama_pegawai = %s, nama_produk = %s, jumlah_produk = %s, total_harga = %s
        WHERE no_transaksi = %s
        """
        self.execute_query(query, (nama_pegawai, nama_produk, jumlah_produk, total_harga, no_transaksi))

    def delete_struk(self, no_transaksi):
        query = "DELETE FROM struk WHERE no_transaksi = %s"
        self.execute_query(query, (no_transaksi,))

    # General Methods
    def execute_query(self, query, params=None):
        try:
            self.cur.execute(query, params)
            self.conn.commit()
        except Error as e:
                        print(f"Error: {e}")

    def fetch_query(self, query, params=None):
        try:
            self.cur.execute(query, params)
            return self.cur.fetchall()
        except Error as e:
            print(f"Error: {e}")
            return []

# Menu dan Submenu
if __name__ == "__main__":
    crud = DatabaseCRUD(mydb)

    while True:
        print("\n=== MENU UTAMA ===")
        print("1. Kelola Pegawai")
        print("2. Kelola Produk")
        print("3. Kelola Transaksi")
        print("4. Kelola Struk")
        print("5. Keluar")

        menu = input("Pilih menu: ")

        if menu == "1":
            while True:
                print("\n--- Kelola Pegawai ---")
                print("1. Tambah Pegawai")
                print("2. Lihat Pegawai")
                print("3. Update Pegawai")
                print("4. Hapus Pegawai")
                print("5. Kembali ke Menu Utama")

                submenu = input("Pilih submenu: ")

                if submenu == "1":
                    nik = input("Masukkan NIK: ")
                    nama = input("Masukkan Nama: ")
                    alamat = input("Masukkan Alamat: ")
                    crud.create_pegawai(nik, nama, alamat)
                    print("Pegawai berhasil ditambahkan.")
                elif submenu == "2":
                    data = crud.read_pegawai()
                    for row in data:
                        print(row)
                elif submenu == "3":
                    nik = input("Masukkan NIK Pegawai yang ingin diupdate: ")
                    nama = input("Masukkan Nama Baru: ")
                    alamat = input("Masukkan Alamat Baru: ")
                    crud.update_pegawai(nik, nama, alamat)
                    print("Pegawai berhasil diupdate.")
                elif submenu == "4":
                    nik = input("Masukkan NIK Pegawai yang ingin dihapus: ")
                    crud.delete_pegawai(nik)
                    print("Pegawai berhasil dihapus.")
                elif submenu == "5":
                    break
                else:
                    print("Pilihan tidak valid.")

        elif menu == "2":
            while True:
                print("\n--- Kelola Produk ---")
                print("1. Tambah Produk")
                print("2. Lihat Produk")
                print("3. Update Produk")
                print("4. Hapus Produk")
                print("5. Kembali ke Menu Utama")

                submenu = input("Pilih submenu: ")

                if submenu == "1":
                    kode_produk = input("Masukkan Kode Produk: ")
                    nama_produk = input("Masukkan Nama Produk: ")
                    jenis_produk = input("Masukkan Jenis Produk: ")
                    harga = float(input("Masukkan Harga: "))
                    crud.create_produk(kode_produk, nama_produk, jenis_produk, harga)
                    print("Produk berhasil ditambahkan.")
                elif submenu == "2":
                    data = crud.read_produk()
                    for row in data:
                        print(row)
                elif submenu == "3":
                    kode_produk = input("Masukkan Kode Produk yang ingin diupdate: ")
                    nama_produk = input("Masukkan Nama Baru: ")
                    jenis_produk = input("Masukkan Jenis Baru: ")
                    harga = float(input("Masukkan Harga Baru: "))
                    crud.update_produk(kode_produk, nama_produk, jenis_produk, harga)
                    print("Produk berhasil diupdate.")
                elif submenu == "4":
                    kode_produk = input("Masukkan Kode Produk yang ingin dihapus: ")
                    crud.delete_produk(kode_produk)
                    print("Produk berhasil dihapus.")
                elif submenu == "5":
                    break
                else:
                    print("Pilihan tidak valid.")

        elif menu == "3":
            while True:
                print("\n--- Kelola Transaksi ---")
                print("1. Tambah Transaksi")
                print("2. Lihat Transaksi")
                print("3. Update Transaksi")
                print("4. Hapus Transaksi")
                print("5. Kembali ke Menu Utama")

                submenu = input("Pilih submenu: ")

                if submenu == "1":
                    no_transaksi = input("Masukkan No Transaksi: ")
                    detail_transaksi = input("Masukkan Detail Transaksi: ")
                    crud.create_transaksi(no_transaksi, detail_transaksi)
                    print("Transaksi berhasil ditambahkan.")
                elif submenu == "2":
                    data = crud.read_transaksi()
                    for row in data:
                        print(row)
                elif submenu == "3":
                    no_transaksi = input("Masukkan No Transaksi yang ingin diupdate: ")
                    detail_transaksi = input("Masukkan Detail Transaksi Baru: ")
                    crud.update_transaksi(no_transaksi, detail_transaksi)
                    print("Transaksi berhasil diupdate.")
                elif submenu == "4":
                    no_transaksi = input("Masukkan No Transaksi yang ingin dihapus: ")
                    crud.delete_transaksi(no_transaksi)
                    print("Transaksi berhasil dihapus.")
                elif submenu == "5":
                    break
                else:
                    print("Pilihan tidak valid.")

        elif menu == "4":
            while True:
                print("\n--- Kelola Struk ---")
                print("1. Tambah Struk")
                print("2. Lihat Struk")
                print("3. Update Struk")
                print("4. Hapus Struk")
                print("5. Kembali ke Menu Utama")

                submenu = input("Pilih submenu: ")

                if submenu == "1":
                    no_transaksi = input("Masukkan No Transaksi: ")
                    nama_pegawai = input("Masukkan Nama Pegawai: ")
                    nama_produk = input("Masukkan Nama Produk: ")
                    jumlah_produk = int(input("Masukkan Jumlah Produk: "))
                    total_harga = float(input("Masukkan Total Harga: "))
                    crud.create_struk(no_transaksi, nama_pegawai, nama_produk, jumlah_produk, total_harga)
                    print("Struk berhasil ditambahkan.")
                elif submenu == "2":
                    data = crud.read_struk()
                    for row in data:
                        print(row)
                elif submenu == "3":
                    no_transaksi = input("Masukkan No Transaksi yang ingin diupdate: ")
                    nama_pegawai = input("Masukkan Nama Pegawai Baru: ")
                    nama_produk = input("Masukkan Nama Produk Baru: ")
                    jumlah_produk = int(input("Masukkan Jumlah Produk Baru: "))
                    total_harga = float(input("Masukkan Total Harga Baru: "))
                    crud.update_struk(no_transaksi, nama_pegawai, nama_produk, jumlah_produk, total_harga)
                    print("Struk berhasil diupdate.")
                elif submenu == "4":
                    no_transaksi = input("Masukkan No Transaksi yang ingin dihapus: ")
                    crud.delete_struk(no_transaksi)
                    print("Struk berhasil dihapus.")
                elif submenu == "5":
                    break
                else:
                    print("Pilihan tidak valid.")

        elif menu == "5":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid.")
            
            
            
