# === Stage 37: Добавь мини-набор unit-тестов без внешних зависимостей ===
# Project: MarketWatch
import unittest


class TestMarketWatch(unittest.TestCase):
    def setUp(self):
        from marketwatch import App, Product, Shop, Price, HistoryEntry, Discount
        self.app = App()

    def test_product_creation(self):
        p = Product("iPhone 15", 999.0)
        self.assertEqual(p.name, "iPhone 15")
        self.assertEqual(p.price, 999.0)

    def test_shop_creation(self):
        s = Shop("AppleStore", 42.0)
        self.assertEqual(s.name, "AppleStore")
        self.assertAlmostEqual(s.rating, 42.0)

    def test_price_with_discount(self):
        d = Discount(15.0)
        p = Price(999.0, d)
        self.assertEqual(p.price, 849.15)

    def test_history_entry(self):
        entry = HistoryEntry("AppleStore", "iPhone 15", 999.0, "2024-06-15")
        self.assertEqual(entry.shop, "AppleStore")
        self.assertEqual(entry.product, "iPhone 15")

    def test_add_product(self):
        prod = Product("Samsung S24", 899.0)
        self.app.add_product(prod)
        products = self.app.get_products()
        self.assertTrue(any(p.name == "Samsung S24" for p in products))


if __name__ == "__main__":
    unittest.main()
