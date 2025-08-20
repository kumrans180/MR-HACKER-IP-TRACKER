# ip_trace.py — HackmanX Cinematic IP Tracer
import requests, datetime, os

# 🎯 Input
ip = input("🔍 Target IP दर्ज करें: ")
url = f"http://ip-api.com/json/{ip}"
res = requests.get(url).json()

# 🚫 Error Handling
if res['status'] == 'fail':
    print(f"\n🚫 IP trace असफल रहा — कारण: {res.get('message', 'Unknown error')}")
    try:
        os.system('espeak -v hi "आईपी पता अमान्य है। कृपया पुनः प्रयास करें।" > /dev/null 2>&1')
    except:
        pass
    exit()

# 🎙️ Hindi Narration (Optional)
try:
    os.system('espeak -v hi "लक्ष्य का आईपी पता प्राप्त हो गया है। स्थान लॉक किया जा रहा है।" > /dev/null 2>&1')
except:
    pass

# 🎨 Cinematic Output
print("\n🎯 Target Locked\n")
print(f"📍 Location     : {res['city']}, {res['regionName']}, {res['country']}")
print(f"🛰 Coordinates  : {res['lat']}, {res['lon']}")
print(f"🌐 ISP          : {res['isp']}")
print(f"🏢 Organization : {res['org']}")
print(f"🕒 Timezone     : {res['timezone']}")
timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(f"📅 Timestamp    : {timestamp}")

# 📁 Save to logs.txt
log_entry = f"{timestamp} - IP: {ip} | Location: {res['city']}, {res['regionName']}, {res['country']} | ISP: {res['isp']}\n"
with open("logs.txt", "a", encoding="utf-8") as log:
    log.write(log_entry)
