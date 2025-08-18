# MR-HACKER-IP-TRACKER

## Features
- Jab koi aapke server ka link open karta hai, uska IP, approx city/country, device info log ho jata hai.
- Web page par "Share Exact Location" button hai—agar user permission de, to exact latitude/longitude bhi log ho jata hai.
- Logs `logs.txt` me save hote hain.

## Kaise Use Karein (Setup Guide)

### 1. GitHub Par Repository Banayein
- Apne GitHub account par login karein
- "New" par click karein, repo ka naam dalein: **MR-HACKER-IP-TRACKER**
- Public/private jo chahiye select karein, fir "Create repository" click karein

### 2. Files Add Karein
- Saare upar diye gaye files ko copy karein (app.py, index.html, requirements.txt, README.md)
- GitHub web editor ya apne PC par bana kar repo me upload karein

### 3. Server Ko Chalayein
- Apne system par Python aur pip install ho (Kali, Termux, Windows sab pe chalega)
- Terminal me yeh commands chalayein:
    ```
    pip install -r requirements.txt
    python app.py
    ```
- Server chal jayega. URL hoga: `http://localhost:5000` ya `http://<aapka-ip>:5000`

### 4. Link Share Karein
- Apne server ka IP ya ngrok se public link banao (jaise `http://your-ip:5000`)
- Jab koi link open karega, uska info `logs.txt` me save ho jayega
- "Share Exact Location" button se latitude/longitude bhi milega (agar user permission de)

### 5. Logs Dekhein
- Sare logs `logs.txt` file me milenge

## Note
- Exact location tabhi milegi jab user browser permission dega
- Illegal use na karein. Educational/knowledge ke liye hi use karein

## Files List
- app.py
- index.html
- requirements.txt
- README.md
- logs.txt (auto create ho jayegi)
