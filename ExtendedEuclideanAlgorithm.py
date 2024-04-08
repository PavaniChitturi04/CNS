def extended_euclidean_algorithm(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, x1, y1 = extended_euclidean_algorithm(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return gcd, x, y

# Example usage:
num1=int(input("enter a number1:"))
num2=int(input("enter a number2:"))

gcd, x, y = extended_euclidean_algorithm(num1, num2)
print("GCD of", num1, "and", num2, "is:", gcd)
print("Coefficients of Bézout's identity: x =", x, ", y =", y)
