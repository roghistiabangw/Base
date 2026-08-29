# === Stage 41: Добавь режим dry-run для операций изменения данных ===
# Project: MarketWatch
def dry_run_mode():
    """Включает режим dry-run для всех операций изменения данных.
    Все операции пишутся в историю, но не применяются к реальным данным."""
    global _data, _history, _dry_run
    _dry_run = True
    _data = {}
    _history = []

    def _apply_changes(changes):
        for item, changes_dict in changes.items():
            if item in _data:
                _data[item] = {**_data[item], **changes_dict}
            else:
                _data[item] = changes_dict

    _apply_changes(_history)
    return _data, _history


def dry_run_mode_off():
    """Выключает режим dry-run и применяет все изменения из истории."""
    global _data, _history, _dry_run
    _dry_run = False
    _data = {}
    _history = []

    def _apply_changes(changes):
        for item, changes_dict in changes.items():
            if item in _data:
                _data[item] = {**_data[item], **changes_dict}
            else:
                _data[item] = changes_dict

    _apply_changes(_history)
    return _data, _history
