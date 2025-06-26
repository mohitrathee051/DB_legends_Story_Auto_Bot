import cv2
import numpy as np
import os
import time
import pytesseract

TEMPLATE_FOLDER = "templates"

# ✅ Top row character coordinates (based on Realme 6 screenshot)
CHARACTER_COORDS = [
    (250, 1430),
    (460, 1430),
    (750, 1430)
]

# ✅ Templates for regular flow (not after start)
GENERAL_TEMPLATES = [
    "ok.png", "ok1.png","yes.png",
    "continue_playing.png", "skip.png", "tap.png", "play_demo.png"
]

# Take screenshot from phone
def take_screenshot():
    os.system("adb exec-out screencap -p > screen.png")
    return cv2.imread("screen.png")

# Simulate a screen tap using adb
def tap(x, y):
    os.system(f"adb shell input tap {x} {y}")
    print(f"[+] Tapped at ({x}, {y})")

# OCR text extractor
def extract_text(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return pytesseract.image_to_string(gray).lower()

# Match template with scaling
def smart_match_template(screen, template_path, threshold=0.78):
    try:
        template = cv2.imread(template_path, 0)
        screen_gray = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
        best_val, best_pos = 0, None

        for scale in [0.95, 1.0, 1.05]:
            resized = cv2.resize(template, (0, 0), fx=scale, fy=scale)
            result = cv2.matchTemplate(screen_gray, resized, cv2.TM_CCOEFF_NORMED)
            _, max_val, _, max_loc = cv2.minMaxLoc(result)

            if max_val > best_val:
                h, w = resized.shape
                best_val = max_val
                best_pos = (max_loc[0] + w // 2, max_loc[1] + h // 2)

        if best_val >= threshold:
            print(f"[✓] Matched {os.path.basename(template_path)} ({best_val:.2f})")
            return best_pos
    except Exception as e:
        print(f"[!] Template error: {e}")
    return None

# Match from a list
def match_any(screen, templates):
    for name in templates:
        path = os.path.join(TEMPLATE_FOLDER, name)
        pos = smart_match_template(screen, path)
        if pos:
            tap(*pos)
            time.sleep(1.5)
            return True
    return False

# Select 3 characters from top row and tap Ready
def select_characters_fixed():
    print("[🎯] Selecting top row characters...")
    for x, y in CHARACTER_COORDS:
        tap(x, y)
        time.sleep(1)

    # Tap Ready using template
    ready_path = os.path.join(TEMPLATE_FOLDER, "ready.png")
    screen = take_screenshot()
    pos = smart_match_template(screen, ready_path, threshold=0.75)
    if pos:
        tap(*pos)
        print("[🚀] Tapped Ready (via template)")
    else:
        print("[!] Ready button not found!")

    time.sleep(2)

# Main bot loop
def auto_story_bot():
    print("[🤖] Bot running — press Ctrl+C to stop")

    while True:
        try:
            screen = take_screenshot()
            time.sleep(1)

            # Check for character selection
            text = extract_text(screen)
            if "select your battle members" in text or "3 remaining" in text:
                select_characters_fixed()
                continue

            # Match start_battle.png first
            start_path = os.path.join(TEMPLATE_FOLDER, "start_battle.png")
            start_pos = smart_match_template(screen, start_path)
            if start_pos:
                tap(*start_pos)
                time.sleep(2)

                # Immediately check for yes.png only
                screen = take_screenshot()
                yes_path = os.path.join(TEMPLATE_FOLDER, "yes.png")
                pos = smart_match_template(screen, yes_path, threshold=0.75)
                if pos:
                    tap(*pos)
                    print("[→] Tapped Yes (after Start Battle)")
                    time.sleep(2)
                continue

            # General flow buttons
            match_any(screen, GENERAL_TEMPLATES)

            time.sleep(2.5)

        except KeyboardInterrupt:
            print("\n[🛑] Bot stopped by user.")
            break
        except Exception as e:
            print(f"[!] Error: {e}")
            time.sleep(2)

if __name__ == "__main__":
    auto_story_bot()
