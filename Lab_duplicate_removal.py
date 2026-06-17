# Function to remove duplicates from a list

def remove_duplicates(data):
    unique_list = []

    for item in data:
        if item not in unique_list:
            unique_list.append(item)

    return unique_list


# Function to remove duplicates (case-insensitive for strings)

def remove_duplicates_case_insensitive(data):
    unique_list = []
    seen = set()

    for item in data:
        # Convert strings to lowercase for comparison
        key = item.lower() if isinstance(item, str) else item

        if key not in seen:
            seen.add(key)
            unique_list.append(item)

    return unique_list


# Accept input from user
user_input = input(
    "Enter elements separated by commas (e.g., 10,20,Vapi,vapi,30): "
)

items = []

for value in user_input.split(","):
    value = value.strip()

    # Convert numeric values to int if possible
    try:
        items.append(int(value))
    except ValueError:
        items.append(value)

result = remove_duplicates_case_insensitive(items)

print("Original List :", items)
print("List after removing duplicates :", result)
