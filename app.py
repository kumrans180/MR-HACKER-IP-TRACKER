from flask import Flask, render_template, request
import datetime, os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/log', methods=['POST'])
def log():
    data = request.json
    with open('logs.txt', 'a') as f:
        f.write(f"{datetime.datetime.now()} - {data}\n")
    os.system('espeak -v hi "Target mil gaya. Coordinates locked."')
    return {'status': 'logged'}

app.run(host='0.0.0.0', port=5000)
