import time, os
from datetime import datetime
from colorama import Fore, init

init(autoreset=True)
LOG_FILE = "logs.txt"

def cinematic_print(text, delay=0.02):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def read_logs():
    if not os.path.exists(LOG_FILE):
        print(Fore.RED + "❌ Log file not found.")
        return
    with open(LOG_FILE, "r", encoding="utf-8") as f:
        logs = f.read().split("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        for entry in logs:
            if entry.strip():
                print(Fore.GREEN + "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
                cinematic_print(entry.strip(), delay=0.005)
                print(Fore.GREEN + "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
                time.sleep(1)

def hindi_alert():
    now = datetime.now().strftime("%H:%M:%S")
    cinematic_print(Fore.YELLOW + f"🕵️‍♂️ नया विज़िटर ट्रेस किया गया — समय: {now}", delay=0.03)

if __name__ == "__main__":
    hindi_alert()
    read_logs()
