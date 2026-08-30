# === Stage 42: Добавь цветной вывод через ANSI-коды с возможностью отключения ===
# Project: MarketWatch
ANSI_COLORS = {
    "red": "\033[31m", "green": "\033[32m", "yellow": "\033[33m",
    "blue": "\033[34m", "magenta": "\033[35m", "cyan": "\033[36m",
    "white": "\033[37m", "bold": "\033[1m", "reset": "\033[0m"
}

def colored(text, color):
    if not ENABLE_ANSI:
        return text
    return ANSI_COLORS.get(color, "") + text + ANSI_COLORS["reset"]

def info(msg):
    print(colored(msg, "cyan"))

def success(msg):
    print(colored(msg, "green"))

def warning(msg):
    print(colored(msg, "yellow"))

def error(msg):
    print(colored(msg, "red"))

def header(title):
    print(colored(f"=== {title} ===", "bold"))
