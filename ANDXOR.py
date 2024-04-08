def main():
    str_value = "Hello World"
    
    # AND Operation with 127
    str1_and = ''.join(chr(ord(char) & 127) for char in str_value)
    print("AND Operation Result:", str1_and)

    # XOR Operation with 127
    str3_xor = ''.join(chr(ord(char) ^ 127) for char in str_value)
    print("XOR Operation Result:", str3_xor)

    # OR Operation with 127
    str4_or = ''.join(chr(ord(char) | 127) for char in str_value)
    print("OR Operation Result:", str4_or)

if __name__ == "__main__":
    main()
