# === Stage 4: Добавь функцию редактирования существующих записей по идентификатору ===
# Project: MarketWatch
def edit_watch_item(item_id, new_data):
    if item_id not in watches:
        print(f"Ошибка: товар с ID {item_id} не найден.")
        return False
    
    existing = watches[item_id]
    
    # Обновляем только переданные поля, сохраняя остальные (например, историю)
    for key, value in new_data.items():
        if key in existing and value is not None:
            existing[key] = value
            
    print(f"Товар {item_id} успешно обновлен.")
    return True

if __name__ == "__main__":
    # Пример использования функции редактирования
    edit_watch_item(1, {"price": 950.00, "store_name": "Магазин Б"})
