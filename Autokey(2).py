class AutokeyCipher:
    def __init__(self):
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def encrypt(self, plaintext, key):
        plaintext = plaintext.upper()
        key = key.upper()
        ciphertext = ''
        key_index = 0

        for char in plaintext:
            if char in self.alphabet:
                # Add the key letter to the plaintext letter
                encrypted_char = self.alphabet[(self.alphabet.index(char) + self.alphabet.index(key[key_index])) % 26]
                ciphertext += encrypted_char

                # Update the key for the next iteration
                key += char
                key_index += 1
            else:
                ciphertext += char

        return ciphertext
    
    def decrypt(self, ciphertext, key):
        ciphertext = ciphertext.upper()
        key = key.upper()
        plaintext = ''
        key_index = 0

        for char in ciphertext:
            if char in self.alphabet:
                # Subtract the key letter from the ciphertext letter
                decrypted_char = self.alphabet[(self.alphabet.index(char) - self.alphabet.index(key[key_index])) % 26]
                plaintext += decrypted_char

                # Update the key for the next iteration
                key += plaintext[-1]
                key_index += 1
            else:
                plaintext += char

        return plaintext

if __name__ == "__main__":
    autokey_cipher = AutokeyCipher()

    
    # Example usage:
    plaintext = input("Enter the plain text: ")
    key = input("Enter the key: ")

    encrypted_text = autokey_cipher.encrypt(plaintext, key)
    print("Encrypted:", encrypted_text)

    decrypted_text = autokey_cipher.decrypt(encrypted_text, key)
    print("Decrypted:", decrypted_text)
