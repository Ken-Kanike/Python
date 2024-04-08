# 1. Write a Python program to create a set, add member(s) in a set and remove one item from set.
# Create a set
my_set = {1, 2, 3, 4, 5}

# Add member(s) to the set
my_set.add(6)
my_set.update([7, 8])

# Remove one item from the set
removed = my_set.pop()

print("Updated set:", my_set)
print("Removed element : ",removed)



# 2. Write a Python program to perform following operations on set: intersection of sets, union of sets, set difference, symmetric difference, clear a set.
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Intersection of sets
intersection = set1.intersection(set2)
print("Intersection of sets:", intersection)

# Union of sets
union = set1.union(set2)
print("Union of sets:", union)

# Set difference
difference = set1.difference(set2)
print("Set difference (set1 - set2):", difference)

# Symmetric difference
symmetric_difference = set1.symmetric_difference(set2)
print("Symmetric difference:", symmetric_difference)

# Clear a set
set1.clear()
print("Set1 after clearing:", set1)



# 3. Write a Python program to find maximum and the minimum value in a set.
my_set = {3, 1, 6, 2, 5, 4}

# Maximum value in the set
maximum = max(my_set)

# Minimum value in the set
minimum = min(my_set)

print("Maximum value in the set:", maximum)
print("Minimum value in the set:", minimum)



# 4. Write a Python program to find the length of a set.
my_set = {1, 2, 3, 4, 5}

# Length of the set
length = len(my_set)

print("Length of the set:", length)

