# === Stage 28: Добавь подсчёт ключевых метрик проекта ===
# Project: MarketWatch
def print_project_metrics():
    stores = set()
    products = set()
    price_records = 0
    discounts_applied = 0
    total_savings = 0.0
    for record in records:
        product_key = (record.product_name, record.store)
        if record.price is not None:
            price_records += 1
            if record.previous_price and record.previous_price != record.price:
                discount = (record.previous_price - record.price) / record.previous_price * 100
                discounts_applied += 1
                total_savings += (record.previous_price - record.price)
        stores.add(record.store)
        products.add(product_key)
    print(f"Unique stores: {len(stores)}")
    print(f"Unique product-store combos: {len(products)}")
    print(f"Price records collected: {price_records}")
    if discounts_applied > 0:
        avg_discount = total_savings / discounts_applied
        print(f"Avg discount in %: {avg_discount:.1f}")
        print(f"Total saved across watchers: {total_savings:.2f}")
