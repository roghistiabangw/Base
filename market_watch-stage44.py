# === Stage 44: Добавь функцию резервного копирования файла данных ===
# Project: MarketWatch
def backup_data_file(filepath):
    """Создаёт резервную копию файла данных с меткой времени."""
    import os
    from datetime import datetime
    if not os.path.exists(filepath):
        return
    backup_path = filepath + ".bak_" + datetime.now().strftime("%Y%m%d_%H%M%S")
    try:
        shutil.copy2(filepath, backup_path)
        print(f"Резервная копия сохранена: {backup_path}")
    except Exception as e:
        print(f"Ошибка при создании резервной копии: {e}")
