# === Stage 22: Добавь проверку просроченных напоминаний ===
# Project: MarketWatch
def check_expired_reminders():
    """Проверяет просроченные напоминания и выводит предупреждения."""
    expired = []
    for entry in reminders:
        if entry.get("reminder_date") and datetime.now() > entry["reminder_date"]:
            expired.append(entry)
    return expired
