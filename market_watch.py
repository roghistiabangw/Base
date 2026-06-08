# === Stage 1: Создай базовую структуру файла приложения, точку входа и демонстрационные данные ===
# Project: MarketWatch
import json
from datetime import datetime, timedelta
from typing import List, Dict, Any

class MarketWatch:
    def __init__(self):
        self.products: List[Dict[str, Any]] = []
        self.history: List[Dict[str, Any]] = []

    def add_product(self, name: str, current_price: float, store: str = "Unknown", discount: float = 0.0) -> None:
        product = {
            "id": len(self.products) + 1,
            "name": name,
            "current_price": current_price,
            "store": store,
            "discount": discount,
            "original_price": current_price / (1 - discount/100) if discount > 0 else None,
            "created_at": datetime.now().isoformat()
        }
        self.products.append(product)

    def record_price_change(self, product_id: int, new_price: float) -> None:
        product = next((p for p in self.products if p["id"] == product_id), None)
        if product:
            change = {
                "product_id": product_id,
                "old_price": product["current_price"],
                "new_price": new_price,
                "timestamp": datetime.now().isoformat()
            }
            self.history.append(change)
            product["current_price"] = new_price

    def get_product(self, product_id: int) -> Dict[str, Any] | None:
        return next((p for p in self.products if p["id"] == product_id), None)

    def save_to_file(self, filename: str = "marketwatch.json") -> None:
        data = {
            "products": self.products,
            "history": self.history
        }
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def load_from_file(self, filename: str = "marketwatch.json") -> None:
        try:
            with open(filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.products = data.get("products", [])
                self.history = data.get("history", [])
        except FileNotFoundError:
            pass

# --- Demo & Entry Point ---
if __name__ == "__main__":
    app = MarketWatch()
    
    # Add demo products
    app.add_product("iPhone 15", 799.0, "Apple Store", 5.0)
    app.add_product("Samsung S24", 849.0, "Samsung Official", 10.0)
    app.add_product("Sony WH-1000XM5", 349.0, "Sony Store", 0.0)
    
    # Simulate a price drop
    app.record_price_change(2, 799.0)
    
    # Save initial state
    app.save_to_file()
    print("MarketWatch initialized with demo data.")
