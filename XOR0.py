def main():
    str_value = "Hello World"
    str1 = [chr(ord(char) ^ 0) for char in str_value]
    
    print("Modified String:", ''.join(str1))

if __name__ == "__main__":
    main()
