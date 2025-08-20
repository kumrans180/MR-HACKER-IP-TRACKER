import time

while True:
    with open("logs.txt") as f:
        print(f.read())
    time.sleep(5)
    os.system("clear")
