a = int(input("Enter the number: "))  # Convert input to int
b = int(input("Enter another number: "))  # Convert input to int

if a > 0 and b > 0:  # Use 'and' for logical AND
    c = a + b
    print(f"The sum of {a} and {b} is {c}")
else:
    print("Enter positive numbers")
