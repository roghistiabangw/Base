# === Stage 14: Добавь генерацию краткой сводки по текущим данным ===
# Project: MarketWatch
def generate_summary(data):
    if not data: return "Нет данных для анализа."
    items = data.get("items", [])
    history = data.get("history", [])
    alerts = data.get("alerts", [])
    summary_lines = []
    summary_lines.append(f"Сводка MarketWatch ({len(items)} товаров, {len(history)} записей истории):")
    if items:
        avg_price = sum(i["price"] for i in items) / len(items)
        min_price = min(i["price"] for i in items)
        max_price = max(i["price"] for i in items)
        summary_lines.append(f"  Средняя цена: {avg_price:.2f}, Диапазон цен: от {min_price} до {max_price}.")
    if history:
        price_changes = [h["change_percent"] for h in history]
        avg_change = sum(price_changes) / len(price_changes)
        summary_lines.append(f"  Средняя динамика цены за период: {avg_change:+.2f}%.")
    if alerts:
        critical_alerts = [a for a in alerts if a.get("severity") == "critical"]
        warning_alerts = [a for a in alerts if a.get("severity") == "warning"]
        summary_lines.append(f"  Активных уведомлений: {len(alerts)} (критических: {len(critical_alerts)}, предупреждений: {len(warning_alerts)}).")
    else:
        summary_lines.append("  Активных уведомлений: нет.")
    return "\n".join(summary_lines)
