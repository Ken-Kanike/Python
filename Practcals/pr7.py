# 1. Create a tuple and find the minimum and maximum number from it.
my_tuple = (3, 8, 1, 6, 2, 9, 5)
minimum = min(my_tuple)
maximum = max(my_tuple)
print("Minimum number:", minimum)
print("Maximum number:", maximum)



# 2. Write a Python program to find the repeated items of a tuple.
tup=(1,3,4,32,2,2,2,2)
print("Duplicate items of tuple are : ", end=' ')
for i in tup:
    if tup.count(i)>1:
        print(i , end=' ')



# 3. Print the number in words for Example: 1234 => One Two Three Four
words=("zero","one","two","three","four")
numbers=[1,2,3,4,]
for num in numbers:
    print(num , " = " ,words[num])
    
