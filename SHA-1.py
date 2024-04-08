import hashlib

def calculate_sha1(text):
    sha1 = hashlib.sha1()
    sha1.update(text.encode('utf-8'))
    return sha1.hexdigest()

# Example usage
text = input("Enter the text to calculate SHA-1 message digest: ")
sha1_digest = calculate_sha1(text)
print("SHA-1 Message Digest:", sha1_digest)
