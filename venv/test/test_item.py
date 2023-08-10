import unittest
from src.item import Item

class TestItem(unittest.TestCase):

    def setUp(self):
        self.item1 = Item("Item1", 100, 10)
        self.item2 = Item("Item2", 150, 5)
        Item.set_discount_rate(0.85)

    def test_average_price(self):
        avg_price = Item.get_average_price()
        self.assertEqual(avg_price, (100 + 150) / 2)

    def test_discounted_price(self):
        self.assertEqual(self.item1.get_discounted_price(), 100 * 0.85)
        self.assertEqual(self.item2.get_discounted_price(), 150 * 0.85)

if __name__ == '__main__':
    unittest.main()
