# === Stage 26: Добавь набор демо-команд для быстрого ручного тестирования ===
# Project: MarketWatch
def demo_commands():
    print("\n=== MarketWatch Demo ===")
    db = Database()
    
    # Создаем демо-товары
    db.insert_product("iPhone 15", "Apple Store", 999, "tech")
    db.insert_product("Samsung Galaxy S24", "Samsung Official", 899, "tech")
    db.insert_product("MacBook Pro M3", "Best Buy", 1299, "tech")
    
    # Добавляем цены и скидки
    db.add_price(0, 950)
    db.add_price(1, 879)
    db.add_price(2, 1249)
    db.update_discount(0, 0.05)
    db.update_discount(1, 0.10)
    
    # Создаем магазины и скидки
    db.insert_store("TechHub", "Online")
    db.add_store_discount(0, 0.15)
    
    # Добавляем наблюдения
    db.add_watch(0, True, "best price")
    db.add_watch(1, False, "price drop")
    db.add_watch(2, True, "under $1200")
    
    # Получаем результаты
    results = db.get_all_watches()
    print(f"\nНаблюдения: {len(results)} активны")
    for r in results:
        if r['status'] == 'active':
            price_info = f"Текущая цена: ${r['price']}"
            discount_info = f", Скидка: {int(r['discount']*100)}%" if r['discount'] else ""
            print(f"  - {r['product_name']} в {r['store_name']}: {price_info}{discount_info}")

demo_commands()
