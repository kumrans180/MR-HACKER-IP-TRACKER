#!/bin/bash
echo "🔧 Installing dependencies..."
sudo apt update
sudo apt install python3 python3-pip espeak -y
pip3 install flask
echo "✅ Installation complete. Run with: python3 app.py"
