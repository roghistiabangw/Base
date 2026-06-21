# === Stage 9: Добавь импорт начальных данных из JSON-строки ===
# Project: MarketWatch
import json, os, random, time
from datetime import datetime, timedelta

INITIAL_DATA = '''
{
  "products": [
    {"id": 101, "name": "Смартфон X", "price": 45990, "currency": "RUB"},
    {"id": 102, "name": "Ноутбук Pro", "price": 89990, "currency": "RUB"},
    {"id": 103, "name": "Наушники Air", "price": 5490, "currency": "RUB"}
  ],
  "stores": [
    {"id": 201, "name": "М.Видео", "url": "https://mvideo.ru"},
    {"id": 202, "name": "DNS", "url": "https://dns-shop.ru"}
  ],
  "history_template": [
    {"product_id": 101, "store_id": 201, "price": 45990, "discount_percent": 0},
    {"product_id": 102, "store_id": 202, "price": 89990, "discount_percent": 5}
  ]
}'''

def load_initial_data():
    try:
        data = json.loads(INITIAL_DATA)
        products = {p["id"]: p for p in data.get("products", [])}
        stores = {s["id"]: s for s in data.get("stores", [])}
        
        history_records = []
        template_history = data.get("history_template", [])
        if template_history:
            base_time = datetime.now() - timedelta(days=30)
            for record in template_history:
                prod_id, store_id = record["product_id"], record["store_id"]
                price = products[prod_id]["price"] * (1 - record["discount_percent"]/100) if "discount_percent" in record else products[prod_id]["price"]
                
                history_records.append({
                    "id": len(history_records) + 1,
                    "product_id": prod_id,
                    "store_id": store_id,
                    "price": round(price, 2),
                    "discount_percent": record.get("discount_percent", 0),
                    "timestamp": base_time.strftime("%Y-%m-%d %H:%M:%S")
                })
        
        return products, stores, history_records
        
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON данных: {e}")
        return {}, {}, []

# Инициализация глобальных переменных данными из строки
PRODUCT_DB, STORE_DB, HISTORY_LOG = load_initial_data()
