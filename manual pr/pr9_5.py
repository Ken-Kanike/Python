# Sample dictionary
my_dict = {'a': 10, 'b': 30, 'c': 20, 'd': 40, 'e': 50}

# Sort the dictionary by values in descending order
sorted_dict = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)

# Extract the top three values
highest_three_values = sorted_dict[:3]

print("Highest three values:", highest_three_values)
