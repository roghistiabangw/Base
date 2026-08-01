# === Stage 36: Добавь проверку целостности данных и функцию ремонта простых проблем ===
# Project: MarketWatch
def check_and_repair(data):
    errors = []
    
    # Проверка: каждый товар в наблюдениях имеет корректный id и магазин
    for obs in data.get('observations', {}):
        oid = obs.get('id')
        if not oid or not isinstance(oid, int):
            errors.append(f"Некорректный ID наблюдения: {obs}")
            continue
        
        shop_id = obs.get('shop_id')
        if shop_id and (not isinstance(shop_id, int) or shop_id <= 0):
            errors.append(f"Некорректный shop_id в наблюдении {oid}: {shop_id}")
        
        # Проверка: цены и скидки — числа >= 0
        for key in ('price', 'discount'):
            val = obs.get(key)
            if val is not None and (not isinstance(val, (int, float)) or val < 0):
                errors.append(f"Некорректное {key} в наблюдении {oid}: {val}")
        
        # Проверка: история содержит корректные записи
        for hist in obs.get('history', []):
            if not isinstance(hist, dict) or 'timestamp' not in hist:
                errors.append(f"Некорректная запись истории в наблюдении {oid}: {hist}")
    
    # Проверка: данные магазинов корректны
    shops = data.get('shops', {})
    for shop_id, info in shops.items():
        if not isinstance(shop_id, int) or shop_id <= 0:
            errors.append(f"Некорректный ID магазина: {info}")
            continue
        if 'name' not in info or not isinstance(info['name'], str):
            errors.append(f"Магазин {shop_id} не имеет корректного имени")
    
    # Проверка: история изменений товаров
    changes = data.get('changes', {})
    for item_id, chg_list in changes.items():
        if not isinstance(item_id, int) or item_id <= 0:
            errors.append(f"Некорректный ID товара в изменениях: {chg_list}")
            continue
        for chg in chg_list:
            if not isinstance(chg, dict):
                errors.append(f"Некорректная запись изменений для товара {item_id}: {chg}")
    
    return errors
