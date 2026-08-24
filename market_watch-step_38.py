# === Stage 38: Добавь расширенный набор тестов для ошибок и пограничных случаев ===
# Project: MarketWatch
import unittest

class TestEdgeCases(unittest.TestCase):
    def test_empty_name(self):
        from marketwatch import Product
        with self.assertRaises(ValueError):
            Product("", 100)
    def test_empty_store(self):
        from marketwatch import Store
        with self.assertRaises(ValueError):
            Store("", "test")
    def test_empty_category(self):
        from marketwatch import Category
        with self.assertRaises(ValueError):
            Category("", "test")
    def test_invalid_price(self):
        from marketwatch import Price
        with self.assertRaises(ValueError):
            Price("abc")
    def test_invalid_discount(self):
        from marketwatch import Discount
        with self.assertRaises(ValueError):
            Discount("abc")
    def test_invalid_date(self):
        from marketwatch import Observation
        with self.assertRaises(ValueError):
            Observation("2024-13-45", 100, "test")
    def test_invalid_history_entry(self):
        from marketwatch import HistoryEntry
        with self.assertRaises(ValueError):
            HistoryEntry("2024-13-45", 100, "test")
    def test_invalid_observation(self):
        from marketwatch import Observation
        with self.assertRaises(ValueError):
            Observation("2024-13-45", 100, "test")
    def test_invalid_store_history(self):
        from marketwatch import StoreHistory
        with self.assertRaises(ValueError):
            StoreHistory("2024-13-45", "test")
    def test_invalid_category_history(self):
        from marketwatch import CategoryHistory
        with self.assertRaises(ValueError):
            CategoryHistory("2024-13-45", "test")
    def test_invalid_product_price(self):
        from marketwatch import ProductPrice
        with self.assertRaises(ValueError):
            ProductPrice("2024-13-45", 100, "test")
    def test_invalid_product_discount(self):
        from marketwatch import ProductDiscount
        with self.assertRaises(ValueError):
            ProductDiscount("2024-13-45", 100, "test")
    def test_invalid_product_history(self):
        from marketwatch import ProductHistory
        with self.assertRaises(ValueError):
            ProductHistory("2024-13-45", 100, "test")
    def test_invalid_product_observation(self):
        from marketwatch import ProductObservation
        with self.assertRaises(ValueError):
            ProductObservation("2024-13-45", 100, "test")
    def test_invalid_product_store_history(self):
        from marketwatch import ProductStoreHistory
        with self.assertRaises(ValueError):
            ProductStoreHistory("2024-13-45", 100, "test")
    def test_invalid_product_category_history(self):
        from marketwatch import ProductCategoryHistory
        with self.assertRaises(ValueError):
            ProductCategoryHistory("2024-13-45", 100, "test")

if __name__ == "__main__":
    unittest.main()
