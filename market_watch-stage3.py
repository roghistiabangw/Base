# === Stage 3: Реализуй хранение состояния в памяти и функции добавления записей ===
# Project: MarketWatch
class MarketWatch:
    def __init__(self):
        self.items = {}  # {item_id: {"name": str, "price": float, "store": str, "discount": float, "history": []}}
        self.next_id = 1

    def add_observation(self, name, price, store, discount=0.0):
        if not name or not isinstance(price, (int, float)) or price <= 0:
            raise ValueError("Некорректные данные товара или цены")
        
        item_id = self.next_id
        self.next_id += 1
        
        record = {
            "name": name,
            "price": round(price, 2),
            "store": store,
            "discount": round(discount, 2) if discount else None,
            "history": []
        }
        
        self.items[item_id] = record
        return item_id

    def get_item(self, item_id):
        return self.items.get(item_id)
