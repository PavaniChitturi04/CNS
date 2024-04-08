def encrypt_vigenere(plaintext, key):
    ciphertext = ""
    key = key.upper()
    key_length = len(key)
    
    for i, char in enumerate(plaintext):
        if char.isalpha():
            key_char = key[i % key_length]
            shift = ord(key_char) - ord('A')
            
            if char.isupper():
                encrypted_char = chr((ord(char) + shift - ord('A')) % 26 + ord('A'))
            else:
                encrypted_char = chr((ord(char) + shift - ord('a')) % 26 + ord('a'))
            
            ciphertext += encrypted_char
        else:
            ciphertext += char
    
    return ciphertext

def decrypt_vigenere(ciphertext, key):
    plaintext = ""
    key = key.upper()
    key_length = len(key)
    
    for i, char in enumerate(ciphertext):
        if char.isalpha():
            key_char = key[i % key_length]
            shift = ord(key_char) - ord('A')
            
            if char.isupper():
                decrypted_char = chr((ord(char) - shift - ord('A')) % 26 + ord('A'))
            else:
                decrypted_char = chr((ord(char) - shift - ord('a')) % 26 + ord('a'))
            
            plaintext += decrypted_char
        else:
            plaintext += char
    
    return plaintext

# Example usage:
plaintext = input("Enter the plain text: ")
key = input("Enter the key: ")
encrypted_text = encrypt_vigenere(plaintext, key)
decrypted_text = decrypt_vigenere(encrypted_text, key)

print("Encrypted Text:", encrypted_text)
print("Decrypted Text:", decrypted_text)
