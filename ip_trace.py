# ip_trace.py
import requests, json, datetime

ip = input("🔍 Target IP डालें: ")
url = f"http://ip-api.com/json/{ip}"
res = requests.get(url).json()

print("\n🎯 Target Locked\n")
print(f"📍 Location     : {res['city']}, {res['regionName']}, {res['country']}")
print(f"🛰 Coordinates  : {res['lat']}, {res['lon']}")
print(f"🌐 ISP          : {res['isp']}")
print(f"🏢 Organization : {res['org']}")
print(f"🕒 Timezone     : {res['timezone']}")
print(f"📅 Timestamp    : {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# Save to logs.txt
with open("logs.txt", "a") as log:
    log.write(json.dumps(res, indent=2) + "\n\n")
