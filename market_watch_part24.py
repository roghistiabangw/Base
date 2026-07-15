# === Stage 24: Добавь компактный вывод одной записи с деталями ===
# Project: MarketWatch
def print_item_history(item_id):
    """Compact view of one item's history."""
    try:
        with open('marketwatch.txt', 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        return
    if not lines:
        return

    target = None
    for line in reversed(lines):
        stripped = line.strip()
        if stripped.startswith(f'item={item_id}:'):
            target = stripped
            break

    if not target:
        print("Item not found.")
        return

    parts = [p for p in target.split(' ') if p]
    while len(parts) < 7:
        parts.append('_')

    name, store, price, old_price, discount, history_count, last_change = (
        parts[0], parts[1], parts[2], parts[3], parts[4], parts[5], parts[6]
    )

    print(f"=== {name} ===")
    print(f"Store:     {store}")
    print(f"Price:     {price}")
    if old_price != '_':
        print(f"Old Price: {old_price}")
        disc = price - float(old_price)
        disc_pct = (disc / float(old_price)) * 100
        print(f"Discount:  {discount} ({disc_pct:.1f}%)")
    else:
        print("No previous price recorded.")

    if history_count != '_':
        print(f"History entries: {history_count}")
