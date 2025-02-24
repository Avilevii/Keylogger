def xor_encrypt_decrypt(data: str, key: int) -> str:
    """מצפין או מפענח טקסט באמצעות XOR"""
    return "".join(chr(ord(char) ^ key) for char in data)