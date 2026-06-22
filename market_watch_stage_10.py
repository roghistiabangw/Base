# === Stage 10: Добавь экспорт текущего состояния в JSON-строку ===
# Project: MarketWatch
def export_to_json():
    import json
    from datetime import datetime
    data = {
        "timestamp": datetime.utcnow().isoformat(),
        "items": items,
        "history": history
    }
    return json.dumps(data, ensure_ascii=False, indent=2)
