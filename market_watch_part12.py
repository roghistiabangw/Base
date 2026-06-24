# === Stage 12: Добавь загрузку данных из локального JSON-файла с обработкой ошибок ===
# Project: MarketWatch
def load_from_json(filepath):
    import json
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if isinstance(data, list):
            return [MarketItem.from_dict(item) for item in data]
        elif isinstance(data, dict):
            return [MarketItem.from_dict(data)]
        else:
            print("Ошибка: Неверный формат JSON данных")
            return []
    except FileNotFoundError:
        print(f"Файл {filepath} не найден")
        return []
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON в файле {filepath}: {e}")
        return []
    except Exception as e:
        print(f"Неизвестная ошибка при загрузке файла {filepath}: {e}")
        return []
