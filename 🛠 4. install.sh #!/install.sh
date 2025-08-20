#!/bin/bash

echo "🎬 HackmanX Setup Initiated..."
sleep 1

echo "🔧 Updating system packages..."
sudo apt update -y

echo "📦 Installing Python, pip, and espeak..."
sudo apt install python3 python3-pip espeak -y

echo "🐍 Installing Flask (Python web framework)..."
pip3 install flask

echo "🔊 Speaking confirmation..."
espeak -v hi "स्थापना सफल रही। अब आप एप्लिकेशन चला सकते हैं।"

echo "✅ Installation complete. Run with: python3 app.py"
