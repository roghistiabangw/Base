# === Stage 6: Добавь фильтрацию записей по статусу, категории или тегам ===
# Project: MarketWatch
def filter_items(status=None, category=None, tags=None):
    filtered = []
    for item in items:
        if status is not None and item['status'] != status:
            continue
        if category is not None and item.get('category') != category:
            continue
        if tags is not None and set(item.get('tags', [])).isdisjoint(tags):
            continue
        filtered.append(item)
    return filtered
