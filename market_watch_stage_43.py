# === Stage 43: Добавь пагинацию длинных списков ===
# Project: MarketWatch
def paginate(items, page_size=10):
    """Compact pagination helper: splits a list into pages of page_size items."""
    pages = []
    for i in range(0, len(items), page_size):
        pages.append(items[i:i + page_size])
    return pages
