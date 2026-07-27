# === Stage 32: Добавь журнал действий пользователя ===
# Project: MarketWatch
class ActionLog:
    def __init__(self):
        self.log = []

    def record(self, action_type, details):
        entry = {
            'type': action_type,
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            **details
        }
        self.log.append(entry)

    def get_log(self):
        return list(reversed(self.log))

    def clear(self):
        self.log.clear()


def log_user_action(action_type, action_name, user_id=1):
    if not hasattr(user_data, 'action_log'):
        user_data.action_log = ActionLog()
    user_data.action_log.record(action_type, {'name': action_name})
