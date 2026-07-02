# === Stage 17: Добавь группировку записей по категориям ===
# Project: MarketWatch
def group_by_category(records):
    from collections import defaultdict
    grouped = defaultdict(list)
    for record in records:
        cat = record.get('category', 'Uncategorized')
        grouped[cat].append(record)
    return dict(sorted(grouped.items()))
