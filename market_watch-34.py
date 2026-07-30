# === Stage 34: Добавь простую систему шаблонов для быстрого создания записей ===
# Project: MarketWatch
TEMPLATES = {
    "electronics": {"category": "electronics", "price_range": (50, 1000), "note": ""},
    "groceries": {"category": "groceries", "price_range": (50, 200), "note": ""},
    "books": {"category": "books", "price_range": (10, 500), "note": ""},
}

def create_from_template(template_name, name=None):
    if template_name not in TEMPLATES:
        print(f"Template '{template_name}' не найден. Доступные: {list(TEMPLATES.keys())}")
        return None
    tmpl = TEMPLATES[template_name]
    record = MarketRecord(name=name or f"{template_name} item", category=tmpl["category"], price_range=tmpl["price_range"])
    if name and not record.name.endswith(" item"):
        record.name = f"{name} ({record.category})"
    return record

def add_record_from_template(template_name, name=None):
    record = create_from_template(template_name, name)
    if record:
        print(f"Создана запись из шаблона '{template_name}'")
