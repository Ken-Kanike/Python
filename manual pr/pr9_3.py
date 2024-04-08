# Sample dictionaries
dict1 = {'a': 100, 'b': 200, 'c': 300}
dict2 = {'b': 300, 'c': 200, 'd': 400}

# Combine dictionaries by adding values for common keys
combined_dict = {}
for key in dict1:
    if key in dict2:
        combined_dict[key] = dict1[key] + dict2[key]
    else:
        combined_dict[key] = dict1[key]

for key in dict2:
    if key not in dict1:
        combined_dict[key] = dict2[key]

print(combined_dict)
