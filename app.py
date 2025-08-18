@app.route("/track", methods=["POST"])
def track_ip():
    ip = request.form.get("ip")
    try:
        geo = requests.get(f"https://ipinfo.io/{ip}/json").json()
        location = f"{geo.get('city','Unknown')}, {geo.get('country','Unknown')} ({geo.get('loc','Unknown')})"
        isp = geo.get('org', 'Unknown')
    except Exception:
        location = "Unknown"
        isp = "Unknown"
    result = f"""
    <h2>📍 ट्रेस रिज़ल्ट:</h2>
    <p>IP: {ip}</p>
    <p>स्थान: {location}</p>
    <p>ISP: {isp}</p>
    """
    return result
