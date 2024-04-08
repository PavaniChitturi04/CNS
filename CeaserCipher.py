def encrypt(plaintext, shift):
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():
            # Determine if the character is uppercase or lowercase
            is_upper = char.isupper()
            
            # Apply the Caesar cipher shift
            char = chr((ord(char) - ord('A' if is_upper else 'a') + shift) % 26 + ord('A' if is_upper else 'a'))
            
        encrypted_text += char
    return encrypted_text

def decrypt(ciphertext, shift):
    return encrypt(ciphertext, -shift)

def main():
    # Get input from the user
    plaintext = input("Enter the text to encrypt: ")
    shift = int(input("Enter the key value: "))

    # Encrypt the input
    encrypted_text = encrypt(plaintext, shift)
    print("Encrypted text:", encrypted_text)

    # Decrypt the encrypted text
    decrypted_text = decrypt(encrypted_text, shift)
    print("Decrypted text:", decrypted_text)

if __name__ == "__main__":
    main()
