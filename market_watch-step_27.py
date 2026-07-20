# === Stage 27: Добавь функции сброса демо-данных и очистки состояния ===
# Project: MarketWatch
def reset_demo_data():
    """Сбросить все демо-данные в памяти и на диске."""
    global products, prices, stores, discounts, history, notifications
    for key in list(prices.keys()):
        del prices[key]
    for key in list(discounts.keys()):
        del discounts[key]
    history.clear()
    notifications.clear()

    # Заполнить демо-данные
    products = {
        "apple": {"name": "Яблоко", "category": "фрукты"},
        "banana": {"name": "Банан", "category": "фрукты"},
        "milk": {"name": "Молоко", "category": "молочка"},
    }
    stores = {
        "megamarket": {"name": "МегаМаркет", "location": "Москва"},
        "fresh": {"name": "Фреш", "location": "Санкт-Петербург"},
    }

    prices["apple"] = 50.0
    prices["banana"] = 35.0
    prices["milk"] = 89.0

    discounts["apple"] = {"store": "megamarket", "discount": 10}
    discounts["banana"] = {"store": "fresh", "discount": 20}

    history.append({
        "item": "apple",
        "price": prices["apple"],
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
    })
    history.append({
        "item": "banana",
        "price": prices["banana"],
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
    })

    notifications.append("Демо-данные сброшены и заполнены.")


def clear_state():
    """Полная очистка: удаляет все данные из памяти."""
    global products, prices, stores, discounts, history, notifications
    products.clear()
    prices.clear()
    stores.clear()
    discounts.clear()
    history.clear()
    notifications.clear()
