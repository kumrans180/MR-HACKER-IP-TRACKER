import webbrowser
import os

print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
mobile = input("🔍 Enter Mobile Number to trace: ")

if not mobile or len(mobile) < 10:
    print("❌ कृपया वैध मोबाइल नंबर दर्ज करें।")
    exit()

print(f"📱 मोबाइल नंबर दर्ज किया गया: {mobile}")
print("🌐 ब्राउज़र में GPS ट्रैकर खुल रहा है...")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print("📍 कृपया ब्राउज़र में स्थान अनुमति दें ताकि ट्रैकिंग शुरू हो सके।")
print("🎯 HackmanX ethical tracking चालू है...")

try:
    os.system('espeak -v hi "मोबाइल नंबर दर्ज किया गया। GPS ट्रैकर चालू हो रहा है। कृपया स्थान अनुमति दें।"')
except:
    print("🔇 आवाज़ नहीं चल सकी, लेकिन ट्रैकर चालू है।")

webbrowser.open("http://localhost:5000/")
