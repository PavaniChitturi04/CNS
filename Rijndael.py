from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def rijndael_encrypt(key, plaintext):
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(plaintext)
    return ciphertext

def rijndael_decrypt(key, ciphertext):
    cipher = AES.new(key, AES.MODE_ECB)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext

def main():
    key = get_random_bytes(16)  # 128-bit key
    plaintext = b'This is a secret message.'

    encrypted = rijndael_encrypt(key, plaintext)
    decrypted = rijndael_decrypt(key, encrypted)

    print("Plaintext:", plaintext)
    print("Encrypted:", encrypted)
    print("Decrypted:", decrypted.decode('utf-8'))

if __name__ == "__main__":
    main()
