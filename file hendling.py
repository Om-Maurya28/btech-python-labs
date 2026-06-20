def count_words(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            words = content.split()
            return len(words)
    except FileNotFoundError:
        return "File not found."

# Example usage
filename = input("Enter the file name: ")
result = count_words(filename)
print("Word Count:", result)

#without taking user input


def count_words():
    try:
        with open("test.txt", "r") as file:
            content = file.read()
            words = content.split()
            return len(words)
    except FileNotFoundError:
        return "File not found."
print("without taking user input")
print("Word Count:", count_words())
