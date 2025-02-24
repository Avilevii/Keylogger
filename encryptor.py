# encryptor.py
from config import SECRET_KEY

def xor_encrypt_decrypt(data: str) -> str:
    """מצפין או מפענח את המחרוזת באמצעות XOR ומחזיר ייצוג Hex"""
    encrypted_bytes = [ord(char) ^ SECRET_KEY for char in data]
    return "".join(f"{byte:02x}" for byte in encrypted_bytes)  # ממיר ל-Hex

def xor_decrypt_hex(hex_data: str) -> str:
    """מפענח מחרוזת מוצפנת ב-Hex חזרה לטקסט"""
    bytes_list = [int(hex_data[i:i+2], 16) ^ SECRET_KEY for i in range(0, len(hex_data), 3)]
    return "".join(chr(byte) for byte in bytes_list)
