# === Stage 20: Добавь восстановление записей из архива ===
# Project: MarketWatch
def restore_archive(archive_path, output_dir):
    """Восстанавливает записи из архива в формате pickle или JSON."""
    import json, os
    if archive_path.endswith('.json'):
        with open(archive_path) as f:
            data = json.load(f)
    elif archive_path.endswith('.pkl') or archive_path.endswith('.pickle'):
        import pickle
        with open(archive_path, 'rb') as f:
            data = pickle.load(f)
    else:
        raise ValueError("Поддерживаются только .json и .pkl файлы")
    
    restored = 0
    for item in data if isinstance(data, list) else [data]:
        target_path = os.path.join(output_dir, f"{item.get('id', 'unknown')}.json")
        with open(target_path, 'w') as f:
            json.dump(item, f, indent=2)
        restored += 1
    
    print(f"Восстановлено {restored} записей из архива.")
