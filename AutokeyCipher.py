#Write a C/JAVA program to implement AutoKey Cipher

def generate_key(keyword, text):
    keyword = keyword.upper()
    keyword = list(keyword)
    if len(keyword) == len(text):
        return keyword
    else:
        for i in range(len(text) - len(keyword)):
            keyword.append(text[i])
    return ''.join(keyword)

def autokey_cipher_encrypt(plaintext, keyword):
    plaintext = plaintext.upper()
    keyword = keyword.upper()
    key = generate_key(keyword, plaintext)
    ciphertext = ''
    for i in range(len(plaintext)):
        if plaintext[i].isalpha():
            shift = (ord(plaintext[i]) + ord(key[i])) % 26
            ciphertext += chr(shift + 65)
        else:
            ciphertext += plaintext[i]
    return ciphertext

def autokey_cipher_decrypt(ciphertext, keyword):
    ciphertext = ciphertext.upper()
    keyword = keyword.upper()
    key = generate_key(keyword, ciphertext)
    plaintext = ''
    for i in range(len(ciphertext)):
        if ciphertext[i].isalpha():
            shift = (ord(ciphertext[i]) - ord(key[i]) + 26) % 26
            plaintext += chr(shift + 65)
            key += chr(shift + 65)
        else:
            plaintext += ciphertext[i]
            key += ciphertext[i]
    return plaintext

# Get user input for plaintext and keyword
plaintext = input("Enter the plaintext: ")
keyword = input("Enter the keyword: ")

# Encrypt the plaintext
encrypted_text = autokey_cipher_encrypt(plaintext, keyword)
print("Encrypted Text:", encrypted_text)

# Decrypt the ciphertext
decrypted_text = autokey_cipher_decrypt(encrypted_text, keyword)
print("Decrypted Text:", decrypted_text)
