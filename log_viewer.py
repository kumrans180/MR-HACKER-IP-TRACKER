import time, os

def narrate(text):
    os.system(f'espeak -v hi "{text}"')

print("📡 Real-time log viewer started...")
with open('logs.txt', 'r') as f:
    f.seek(0, 2)
    while True:
        line = f.readline()
        if line:
            print(f"\033[92m{line.strip()}\033[0m")
            narrate("Naya target track hua")
        time.sleep(1)
