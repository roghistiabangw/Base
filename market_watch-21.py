# === Stage 21: Добавь простую систему напоминаний с датой выполнения ===
# Project: MarketWatch
import json, datetime

class Reminder:
    def __init__(self, product_id, date, message=""):
        self.product_id = product_id
        self.date = datetime.datetime.strptime(date, "%Y-%m-%d").date() if isinstance(date, str) else date
        self.message = message
        self.done = False

    @property
    def is_due(self):
        return not self.done and self.date <= datetime.date.today()

    @staticmethod
    def create(product_id, **kwargs):
        d = kwargs.get("date", "")
        if isinstance(d, str) and len(d) == 10:
            pass
        else:
            raise ValueError("Неверный формат даты")
        msg = kwargs.get("message", "")
        return Reminder(product_id, d, msg)

    def save(self):
        reminders_file = "data/notifications.json"
        if not os.path.exists(reminders_file):
            open(reminders_file, 'w').close()
        with open(reminders_file, 'r') as f:
            data = json.load(f) if f.readable() else []
        existing = [r for r in data if r["product_id"] == self.product_id and not r["done"]]
        if existing:
            existing[0].update(self.__dict__)
        else:
            data.append(self.__dict__)
        with open(reminders_file, 'w') as f:
            json.dump(data, f, indent=2)

    @staticmethod
    def check():
        reminders_file = "data/notifications.json"
        if not os.path.exists(reminders_file):
            return []
        with open(reminders_file, 'r') as f:
            data = json.load(f)
        return [Reminder(**r) for r in data if not r["done"] and r["date"] <= datetime.date.today()]

    def __repr__(self):
        status = "Готово" if self.done else ("Срочно!" if self.is_due else "Ожидание")
        return f"<Reminder {status}: {self.message} для товара {self.product_id}>"
