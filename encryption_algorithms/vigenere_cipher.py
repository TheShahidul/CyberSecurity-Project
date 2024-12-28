def encrypt(text, key):
    key = key.upper()
    result = []
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index]) - ord('A')
            base = ord('A') if char.isupper() else ord('a')
            result.append(chr((ord(char) - base + shift) % 26 + base))
            key_index = (key_index + 1) % len(key)
        else:
            result.append(char)
    return ''.join(result)

def decrypt(cipher_text, key):
    key = key.upper()
    result = []
    key_index = 0
    for char in cipher_text:
        if char.isalpha():
            shift = ord(key[key_index]) - ord('A')
            base = ord('A') if char.isupper() else ord('a')
            result.append(chr((ord(char) - base - shift) % 26 + base))
            key_index = (key_index + 1) % len(key)
        else:
            result.append(char)
    return ''.join(result)
