#!/bin/bash
echo "🔧 Installing HackmanX-IP-Tracker dependencies..."
sudo apt update
sudo apt install python3-pip -y
pip3 install -r requirements.txt --break-system-packages
echo "✅ Setup complete!"
echo "🎬 Run with: python3 app.py"
