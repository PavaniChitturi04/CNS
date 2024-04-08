import hashlib

def calculate_md5(text):
    md5 = hashlib.md5()
    md5.update(text.encode('utf-8'))
    return md5.hexdigest()

# Example usage
text = input("Enter the text to calculate MD5 message digest: ")
md5_digest = calculate_md5(text)
print("MD5 Message Digest:", md5_digest)
