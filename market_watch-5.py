# === Stage 5: Добавь удаление записей и аккуратную обработку отсутствующих идентификаторов ===
# Project: MarketWatch
def delete_record(record_id: int) -> bool:
    """Удаление записи по ID с проверкой существования."""
    if record_id not in _records:
        print(f"Ошибка: запись с id={record_id} не найдена.")
        return False
    
    del _records[record_id]
    print(f"Запись с id={record_id} успешно удалена.")
    return True

def get_missing_ids() -> list[int]:
    """Возвращает список отсутствующих идентификаторов для валидации."""
    expected = set(range(1, max(_records.keys()) + 2)) if _records else {0}
    missing = expected - set(_records.keys())
    return sorted(missing)
