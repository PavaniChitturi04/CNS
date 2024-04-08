def encrypt_caesar(plain_text, shift):
    encrypted_text = ""
    for char in plain_text:
        if char.isalpha():
            if char.islower():
                encrypted_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                encrypted_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            encrypted_text += char
    return encrypted_text

def main():
    message = input("Enter the message: ")
    shift = int(input("Enter the shift value: "))

    encrypted_message = encrypt_caesar(message, shift)
    print("Encrypted message:", encrypted_message)

if __name__ == "__main__":
    main()
