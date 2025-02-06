import unittest
from app import CartItem, ShoppingCart

class TestShoppingCart(unittest.TestCase):
    """
    Class untuk menguji fungsi ShoppingCart.
    """
    def test_add_item(self):
        """
        Fungsi u/ menguji method menambahkan item ke dalam keranjang belanja.
        """
        cart = ShoppingCart()
        cart.add_item(CartItem("Apel", 3400))
        self.assertEqual(len(cart.items), 1)
        self.assertEqual(cart.items[0].name,"Apel")
        self.assertEqual(cart.items[0].price, 3400)
    
    def test_remove_item(self):
        """~
        Fungsi u/ menguji method menghapus item dari keranjang belanja.
        """
        cart = ShoppingCart()
        cart.add_item(CartItem("Apel", 3400))
        cart.remove_item("Apel")
        self.assertEqual(len(cart.items), 0)
        
    def test_calculate_total(self):
        """
        Fungsi u/ menguji method hitung total harga semua item dalam keranjang belanja.
        """
        cart = ShoppingCart()
        cart.add_item(CartItem("Apel", 3400))
        cart.add_item(CartItem("Jeruk", 2100))
        total = cart.calculate_total()
        self.assertEqual(total, 5500)
        
if __name__ == "__main__":
    unittest.main()