# Sample dictionary
my_dict = {'apple': 5, 'banana': 2, 'orange': 8, 'grape': 3}

# Sort in ascending order
sorted_asc = dict(sorted(my_dict.items(), key=lambda item: item[1]))

# Sort in descending order
sorted_desc = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))

# Print sorted dictionaries
print("Ascending order:", sorted_asc)
print("Descending order:", sorted_desc)
