<h1 align="center">🎮 Dragon Ball Legends Auto Story Bot</h1>
<p align="center">
  🤖 Automate story mode battles using ADB + Python + OpenCV — no APKs, no rooting, just pure safe automation.
</p>

---

## 📸 Demo

> Auto-selects characters → taps ready → starts battle → taps yes/ok → continues loop.

![screenshot](./templates/ready.png)
![screen](https://github.com/user-attachments/assets/177efb9a-d0e6-4f0f-9967-b98c86f84de1)

---

## 🛠 Tools Used

| Tool         | Purpose                                |
|--------------|----------------------------------------|
| ADB          | Take screenshots & simulate screen taps |
| Python       | Write logic, control loop               |
| OpenCV       | Match UI buttons via image templates    |
| Tesseract    | (Optional) OCR for screen recognition   |
| Ubuntu/Linux | Development environment                 |

---

## 🚀 Features

✅ Tap top 3 characters on selection screen  
✅ Click "Ready" using image detection  
✅ Tap "Start Battle" and automatically choose "Yes"  
✅ Tap "OK", "Skip", "Tap", "Continue" using template matching  
✅ Works 100% offline, no APKs or risky installs  
✅ No root required, just USB debugging enabled

---


---

## ⚙️ Setup Instructions

1. **Enable USB Debugging**  
   On your Android phone:
   - Go to Developer Options
   - Turn on "USB Debugging"

2. **Install ADB on Linux**
   ```bash
   sudo apt update
   sudo apt install android-tools-adb

3. **Create Python Virtual Environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install opencv-python pytesseract numpy
   sudo apt install tesseract-ocr

4. **Test Device Connection**
   ```bash
   adb devices

▶️ Run the Bot:python auto_story_bot.py

🔐 Is This Safe?
Yes. 100% Safe.
This project only uses:

✅ ADB commands for screenshots & taps

✅ Your own Python script

❌ No APKs

❌ No background services

❌ No root, no third-party apps

Once you're done, just disable USB Debugging for peace of mind.
 

