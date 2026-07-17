# === Stage 25: Добавь обработку некорректных дат и понятные сообщения об ошибках ===
# Project: MarketWatch
def parse_date(date_str):
    """Парсит дату из строки, возвращая datetime или None с ошибкой."""
    import datetime
    formats = [
        "%Y-%m-%d", "%d.%m.%y", "%d.%m.%Y",
        "%Y/%m/%d", "%d.%b.%Y", "%d %B %Y"
    ]
    for fmt in formats:
        try:
            return datetime.datetime.strptime(date_str, fmt)
        except ValueError:
            continue
    raise ValueError(f"Некорректная дата: '{date_str}'. Используйте формат YYYY-MM-DD или DD.MM.YYYY.")

def validate_prices(prices):
    """Проверяет список цен на корректность."""
    valid = []
    for i, price in enumerate(prices):
        try:
            p = float(price)
            if p <= 0:
                raise ValueError("Цена не может быть нулевой или отрицательной")
            valid.append(p)
        except (ValueError, TypeError) as e:
            raise ValueError(f"Ошибка в цене [{i}]: '{price}' — {e}")
    return valid

def validate_shop(shop_name):
    """Проверяет название магазина."""
    if not shop_name or not isinstance(shop_name, str):
        raise ValueError("Название магазина должно быть непустой строкой")
    if len(shop_name) > 100:
        raise ValueError("Название магазина не может превышать 100 символов")

def validate_item(item_dict):
    """Полная проверка товара перед добавлением."""
    required = ["name", "price", "date"]
    for key in required:
        if key not in item_dict:
            raise ValueError(f"Отсутствует обязательное поле: '{key}'")

    name = item_dict["name"]
    price = item_dict["price"]
    date = item_dict["date"]

    validate_shop(name)
    parsed_date = parse_date(date)
    if parsed_date is None:
        raise ValueError(f"Некорректная дата: '{date}'")

    return {"name": name, "price": price, "date": parsed_date}
