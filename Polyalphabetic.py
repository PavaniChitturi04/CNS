#Write a C/JAVA program to implement polyalphabetic Cipher

def generate_vigenere_table():
    table = [[(chr((i + j) % 26 + ord('A'))) for j in range(26)] for i in range(26)]
    return table

def encrypt_vigenere(plaintext, key):
    table = generate_vigenere_table()
    plaintext = plaintext.upper()
    key = key.upper()
    ciphertext = ''
    key_index = 0
    for char in plaintext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')
            ciphertext += table[ord(char) - ord('A')][shift]
            key_index += 1
        else:
            ciphertext += char
    return ciphertext

def decrypt_vigenere(ciphertext, key):
    table = generate_vigenere_table()
    key = key.upper()
    plaintext = ''
    key_index = 0
    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')
            row = table[shift]
            plaintext += chr(row.index(char) + ord('A'))
            key_index += 1
        else:
            plaintext += char
    return plaintext

def main():
    plaintext = input("Enter the plaintext: ")
    key = input("Enter the key: ")
    encrypted_text = encrypt_vigenere(plaintext, key)
    print("Encrypted:", encrypted_text)
    
    decrypted_text = decrypt_vigenere(encrypted_text, key)
    print("Decrypted:", decrypted_text)

if __name__ == "__main__":
    main()
