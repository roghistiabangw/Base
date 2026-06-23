# === Stage 11: Добавь сохранение данных в локальный JSON-файл ===
# Project: MarketWatch
import json, os

def save_data(data):
    with open('marketwatch.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def load_data():
    if not os.path.exists('marketwatch.json'):
        return []
    try:
        with open('marketwatch.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []

def get_or_create_data():
    data = load_data()
    if not isinstance(data, list):
        save_data([])
        return []
    return data
