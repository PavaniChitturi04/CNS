def euclidean_algorithm(a, b):
    while b:
        a, b = b, a % b
    return a

# Example usage:
num1=int(input("enter a number1:"))
num2=int(input("enter a number2:"))


gcd = euclidean_algorithm(num1, num2)
print("GCD of", num1, "and", num2, "is:", gcd)
