ip = input("🔍 Target IP दर्ज करें: ")
url = f"http://ip-api.com/json/{ip}"
res = requests.get(url).json()

if res['status'] == 'fail':
    print(f"\n🚫 IP trace असफल रहा — कारण: {res.get('message', 'Unknown error')}")
    exit()

print("\n🎯 Target Locked\n")
print(f"📍 Location     : {res['city']}, {res['regionName']}, {res['country']}")
print(f"🛰 Coordinates  : {res['lat']}, {res['lon']}")
print(f"🌐 ISP          : {res['isp']}")
print(f"🏢 Organization : {res['org']}")
print(f"🕒 Timezone     : {res['timezone']}")
print(f"📅 Timestamp    : {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
