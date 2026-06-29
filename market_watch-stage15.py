# === Stage 15: Добавь расчёт недельной статистики по датам ===
# Project: MarketWatch
def calculate_weekly_stats(history):
    from datetime import date, timedelta
    if not history: return {}
    stats = {}
    for entry in history:
        d = date.fromisoformat(entry['date'])
        week_key = (d - timedelta(days=d.weekday())).strftime('%Y-%W')
        if week_key not in stats: stats[week_key] = {'min': float('inf'), 'max': 0, 'sum': 0, 'count': 0}
        price = entry['price']
        stats[week_key]['min'] = min(stats[week_key]['min'], price)
        stats[week_key]['max'] = max(stats[week_key]['max'], price)
        stats[week_key]['sum'] += price
        stats[week_key]['count'] += 1
    return {k: {**v, 'avg': v['sum']/v['count']} for k, v in stats.items()}
