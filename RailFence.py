def rail_fence_encrypt(plaintext, num_rails):
    fence = [[' ' for _ in range(len(plaintext))] for _ in range(num_rails)]

    
    index = 0
    for rail in range(num_rails):
        for i in range(len(plaintext)):
            if rail == (i % num_rails):
                fence[rail][i] = plaintext[index]
                index += 1

    
    plain_text = ''.join([''.join(row) for row in fence])
    fence = [[' ' for _ in range(len(plain_text))] for _ in range(num_rails)]


    for rail in range(num_rails):
        for i in range(len(plain_text)):
            fence[rail][i] = ' '

    
    index = 0
    for rail in range(num_rails):
        for i in range(len(plain_text)):
            if rail == (i % num_rails):
                fence[rail][i] = '*'
                index += 1

    
    index = 0
    for rail in range(num_rails):
        for i in range(len(plain_text)):
            if fence[rail][i] == '*':
                fence[rail][i] = plain_text[index]
                index += 1

    
    encrypted_text = ''
    for i in range(len(plain_text)):
        for rail in range(num_rails):
            if fence[rail][i] != ' ':
                encrypted_text += fence[rail][i]

    return encrypted_text

def rail_fence_decrypt(encrypted_text, num_rails):
    decrypted_text = rail_fence_encrypt(encrypted_text, num_rails)
    decrypted_text = rail_fence_encrypt(decrypted_text, num_rails)
    return decrypted_text


plaintext = "HELLOSAM"


num_rails = 4

encrypted_message = rail_fence_encrypt(plaintext, num_rails)

print("Encrypted Message:", encrypted_message)


decrypted_message = rail_fence_decrypt(encrypted_message, num_rails)

print("Decrypted Message:", decrypted_message)
