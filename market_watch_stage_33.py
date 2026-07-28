# === Stage 33: Добавь откат последнего действия там, где это разумно ===
# Project: MarketWatch
def undo_last():
    """Откат последнего действия: удаляет последнюю запись из истории наблюдений."""
    if history and history[-1]["action"] == "add":
        del history[-1]
        print("Undo: removed last observation.")
    elif history and history[-1]["action"] == "update_price":
        prev = history[-2]["price"] if len(history) > 1 else None
        current = history[-1]
        # Восстанавливаем предыдущую цену в текущем товаре и удаляем историю
        for item in items:
            if item["id"] == current["item_id"]:
                item["price"] = prev
                break
        del history[-1]
        print("Undo: reverted price update.")
    elif history and history[-1]["action"] == "update_store":
        prev = history[-2]["store_name"] if len(history) > 1 else None
        current = history[-1]
        for item in items:
            if item["id"] == current["item_id"]:
                item["store"] = prev
                break
        del history[-1]
        print("Undo: reverted store change.")
    elif history and history[-1]["action"] == "add_discount":
        discount_val = history[-1]["discount"]
        for item in items:
            if item["id"] == current["item_id"]:
                item["discount"] -= discount_val
                break
        del history[-1]
        print("Undo: reverted discount addition.")
    elif history and history[-1]["action"] == "remove_discount":
        for item in items:
            if item["id"] == current["item_id"]:
                item["discount"] += 50
                break
        del history[-1]
        print("Undo: reverted discount removal.")
    elif history and history[-1]["action"] == "remove_item":
        removed = history[-1]["name"]
        items[:] = [i for i in items if i["name"] != removed]
        del history[-1]
        print(f"Undo: re-added item '{removed}'.")
    else:
        print("Nothing to undo.")
