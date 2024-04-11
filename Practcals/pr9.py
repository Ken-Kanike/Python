# 1. Write a Python script to sort (ascending and descending) a dictionary by value.
my_dict = {'a': 5, 'b': 2, 'c': 8, 'd': 1}

# Sorting in ascending order by value
sorted_dict_asc = {k: v for k, v in sorted(my_dict.items(), key=lambda item: item[1])}
print("Sorted dictionary (ascending):", sorted_dict_asc)

# Sorting in descending order by value
sorted_dict_desc = {k: v for k, v in sorted(my_dict.items(), key=lambda item: item[1], reverse=True)}
print("Sorted dictionary (descending):", sorted_dict_desc)


# 2. Write a Python script to concatenate following dictionaries to create a new one.
# a. Sample Dictionary: 
# b. dic1 = {1:10, 2:20} 
# c. dic2 = {3:30, 4:40} 
# d. dic3 = {5:50,6:60}
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

# Concatenating dictionaries
new_dict = {**dic1, **dic2, **dic3}
print("Concatenated dictionary:", new_dict)

#or 
dic4 = {}
for d in( dic1 , dic2 , dic3):
    dic4.update(d)
print("Concatenated dictionary:", dic4)



# 3. Write a Python program to combine two dictionary adding values for common keys.
# a. d1 = {'a': 100, 'b': 200, 'c':300}
# b. d2 = {'a': 300, 'b': 200, 'd':400}
d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

combined_dict = {}

for key in d1:
    if key in d2:
        combined_dict[key] = d1[key] + d2[key]
    else:
        combined_dict[key] = d1[key]

for key in d2:
    if key not in d1:
        combined_dict[key] = d2[key]

print("Combined dictionary:", combined_dict)


# 4. Write a Python program to print all unique values in a dictionary.
# a. Sample Data: [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},{"VII":"S005"}, {"V":"S009"}, {"VIII":"S007"}]
L = [
    {"V": "S001"},
    {"V": "S002"},
    {"VI": "S001"},
    {"VI": "S005"},
    {"VII": "S005"},
    {"V": "S009"},
    {"VIII": "S007"}
]

print("original list:", L)

u_value = set(val for dic in L for val in dic.values())

print("unique values:", u_value)


# 5. Write a Python program to find the highest 3 values in a dictionary.

# Sorting the dictionary by values in descending order
sorted_dict_desc = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)

print("Highest 3 values in the dictionary:")
for i in range(3):
    print(sorted_dict_desc[i])
