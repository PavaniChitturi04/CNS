
#Write a C/JAVA program to implementthe DES algorithm logic.


from pyDes import des, PAD_PKCS5, ECB

# Function to ensure the key is 8 bytes long
def validate_key(key):
    if len(key) != 8:
        raise ValueError("Key must be 8 bytes long (64 bits)")
    return key

# Function to ensure the data is a byte string
def validate_data(data):
    if not isinstance(data, bytes):
        raise TypeError("Data must be a byte string")
    return data

# Get user input for the key
key = input("Enter the key (must be 8 bytes long): ").encode('utf-8')
key = validate_key(key)

# Get user input for the data
data = input("Enter the data to be encrypted: ").encode('utf-8')
data = validate_data(data)

# Create DES object with the key
des_cipher = des(key, padmode=PAD_PKCS5, mode=ECB)

# Encrypt the data
encrypted_data = des_cipher.encrypt(data)

# Decrypt the encrypted data
decrypted_data = des_cipher.decrypt(encrypted_data)

# Convert bytes to hexadecimal for better visualization
encrypted_hex = encrypted_data.hex()
decrypted_text = decrypted_data.decode('utf-8')

# Display the output
print("Encrypted data (hexadecimal):", encrypted_hex)
print("Decrypted data:", decrypted_text)
