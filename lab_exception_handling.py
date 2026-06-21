results = []

def divide_numbers(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except TypeError:
        print("Error: Invalid input type.")
    except Exception as e:
        print("Error:", e)
    else:
        print("Result =", result)
        results.append(result)
    finally:
        print("Execution completed.\n")

# User Input
try:
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))

    divide_numbers(x, y)

except ValueError:
    print("Error: Please enter valid numeric values.")

print("Stored Results:", results)
