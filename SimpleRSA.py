import random

# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Function to find gcd of two numbers
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Function to find modular inverse using extended Euclidean algorithm
def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

# Function to generate RSA keys
def generate_rsa_keys(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError("Both numbers must be prime.")
    elif p == q:
        raise ValueError("p and q cannot be equal.")

    n = p * q
    phi = (p - 1) * (q - 1)

    # Choose e such that 1 < e < phi and gcd(e, phi) = 1
    e = random.randrange(1, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(1, phi)

    # Calculate d, the modular multiplicative inverse of e modulo phi
    d = mod_inverse(e, phi)

    return ((e, n), (d, n))

# Function to encrypt a message
def encrypt(public_key, plaintext):
    e, n = public_key
    encrypted_msg = [pow(ord(char), e, n) for char in plaintext]
    return encrypted_msg

# Function to decrypt a message
def decrypt(private_key, ciphertext):
    d, n = private_key
    decrypted_msg = [chr(pow(char, d, n)) for char in ciphertext]
    return ''.join(decrypted_msg)

# Main function
def main():
    p = int(input("Enter a prime number (p): "))
    q = int(input("Enter another prime number (q): "))

    public_key, private_key = generate_rsa_keys(p, q)

    message = input("Enter the message to encrypt: ")
    print("Original message:", message)

    encrypted_message = encrypt(public_key, message)
    print("Encrypted message:", encrypted_message)

    decrypted_message = decrypt(private_key, encrypted_message)
    print("Decrypted message:", decrypted_message)

if __name__ == "__main__":
    main()
