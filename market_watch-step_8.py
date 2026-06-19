# === Stage 8: Реализуй текстовый интерфейс команд с меню действий ===
# Project: MarketWatch
def show_menu():
    print("\n=== MarketWatch: Меню действий ===")
    print("1. Добавить наблюдение за товаром")
    print("2. Показать список всех товаров")
    print("3. Изменить цену товара в магазине")
    print("4. Удалить наблюдение по ID")
    print("5. Вывести историю изменений цены")
    print("6. Выйти из программы")
    try:
        choice = input("Введите номер действия (1-6): ").strip()
        return int(choice) if choice.isdigit() else None
    except ValueError:
        return None

def run_command_menu():
    while True:
        cmd = show_menu()
        if cmd is None: continue
        if cmd == 1: add_observation()
        elif cmd == 2: list_observations()
        elif cmd == 3: update_price()
        elif cmd == 4: delete_observation()
        elif cmd == 5: show_history()
        elif cmd == 6: print("Выход из MarketWatch."); break

if __name__ == "__main__":
    run_command_menu()
