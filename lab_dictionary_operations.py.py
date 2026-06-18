# Create a dictionary
student = {
    "Name": "Om",
    "Age": 20,
    "Course": "BCA",
    "Marks": 85
}

# Iterate through dictionary
for key, value in student.items():
    print(key, ":", value)
string = input("Enter a string: ")

frequency = {}

for char in string:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

print("Character Frequency:")
for key, value in frequency.items():
    print(key, ":", value)
