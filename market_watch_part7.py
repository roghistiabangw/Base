# === Stage 7: Добавь сортировку записей по дате, приоритету и названию ===
# Project: MarketWatch
def sort_items(items, key='date', reverse=False):
    if key == 'date':
        return sorted(items, key=lambda x: x['timestamp'], reverse=reverse)
    elif key == 'priority':
        return sorted(items, key=lambda x: -x.get('priority', 0), reverse=True)
    elif key == 'name':
        return sorted(items, key=lambda x: x['name'].lower(), reverse=False)
    else:
        return items
