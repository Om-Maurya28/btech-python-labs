string = input("Enter a string: ")
reversed_string = string[::-1]

print("Reversed string:", reversed_string)
main_string = input("Enter the main string: ")
substring = input("Enter the substring to search: ")

if substring in main_string:
    print("Substring is present in the string.")
else:
    print("Substring is NOT present in the string.")
