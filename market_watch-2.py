# === Stage 2: Добавь модели данных и функции валидации пользовательского ввода ===
# Project: MarketWatch
class ValidationError(Exception):
    pass

def validate_price(price_str):
    try:
        price = float(price_str)
        if price < 0:
            raise ValidationError("Цена не может быть отрицательной")
        return price
    except ValueError:
        raise ValidationError("Некорректный формат цены")

def validate_store_name(name):
    if not name or len(name.strip()) == 0:
        raise ValidationError("Название магазина не может быть пустым")
    if len(name) > 100:
        raise ValidationError("Название магазина слишком длинное")
    return name.strip()

def validate_discount(discount_str):
    try:
        discount = float(discount_str)
        if discount < 0 or discount > 100:
            raise ValidationError("Скидка должна быть от 0 до 100 процентов")
        return discount
    except ValueError:
        raise ValidationError("Некорректный формат скидки")

def validate_product_name(name):
    if not name or len(name.strip()) == 0:
        raise ValidationError("Название товара не может быть пустым")
    if len(name) > 200:
        raise ValidationError("Название товара слишком длинное")
    return name.strip()

def validate_date(date_str):
    try:
        from datetime import datetime
        datetime.strptime(date_str, "%Y-%m-%d")
        return date_str
    except ValueError:
        raise ValidationError("Некорректный формат даты (ожидалось YYYY-MM-DD)")
