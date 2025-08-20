import webbrowser
import time

print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
mobile = input("🔍 Enter Mobile Number to trace: ")
print("📱 मोबाइल नंबर दर्ज किया गया:", mobile)
print("🌐 ब्राउज़र में GPS ट्रैकर खोला जा रहा है...")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

# Save mobile number temporarily (optional)
with open("mobile_temp.txt", "w") as f:
    f.write(mobile)

# Open browser to localhost tracker
webbrowser.open("http://localhost:5000")

time.sleep(2)
print("📍 कृपया ब्राउज़र में स्थान अनुमति दें ताकि ट्रैकिंग शुरू हो सके।")
print("🎯 HackmanX ethical tracking चालू है...")
