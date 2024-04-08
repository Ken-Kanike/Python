# 1. Write a Python program to sum all the items in a list.

#take uer input
my_list = []
num = int(input("Enter the length of list:"))
for n in range(num):
    number = int(input(f"Enter { n+1 } element of list: "))
    my_list.append(number)
total = sum(my_list)
print("Sum of all items in the list:", total)

# or
my_list = [1, 2, 3, 4, 5]
total = sum(my_list)
print("Sum of all items in the list:", total)


# 2. Write a Python program to multiplies all the items in a list.
my_list = [1, 2, 3, 4, 5]
result = 1
for item in my_list:
    result *= item
print("Multiplication of all items in the list:", result)


# 3. Write a Python program to get the largest number from a list.
my_list = [10, 30, 20, 50, 40]
largest = max(my_list)
print("Largest number in the list:", largest)


# 4. Write a Python program to get the smallest number from a list.
my_list = [10, 30, 20, 50, 40]
smallest = min(my_list)
print("Smallest number in the list:", smallest)


# 5. Write a Python program to reverse a list.
my_list = [1, 2, 3, 4, 5]
reversed_list = my_list[::-1]
print("Reversed list:", reversed_list)
#or
print("Reversed list:",my_list.reverse())


# 6. Write a Python program to find common items from two lists.
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

common_items = list(set(list1) & set(list2)) # or  list(set(list1).intersection(list2))
print("Common items from two lists:", common_items)


# 7. Write a Python program to select the even items of a list.
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_items = [item for item in my_list if item % 2 == 0]
print("Even items of the list:", even_items)
#or
evenList = []
for i in my_list:
    if i%2 == 0:
        evenList.append(i)
print("Even items of the list:", even_items)