#Write a C/JAVA program to implement the Advanced Columnar Transposition technique

import numpy as np

# Define the encryption matrix and its inverse
encryption_matrix = np.array([[6, 24], [13, 16]])
decryption_matrix = np.array([[16, 8], [19, 5]])  # Inverse of the encryption matrix

# Function to encrypt plaintext
def hill_cipher_encrypt(plaintext):
    plaintext = plaintext.upper().replace(" ", "")
    # Pad the plaintext if its length is not even
    if len(plaintext) % 2 != 0:
        plaintext += "X"

    ciphertext = ""
    for i in range(0, len(plaintext), 2):
        # Convert pairs of letters to numerical vectors
        pair = [ord(char) - 65 for char in plaintext[i:i+2]]
        # Multiply the vector by the encryption matrix modulo 26
        result = np.dot(encryption_matrix, pair) % 26
        # Convert back to letters and append to the ciphertext
        ciphertext += ''.join(chr(char + 65) for char in result)
    
    return ciphertext

# Function to decrypt ciphertext
def hill_cipher_decrypt(ciphertext):
    plaintext = ""
    for i in range(0, len(ciphertext), 2):
        # Convert pairs of letters to numerical vectors
        pair = [ord(char) - 65 for char in ciphertext[i:i+2]]
        # Multiply the vector by the decryption matrix modulo 26
        result = np.dot(decryption_matrix, pair) % 26
        # Convert back to letters and append to the plaintext
        plaintext += ''.join(chr(char + 65) for char in result)
    
    return plaintext

# Example usage
def main():
    plaintext = input("enter the Plain Text:")
    encrypted_text = hill_cipher_encrypt(plaintext)
    print("Encrypted text:", encrypted_text)
    
    decrypted_text = hill_cipher_decrypt(encrypted_text)
    print("Decrypted text:", decrypted_text)

if __name__ == "__main__":
    main()
