# === Stage 30: Добавь поддержку нескольких пользовательских профилей внутри приложения ===
# Project: MarketWatch
def show_profiles():
    print("\n=== Управление профилями ===")
    for i, p in enumerate(profiles):
        print(f"  [{i+1}] {p['name']} — наблюдают: {len(p['watchlist'])}")


def create_profile(name=""):
    if not name:
        name = input("Имя профиля: ") or "Новый профиль"
    for p in profiles:
        if p["name"] == name:
            print("Такое имя уже занято.")
            return False
    new = {"id": len(profiles) + 1, "name": name, "watchlist": {}}
    profiles.append(new)
    current_profile_id = new["id"]
    print(f"Профиль '{name}' создан. ID: {current_profile_id}")
    return True


def delete_profile(idx):
    idx -= 1
    if not profiles or idx < 0 or idx >= len(profiles):
        print("Неверный номер профиля.")
        return False
    name = profiles[idx]["name"]
    for p in profiles:
        if p["id"] == profiles[idx]["id"]:
            del p["watchlist"]
    profiles.pop(idx)
    print(f"Профиль '{name}' удалён.")
    return True


def switch_profile(idx):
    idx -= 1
    if not profiles or idx < 0 or idx >= len(profiles):
        print("Неверный номер профиля.")
        return False
    current_profile_id = profiles[idx]["id"]
    print(f"Переключён на профиль: {profiles[idx]['name']}")


def watchlist_for_profile(idx, action, item_name="", price=None, store=""):
    idx -= 1
    if not profiles or idx < 0 or idx >= len(profiles):
        print("Неверный номер профиля.")
        return False
    profile = profiles[idx]
    wl = profile["watchlist"]
    if action == "add":
        wl[item_name] = {"price": price, "store": store}
        print(f"Добавлен '{item_name}' в профиль {profile['name']}")
    elif action == "remove":
        if item_name in wl:
            del wl[item_name]
            print(f"Удалён '{item_name}' из профиля {profile['name']}")
        else:
            print("Товар не найден в этом профиле.")
