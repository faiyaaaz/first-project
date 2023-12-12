#Function to swap two numbers.

def swap(a, b):
    a,b = b,a
    return f"\nValue in function: {a} {b}"

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

x = print(swap(a, b))
print(f"\nValue in main: {a} {b}")
