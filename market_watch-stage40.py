# === Stage 40: Добавь CLI-параметры через argparse для основных операций ===
# Project: MarketWatch
import sys

def main():
    parser = argparse.ArgumentParser(description="MarketWatch CLI")
    sub = parser.add_subparsers(dest="cmd", required=True)
    watch = sub.add_parser("watch", help="добавить наблюдение")
    watch.add_argument("item", help="название товара")
    watch.add_argument("--price", type=float, required=True)
    watch.add_argument("--store", help="название магазина")
    watch.add_argument("--discount", type=float, help="скидка в %")
    buy = sub.add_parser("buy", help="отметить покупку")
    buy.add_argument("item", help="название товара")
    buy.add_argument("--price", type=float, required=True)
    buy.add_argument("--store", help="название магазина")
    buy.add_argument("--discount", type=float, help="скидка в %")
    history = sub.add_parser("history", help="показать историю")
    args = parser.parse_args()
    if args.cmd == "watch":
        item = Item(args.item, price=args.price, store=args.store, discount=args.discount)
        if args.store:
            store = Store(args.store)
            item.store = store
        if args.discount:
            discount = Discount(args.discount)
            item.discount = discount
        db = Database()
        db.add(item)
        print(f"Добавлено наблюдение за {args.item}")
    elif args.cmd == "buy":
        item = Item(args.item, price=args.price, store=args.store, discount=args.discount)
        if args.store:
            store = Store(args.store)
            item.store = store
        if args.discount:
            discount = Discount(args.discount)
            item.discount = discount
        db = Database()
        db.add(item)
        print(f"Отмечено: {args.item} куплено")
    elif args.cmd == "history":
        db = Database()
        db.show_all()

if __name__ == "__main__":
    main()
