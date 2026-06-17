# Take input from user
num = int(input("Enter a number: "))

# Calculate square
square = num * num

# Print result
print("Square of the number is:", square)

# Take input from user
num = int(input("Enter a number: "))

# Calculate cube
cube = num * num * num

# Print result
print("Cube of the number is:", cube)

# Take input from user
num = int(input("Enter a number: "))

# Check for prime
if num <= 1:
    print("Not a Prime Number")
else:
    for i in range(2, num):
        if num % i == 0:
            print("Not a Prime Number")
            break
    else:
        print("Prime Number")

# Take input from user
num = int(input("Enter a number: "))

if num < 0:
    print("Factorial does not exist for negative numbers")
elif num == 0:
    print("Factorial is: 1")
else:
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i
    print("Factorial is:", fact)

# Take input from user
num = int(input("Enter a number: "))

if num <= 1:
    print("No prime factors")
else:
    print("Prime factors are:")

    # Divide by 2 first
    while num % 2 == 0:
        print(2)
        num = num // 2

    # Check for odd factors
    for i in range(3, int(num**0.5) + 1, 2):
        while num % i == 0:
            print(i)
            num = num // i

    # If remaining number is prime
    if num > 2:
        print(num)

