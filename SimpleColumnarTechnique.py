import math

def encryptMessage(msg, key):
    cipher = ""

    # Calculate the number of columns based on the length of the key
    col = len(key)

    # Calculate the number of rows needed to accommodate the message
    row = int(math.ceil(len(msg) / col))

    # Add padding character '_' to fill the empty cells of the matrix
    msg += '_' * (row * col - len(msg))

    # Create the matrix and insert the message row-wise
    matrix = [msg[i:i+col] for i in range(0, len(msg), col)]

    # Read the matrix column-wise using the key
    for k in sorted(key):
        idx = key.index(k)
        cipher += ''.join(row[idx] for row in matrix)

    return cipher

def decryptMessage(cipher, key):
    msg = ""

    # Calculate the number of columns based on the length of the key
    col = len(key)

    # Calculate the number of rows needed to accommodate the ciphertext
    row = int(math.ceil(len(cipher) / col))

    # Create the matrix to store the deciphered message
    matrix = [[None] * col for _ in range(row)]

    # Arrange the matrix column-wise according to the key
    idx = 0
    for k in sorted(key):
        col_idx = key.index(k)
        for i in range(row):
            matrix[i][col_idx] = cipher[idx]
            idx += 1

    # Convert the matrix into a string
    for row in matrix:
        msg += ''.join(row)

    return msg.rstrip('_')

# Driver Code
if __name__ == "__main__":
    key = input("Enter the key: ")
    msg = input("Enter the message: ")

    cipher = encryptMessage(msg, key)
    print("Encrypted Message:", cipher)

    decrypted_msg = decryptMessage(cipher, key)
    print("Decrypted Message:", decrypted_msg)
