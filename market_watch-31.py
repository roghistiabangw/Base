# === Stage 31: Добавь переключение активного пользовательского профиля ===
# Project: MarketWatch
def switch_profile(new_name: str) -> None:
    """Переключить активный профиль на имя new_name."""
    global active_profile
    if new_name not in profiles:
        raise ValueError(f"Профиль '{new_name}' не найден. Доступные: {list(profiles.keys())}")
    active_profile = new_name
