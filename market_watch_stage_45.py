# === Stage 45: Добавь восстановление из резервной копии ===
# Project: MarketWatch
def restore_from_backup(self, backup_path):
        """Восстановление состояния из резервной копии.
        
        Загружает список наблюдений и историю из указанного файла.
        Возвращает количество восстановленных записей.
        """
        if not backup_path.endswith('.json'):
            raise ValueError("Файл резервной копии должен иметь расширение .json")
        
        try:
            with open(backup_path, 'r', encoding='utf-8') as f:
                backup_data = json.load(f)
        except FileNotFoundError:
            print(f"Ошибка: файл {backup_path} не найден")
            return 0
        except json.JSONDecodeError:
            print(f"Ошибка: некорректный формат JSON в {backup_path}")
            return 0
        
        try:
            self._observations = backup_data.get('observations', [])
            self._history = backup_data.get('history', [])
            self._last_updated = backup_data.get('last_updated', datetime.now().isoformat())
            print(f"Восстановлено {len(self._observations)} наблюдений из {backup_path}")
            return len(self._observations)
        except Exception as e:
            print(f"Ошибка восстановления: {e}")
            return 0
