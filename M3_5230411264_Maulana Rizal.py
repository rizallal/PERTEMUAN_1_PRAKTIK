class DaftarMenu:

    def MainMenu():
        while True:
            DaftarMenu.tampilkan_main_menu()
            pilihan = input("Pilih menu: ")

            if pilihan == '1':
                DaftarMenu.menu_makanan()
            elif pilihan == '2':
                DaftarMenu.menu_minuman()
            elif pilihan == '3':
                DaftarMenu.SubMenu()
            elif pilihan == '4':
                print("Terima kasih !")
                break
            else:
                print("Pilihan tidak valid.")


    def tampilkan_main_menu():
        print("\n===== Menu Utama =====")
        print("1. Lihat Daftar Makanan")
        print("2. Lihat Daftar Minuman")
        print("3. Tambah Menu")
        print("4. Keluar")
        print("=======================")

    def menu_makanan():
        print("\n===== List Makanan =====")
        print("1. Nasi Goreng: Rp15000")
        print("2. Ayam Geprek: Rp25000")
        print("3. Seblak: Rp15000")
        print("4. Soto: Rp10000")
        print("5. Kembali")
        print("=========================")
        input("Tekan 5 untuk kembali ke Menu Utama...")

    def menu_minuman():
        print("\n===== List Minuman =====")
        print("1. Es Teh: Rp5000")
        print("2. Es Jeruk: Rp5000")
        print("3. Air Putih: Rp4000")
        print("4. Air Es: Rp1000")
        print("=========================")
        input("Tekan 5 untuk kembali ke Menu Utama...")

    def SubMenu():
        while True:
            DaftarMenu.tampilkan_sub_menu()
            pilihan = input("Pilih sub-menu: ")

            if pilihan == '1':
                DaftarMenu.tambah_makanan()
            elif pilihan == '2':
                DaftarMenu.tambah_minuman()
            elif pilihan == '3':
                break
            else:
                print("Pilihan tidak valid. Coba lagi.")

    def tampilkan_sub_menu():
        print("\n===== Tambah Menu =====")
        print("1. Tambah Makanan")
        print("2. Tambah Minuman")
        print("3. Kembali")
        print("=======================")


    def tambah_makanan():
        nama_makanan = input("Masukkan nama makanan: ")
        harga_makanan = input("Masukkan harga makanan: ")
        print(f"{nama_makanan} harga Rp{harga_makanan} telah ditambahkan.")
        input("Tekan 5 untuk kembali ke SubMenu...")


    def tambah_minuman():
        nama_minuman = input("Masukkan nama minuman: ")
        harga_minuman = input("Masukkan harga minuman: ")
        print(f"{nama_minuman} harga Rp{harga_minuman} telah ditambahkan.")
        input("Tekan 5 untuk kembali ke SubMenu...")


DaftarMenu.MainMenu()
