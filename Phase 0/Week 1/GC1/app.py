"""
=========================================
Graded Challange 1

Nama: Muhammad Iqbal Saputra
Batch: RMT-32

Program ini dibuat untuk perushaan retail yang mana memungkinkan user untuk menambah, menghapus dan melihat item di keranjang belanja pada sebuah toko.
=========================================
"""


class CartItem:
    """
    Class untuk merepresentasikan item dalam keranjang belanja.

    Attributes:
        name (str): Nama item.
        price (float): Harga item.
    """

    def __init__(self, name, price):
        """
        Fungsi u/ menginisialisasi item dengan nama dan harga.

        Parameter:
            name (str): Nama item.
            price (float): Harga item.
        """
        self.name = name
        self.price = price


class ShoppingCart:
    """
    Class untuk mengelola keranjang belanja.

    Attributes:
        items (list): Daftar item dalam keranjang belanja.
    """

    def __init__(self):
        """
        Fungsi u/ menginisialisasi keranjang belanja dengan daftar item kosong.
        """
        self.items = []

    def add_item(self, item):
        """
        Fungsi u/ menambahkan item ke dalam keranjang belanja.

        Parameter:
            item (CartItem): Item yang akan ditambahkan ke keranjang belanja.
        """
        self.items.append(item)
        print(f'Barang "{item.name}" berhasil dimasukan ke keranjang')

    def remove_item(self, item_name):
        """
        Fungsi u/ item dari keranjang belanja berdasarkan nama.

        Parameter:
            item_name (str): Nama item yang akan dihapus dari keranjang belanja.
        """
        for item in self.items:
            if item.name == item_name:
                self.items.remove(item)
                print(f'Barang "{item_name} berhasil dihapus di keranjang belanja.')

                return
        print(f'Barang "{item_name}" tidak ditemukan di keranjang.')

    def display_items(self):
        """
        Fungsi u/ menampilkan semua item yang ada di dalam keranjang belanja.
        """
        if not self.items:
            print("Keranjang belanja kosong.")
        else:
            print("Barang di Keranjang:")
            for i, item in enumerate(self.items):
                print(f"{i+1}. {item.name} - Rp {item.price:0.2f}")

    def calculate_total(self):
        """
        Fungsi u/ menghitung dan mengembalikan total harga semua item dalam keranjang belanja.

        Returns:
            float: Total harga semua item dalam keranjang belanja.
        """
        return sum(item.price for item in self.items)

    def run(self):
        """
        Fungsi u/ menjalankan aplikasi keranjang belanja.
        """
        print("Selamat Datang di Keranjang Belanja Toko Makmur!".center(30, "="))
        runApp = 1
        while runApp:
            print("\nMenu:")
            print("1. Menambah Barang")
            print("2. Hapus Barang")
            print("3. Tampilkan Barang di Keranjang")
            print("4. Lihat Total Belanja")
            print("5. Exit")

            choice = input("Pilihan: ")
            if choice == "1":
                name = input("Masukan nama barang: ")
                try:
                    price = float(input("Masukan harga: "))
                    self.add_item(CartItem(name, price))
                except (
                    ValueError
                ):  # jika user memasukan selain angka, misal user memasukan sebuah huruf/string maka akan raise error
                    print("Harga harus berupa angka")
            elif choice == "2":
                name = input("Masukan nama barang yang ingin dihapus: ")
                self.remove_item(name)
            elif choice == "3":
                self.display_items()
            elif choice == "4":
                total = self.calculate_total()
                print(f"Total belanja: Rp {total: 0.2f}")
            elif choice == "5":
                print("Sampai Jumpa! Terima kasih sudah belanja di Toko Makmur.")
                break
            else:
                print("Pilihannya salah. Coba lagi ya.")


if __name__ == "__main__":
    cart = ShoppingCart()
    cart.run()
