def autokey_encryption(msg, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    length = len(msg)

    # Generating the keystream
    new_key = key + msg
    new_key = new_key[:len(new_key) - len(key)]
    encrypted_msg = ""

    # Applying encryption algorithm
    for x in range(length):
        first = alphabet.index(msg[x])
        second = alphabet.index(new_key[x])
        total = (first + second) % 26
        encrypted_msg += alphabet[total]

    return encrypted_msg


def autokey_decryption(msg, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    current_key = key
    decrypted_msg = ""

    # Applying decryption algorithm
    for x in range(len(msg)):
        get1 = alphabet.index(msg[x])
        get2 = alphabet.index(current_key[x])
        total = (get1 - get2) % 26
        total = (total + 26) if total < 0 else total
        decrypted_msg += alphabet[total]
        current_key += alphabet[total]

    return decrypted_msg


# Example usage:
msg = input("Enter the plain text: ")
key = input("Enter the key: ")

encrypted_msg = autokey_encryption(msg, key)
decrypted_msg = autokey_decryption(encrypted_msg, key)

print(f"Encrypted: {encrypted_msg}")
print(f"Decrypted: {decrypted_msg}")
