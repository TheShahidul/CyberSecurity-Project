def encrypt(text, key):
    key = int(key)  # Ensure key is an integer
    result = ""
    for char in text:
        if char.isalpha():
            shift = key % 26
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def decrypt(cipher_text, key):
    return encrypt(cipher_text, -int(key))
