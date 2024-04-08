import string

def generate_substitution_key(seed=0):
    alphabet = list(string.ascii_lowercase)
    shuffled_alphabet = alphabet.copy()
    # Use seed for reproducibility
    if seed:
        import random
        random.seed(seed)
    random.shuffle(shuffled_alphabet)
    substitution_key = dict(zip(alphabet, shuffled_alphabet))
    return substitution_key

def encrypt(plaintext, substitution_key):
    ciphertext = ''
    for char in plaintext.lower():
        if char.isalpha():
            ciphertext += substitution_key[char]
        else:
            ciphertext += char
    return ciphertext

def decrypt(ciphertext, substitution_key):
    decryption_key = {v: k for k, v in substitution_key.items()}
    plaintext = ''
    for char in ciphertext.lower():
        if char.isalpha():
            plaintext += decryption_key[char]
        else:
            plaintext += char
    return plaintext

def main():
    seed = 42  # You can change this seed for a different substitution key
    substitution_key = generate_substitution_key(seed)

    plaintext = input("Enter the plain text: ")
    print("Original Text:   ", plaintext)

    ciphertext = encrypt(plaintext, substitution_key)
    print("Encrypted Text:  ", ciphertext)

    decrypted_text = decrypt(ciphertext, substitution_key)
    print("Decrypted Text:  ", decrypted_text)

if __name__ == "__main__":
    main()
