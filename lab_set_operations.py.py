# Create two sets (taking input from user)

A = set(map(int, input("Enter elements of Set A separated by space: ").split()))
B = set(map(int, input("Enter elements of Set B separated by space: ").split()))

# 1. Intersection (Common elements)
intersection_set = A.intersection(B)

# 2. Union (All unique elements)
union_set = A.union(B)

print("Intersection of A and B:", intersection_set)
print("Union of A and B:", union_set)

# 3. Add single item to Set A
single_item = int(input("Enter a single item to add to Set A: "))
A.add(single_item)
print("Set A after adding single item:", A)

# 4. Add multiple items to Set A
multiple_items = set(map(int, input("Enter multiple items to add separated by space: ").split()))
A.update(multiple_items)
print("Set A after adding multiple items:", A)
