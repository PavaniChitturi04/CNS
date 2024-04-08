def mod_inverse(a, m):
    # Extended Euclidean Algorithm to find modular inverse
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def encrypt(plaintext):
    ciphertext = ''
    for char in plaintext:
        if char.isalpha():
            x = ord(char) - ord('A') if char.isupper() else ord(char) - ord('a')
            c = (3 * x + 12) % 26
            char_encrypted = chr(c + ord('A') if char.isupper() else c + ord('a'))
            ciphertext += char_encrypted
        else:
            ciphertext += char
    return ciphertext

def decrypt(ciphertext):
    plaintext = ''
    a_inverse = mod_inverse(3, 26)  # Modular inverse of 'a' (3) modulo 26
    for char in ciphertext:
        if char.isalpha():
            y = ord(char) - ord('A') if char.isupper() else ord(char) - ord('a')
            x = (a_inverse * (y - 12)) % 26
            char_decrypted = chr(x + ord('A') if char.isupper() else x + ord('a'))
            plaintext += char_decrypted
        else:
            plaintext += char
    return plaintext

# Example usage:
plaintext = input("Enter the plain text:")
encrypted_text = encrypt(plaintext)
decrypted_text = decrypt(encrypted_text)

print("Original Text:", plaintext)
print("Encrypted Text:", encrypted_text)
print("Decrypted Text:", decrypted_text)
