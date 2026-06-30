# === Stage 16: Добавь расчёт месячной статистики по датам ===
# Project: MarketWatch
def calculate_monthly_stats(history):
    from collections import defaultdict
    stats = defaultdict(lambda: {'min': float('inf'), 'max': -float('inf'), 'avg': 0, 'count': 0})
    for item in history:
        if not isinstance(item.get('date'), str) or len(item['date']) < 7: continue
        month_key = item['date'][:7]
        price = item.get('price')
        if price is None: continue
        try:
            val = float(price)
        except (TypeError, ValueError):
            continue
        stats[month_key]['min'] = min(stats[month_key]['min'], val)
        stats[month_key]['max'] = max(stats[month_key]['max'], val)
        stats[month_key]['avg'] += val
        stats[month_key]['count'] += 1
    for month in sorted(stats.keys()):
        data = stats[month]
        if data['count'] > 0:
            data['avg'] /= data['count']
            del data['min'], data['max'] # optional cleanup, keep only avg and count if needed
            yield {**data, 'month': month}
