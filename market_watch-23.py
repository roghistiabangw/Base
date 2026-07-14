# === Stage 23: Добавь форматированный вывод таблицей в консоль ===
# Project: MarketWatch
def print_table(headers, rows):
    col_widths = [max(len(str(h)), max((len(str(r[i])) for r in rows), default=0)) + 2 for i, h in enumerate(headers)]
    fmt = ' | '.join(f'{{:<{w}}}' for w in col_widths)
    print(fmt.format(*headers))
    print('-+-'.join('-' * w for w in col_widths))
    for row in rows:
        print(fmt.format(*[str(x) if x is not None else '' for x in row]))

if __name__ == '__main__':
    watch_list = WatchList()
    items = [
        Item('Apple iPhone 15', 'PriceTech.ru', 79900, 84900),
        Item('Samsung Galaxy S23', 'MegaStore.com', 64900, 69900),
        Item('Sony WH-1000XM5', 'AudioWorld.ru', 29900, 34900),
    ]
    for it in items:
        watch_list.add(it)

    print_table(
        ['ID', 'Товар', 'Магазин', 'Текущая цена', 'Ранняя цена', 'Скидка (%)'],
        [[i.id, i.name, i.store, f'{i.current_price:,}', f'{i.early_price:,}', f'{round((1 - i.current_price/i.early_price)*100):.1f}'] for i in watch_list],
    )

    print_table(
        ['ID', 'Товар', 'Магазин', 'Дата обновления'],
        [[i.id, i.name, i.store, i.last_updated.strftime('%Y-%m-%d %H:%M')] if hasattr(i, 'last_updated') else [i.id, i.name, i.store, 'N/A'] for i in watch_list],
    )

    print('\nИстория изменений:')
    history = [(1234567890, 'Apple iPhone 15', 'PriceTech.ru', 79900), (1234567891, 'Samsung Galaxy S23', 'MegaStore.com', 64900)]
    print_table(
        ['ID', 'Товар', 'Магазин', 'Цена'],
        history,
    )
