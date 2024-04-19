#Write a C/JAVA program to implement Playfair Cipher with key ldrp

def generate_playfair_matrix(key):
    key = key.upper().replace('J', 'I')  # Convert to uppercase and replace 'J' with 'I'
    key = ''.join(dict.fromkeys(key))    # Remove duplicates
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    matrix = []
    for char in key + alphabet:
        if char not in matrix:
            matrix.append(char)
    # Create a 5x5 matrix
    playfair_matrix = [matrix[i:i+5] for i in range(0, 25, 5)]
    return playfair_matrix

def get_char_positions(matrix, char):
    positions = []
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                positions.append((i, j))
    return positions

def encrypt_playfair(plaintext, key):
    playfair_matrix = generate_playfair_matrix(key)
    plaintext = plaintext.upper().replace('J', 'I')  # Convert to uppercase and replace 'J' with 'I'
    plaintext = plaintext.replace(" ", "")         # Remove spaces
    # Handling odd-length plaintext
    if len(plaintext) % 2 != 0:
        plaintext += 'X'
    # Encrypt pairs of letters
    ciphertext = ""
    for i in range(0, len(plaintext), 2):
        char1, char2 = plaintext[i], plaintext[i+1]
        row1, col1 = get_char_positions(playfair_matrix, char1)[0]
        row2, col2 = get_char_positions(playfair_matrix, char2)[0]
        if row1 == row2:  # Same row
            ciphertext += playfair_matrix[row1][(col1 + 1) % 5]
            ciphertext += playfair_matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:  # Same column
            ciphertext += playfair_matrix[(row1 + 1) % 5][col1]
            ciphertext += playfair_matrix[(row2 + 1) % 5][col2]
        else:  # Forming a rectangle
            ciphertext += playfair_matrix[row1][col2]
            ciphertext += playfair_matrix[row2][col1]
    return ciphertext

def decrypt_playfair(ciphertext, key):
    playfair_matrix = generate_playfair_matrix(key)
    plaintext = ''
    for i in range(0, len(ciphertext), 2):
        char1, char2 = ciphertext[i], ciphertext[i+1]
        row1, col1 = get_char_positions(playfair_matrix, char1)[0]
        row2, col2 = get_char_positions(playfair_matrix, char2)[0]
        if row1 == row2:  # Same row
            plaintext += playfair_matrix[row1][(col1 - 1) % 5]
            plaintext += playfair_matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:  # Same column
            plaintext += playfair_matrix[(row1 - 1) % 5][col1]
            plaintext += playfair_matrix[(row2 - 1) % 5][col2]
        else:  # Forming a rectangle
            plaintext += playfair_matrix[row1][col2]
            plaintext += playfair_matrix[row2][col1]
    return plaintext

def main():
    plaintext = input("Enter the plaintext: ")
    key = "ldrp"
    ciphertext = encrypt_playfair(plaintext, key)
    print("Encrypted:", ciphertext)

    decrypted_text = decrypt_playfair(ciphertext, key)
    print("Decrypted:", decrypted_text)

if __name__ == "__main__":
    main()
