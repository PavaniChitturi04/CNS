def generate_playfair_matrix(key):
    key = key.upper().replace("J", "I")
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key_set = set(key)
    remaining_chars = [char for char in alphabet if char not in key_set]

    playfair_matrix = [list(key)]
    for i in range(5):
        row = []
        for j in range(5):
            if key:
                row.append(key[0])
                key = key[1:]
            else:
                row.append(remaining_chars[0])
                remaining_chars = remaining_chars[1:]
        playfair_matrix.append(row)

    return playfair_matrix

def find_positions(matrix, char):
    for i, row in enumerate(matrix):
        if char in row:
            return i, row.index(char)

def playfair_encrypt(plaintext, key):
    matrix = generate_playfair_matrix(key)
    plaintext = plaintext.upper().replace("J", "I")
    plaintext_pairs = [plaintext[i:i + 2] for i in range(0, len(plaintext), 2)]
    
    ciphertext = ""
    for pair in plaintext_pairs:
        if len(pair) == 1:  # Handle the case where the last pair has only one character
            pair += "X"
        row1, col1 = find_positions(matrix, pair[0])
        row2, col2 = find_positions(matrix, pair[1])

        if row1 == row2:
            ciphertext += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            ciphertext += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
        else:
            ciphertext += matrix[row1][col2] + matrix[row2][col1]

    return ciphertext

# Example usage:
plaintext = input("Enter the plain text: ")
key = "ldrp"
encrypted_text = playfair_encrypt(plaintext, key)

print("Original Text:", plaintext)
print("Encrypted Text:", encrypted_text)
