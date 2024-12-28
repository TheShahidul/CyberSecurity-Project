from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os

def encrypt(text, key):
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key.ljust(32)[:32].encode()), modes.CFB(iv))
    encryptor = cipher.encryptor()
    return (iv + encryptor.update(text.encode()) + encryptor.finalize()).hex()

def decrypt(cipher_text, key):
    cipher_text = bytes.fromhex(cipher_text)
    iv = cipher_text[:16]
    cipher_text = cipher_text[16:]
    cipher = Cipher(algorithms.AES(key.ljust(32)[:32].encode()), modes.CFB(iv))
    decryptor = cipher.decryptor()
    return (decryptor.update(cipher_text) + decryptor.finalize()).decode()
