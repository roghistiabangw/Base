# === Stage 19: Добавь функцию архивации завершённых или старых записей ===
# Project: MarketWatch
def archive_old_records(db, cutoff_days=30):
    from datetime import datetime, timedelta
    today = datetime.now()
    cutoff_date = today - timedelta(days=cutoff_days)
    archived_count = 0
    with db.cursor() as cursor:
        cursor.execute("SELECT id FROM products WHERE last_seen < %s", (cutoff_date.isoformat(),))
        old_ids = [row[0] for row in cursor.fetchall()]
        if not old_ids: return
        cursor.executemany(
            "UPDATE products SET status='archived', last_seen=%s, archived_at=%s WHERE id=?",
            [(cutoff_date.isoformat(), today.isoformat()) for _ in old_ids]
        )
        db.commit()
        print(f"Archived {len(old_ids)} records older than {cutoff_days} days.")
