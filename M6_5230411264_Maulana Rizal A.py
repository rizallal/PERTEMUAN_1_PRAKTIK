class Order:
    def __init__(self, ID, name, total_order):
        self.__ID = ID
        self.name = name
        self.total_order = total_order

    def setOrder(self, ID, name, total_order):
        self.__ID = ID
        self.name = name
        self.total_order = total_order

    def getOrderDetails(self):
        return {
            'ID': self.__ID,
            'Nama': self.name,
            'Total Order': self.total_order
        }

class Delivery:
    def __init__(self, id, name, information, date, address):
        self.__id = id
        self.name = name
        self.information = information
        self.date = date
        self.address = address

    def processDelivery(self):
        print("Memproses pengiriman untuk:", self.name)
        print("Tanggal Pengiriman:", self.date)
        print("Alamat:", self.address)

    def getDeliveryDetails(self):
        return {
            'ID': self.__id,
            'Nama': self.name,
            'Informasi': self.information,
            'Tanggal': self.date,
            'Alamat': self.address
        }



orders = []
deliveries = []


def tambah_order():
    ID = int(input("Masukkan ID Order: "))
    name = input("Masukkan Nama Order: ")
    total_order = float(input("Masukkan Total Order: "))
    order = Order(ID, name, total_order)
    orders.append(order)
    print("Order berhasil ditambahkan!\n")


def lihat_orders():
    if not orders:
        print("Tidak ada order yang tersedia.\n")
    else:
        for order in orders:
            print(order.getOrderDetails())
        print()


def tambah_delivery():
    id = int(input("Masukkan ID Pengiriman: "))
    name = input("Masukkan Nama Pengiriman: ")
    information = input("Masukkan Informasi Pengiriman: ")
    date = input("Masukkan Tanggal Pengiriman (YYYY-MM-DD): ")
    address = input("Masukkan Alamat Pengiriman: ")
    delivery = Delivery(id, name, information, date, address)
    deliveries.append(delivery)
    print("Pengiriman berhasil ditambahkan!\n")


def lihat_deliveries():
    if not deliveries:
        print("Tidak ada pengiriman yang tersedia.\n")
    else:
        for delivery in deliveries:
            print(delivery.getDeliveryDetails())
        print()


def proses_delivery():
    if not deliveries:
        print("Tidak ada pengiriman untuk diproses.\n")
    else:
        for delivery in deliveries:
            delivery.processDelivery()
        print()


def menu_utama():
    while True:
        print("===========Menu Utama:===========")
        print("Total Orders:", len(orders))
        print("Total Deliveries:", len(deliveries))
        print("1. Kelola Order")
        print("2. Kelola Pengiriman")
        print("3. Keluar")
        print("================================")
        pilihan = input("Masukkan pilihan Anda: ")

        if pilihan == '1':
            menu_order()
        elif pilihan == '2':
            menu_pengiriman()
        elif pilihan == '3':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.\n")


def menu_order():
    while True:
        print("\n========= Menu Order =========")
        print("Total Orders:", len(orders))
        print("Total Deliveries:", len(deliveries))
        print("1. Tambah Order")
        print("2. Lihat Order")
        print("3. Kembali ke menu utama")
        print("=====================================")
        pilihan = input("Masukan pilihan anda")

        if pilihan == '1':
            tambah_order()
        elif pilihan == '2':
            lihat_orders()
        elif pilihan == '3':
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.\n")


def menu_pengiriman():
    while True:
        print("\n========= Menu Pengiriman =========")
        print("1. Tambah Pengirim")
        print("2. Lihat Pengirim")
        print("3. Proses Pengirim")
        print("4. Kembali ke menu utama")
        print("=====================================")
        pilihan = input("Pilih salah satu")

        if pilihan == '1':
            tambah_delivery()
        elif pilihan == '2':
            lihat_deliveries()
        elif pilihan == '3':
            proses_delivery()
        elif pilihan == '4':
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.\n")


menu_utama()
