from pyDes import des, PAD_PKCS5, ECB

def encrypt_des(key, data):
    # Create a DES object with the key and ECB mode
    k = des(key, ECB, key, pad=None, padmode=PAD_PKCS5)
    # Encrypt the data
    encrypted_data = k.encrypt(data)
    return encrypted_data

def decrypt_des(key, data):
    # Create a DES object with the key and ECB mode
    k = des(key, ECB, key, pad=None, padmode=PAD_PKCS5)
    # Decrypt the data
    decrypted_data = k.decrypt(data)
    return decrypted_data

if __name__ == "__main__":
    # Take user input for the key (must be 8 bytes long)
    key = input("Enter the key (8 bytes): ").encode()
    if len(key) != 8:
        print("Key must be 8 bytes long.")
        exit(1)

    # Take user input for the plaintext
    plaintext = input("Enter the plaintext: ").encode()

    # Encrypt the plaintext
    encrypted_text = encrypt_des(key, plaintext)
    print("Encrypted:", encrypted_text.hex())

    # Decrypt the ciphertext
    decrypted_text = decrypt_des(key, encrypted_text)
    print("Decrypted:", decrypted_text.decode())
