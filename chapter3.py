"""#list 
#creating list
l1 = [1,2,3,4,5,6,7,8]
l2= ["a","b","c","d"]

#accessing values of list
print(l1[3])
print(l1[0],l1[2]) 
print(l1[1:3])
print(l1)
print(l2)

#deleting values from list
a = l1.pop() # => returns last element
b = l1.pop(0) #  => returns element at 0 index
print(a , b)
l2.remove("a") # => removes specified element from list , does not return it
del l2[2]  # => deletes specified index element , does not returns it
del l1[1:3]  # => deletes specified range of index element , does not returns it
print(l1)
print(l2)

#updating a list
l1[1] = 8    # updates the value at index 1
l2[0] = "e"  # updates the value at index 1
print(l1)
print(l2)

#basic list operations
#traversing list
for i in l1:   # using for loop
    print(i)
for a in l2:
    print(a)    

for i in range(len(l1)):  # using range function
    l1[i]+= 1             # adding 1 at each index 

for item in enumerate(l1): # uing enumerate funtion to print both index and values
    print(item)
for a in enumerate(l2):
    print(a)


#concatenating list
l3 = l1 + l2
print(l3)

#repetion list
print(l2*3)

#finding length of list
print(len(l3))

#membership  
print( "a" in l2)  #  => cheks if a in l2
print( "c" in l2)

#slicing [start : end -1 : step]
print(l3)
print(l3[2:4])  # prints list elements from 2nd index upto 4th index (-1) i.e 3
print(l3[2:])  # prints list elements from 2nd index upto end
print(l3[:4])  # prints list elements from start upto upto 4th index (-1) i.e 3
print(l3[:])  # prints whole list
print(l3[len(l3):0:-1])  # prints list reverse ( not printing element at 0 index bec -1)

#list methods
print(l1)
l1.insert(0,-1)  # inserts element at 0th index  insert( index , element ) takes only 2 arguments
l1.append(20)  # appends 20 at the end of l1 , takes only 1 paramter element
l1.extend([30])  # appends a lisr at the end of l1 , takes only one list type object ( can contain multiple elements inside list but not in parameter])
l1.extend([40,50])
print(l1)

#sort
sorted(l1) #or l1.sort()
print(l1)

# built in list functions
print(all(l1))
print(any(l1))
print(len(l1))
print(max(l1))
print(min(l1))
print(sum(l1))

 
#list function  str  = > list or new list
str1 = "Hello"
print(list(str1))


#split function  str  = > list or new list
str2 = "This is python programming"
l5 = str2.split()
print( l5 )
print(str1.split())
str2 = "This#is#python#programming"
print(str2.split('#'))

#join   list => str
str = "**"
print(str.join(l5))

#WAP a list program to take n numbers input in list , get max , min , sum , avg from the formed list without using any built built in funxtion
mylist = []
n = int(input("Enter the size of list : "))
for i in range(n):
     mylist.append(int(input("Enter {} number in list :".format(i))))
print("formed list = ", mylist)

max_element = 0
for i in range(n):
    if mylist[i] > max_element:
        max_element = mylist[i]
print("max element of list : ", max_element)

min_element = mylist[0]
for i in range(n):
    if mylist[i] < min_element:
        min_element = mylist[i]
print("min element of list : ", min_element)

sum = 0
for i in range(n):
    sum += mylist[i]
avg = sum/n
print("Sum of list elements = ",sum)    
print("Avg of list elements = ",avg)    



#-------------------------------------------------------------------------------
#Tuples

#creating tuples
t1 = (1,2,3,4,5,6,7,8) # => tuple
print(type(t1))
t2 = (10)  # => int
print(type(t2))
t3 = (10,)  # => tuple
print(type(t3))

#accessing values of tuple
print(t1[3])
print(t1[0],t1[2]) 
print(t1[1:3])
print(t3)

#deleting tuple
#cant delete values of tuples , immutable
del t2;
try:
    print(t2)
except:
    print("Tuple t2 does not exist")


#udpating tuple
#cant update values of tuples , immutable
t2 = t1 + (9,)+ t3;
print(t2)

#basic tuple operations
#len
print(len(t2))

#cocatination => see updating sum

#repetion
print((10,20,30)*3)

#memberhsip
print(10 in t2)
print(20 in t2)


#traversing tuple
for i in t2:   # starts from 1st value in tuple ie 1
    print(i)
for i in range(len(t2)):  # starts from 0th index
    print("t2[",i,"] = ",t2[i])


#tuples built in functions
tup1 = (1,2,3)
tup2 =(1,2,4)

#cmp   
#tup1 < tup2 => -1
#tup1 = tup2 => 0
#tup1 > tup2 => 1
# print(cmp(t1,t2))... doesn't work!

#len
print(len(tup2))

#max
print(max(tup1 + tup2))

#min
print(tup2)

#tuple()
list1 = [1,2,3,4]
print(type(list1))
print(type(tuple(list1)))
print(tuple("hello"))




#-------------------------------------------------------------------------------
#Sets
s1 = {10,20,30,40,50}

#accessing sets => cant be accessed using index => unordered
print(s1)
for i in s1:
    print(i)


#deleting values from set
#remove
s1.remove(20)
print(s1)

#discard
s1.discard(50)
print(s1)

#del  => deletes whole set
del s1
try:
    print(s1)
except:
    print("Set s1 does not exist")

#updating set values
#add  takes only 1 element
s1 = {10,20}
s1.add(30)
s1.add(20) # => wont add same elements the already exists
print(s1)

#update  takes multiple elements in the form of sequence
s1.update([40, 50,60])
s1.update((70, 80,90))
s1.update({100, 120,110})
#s1.update(70, 80,90)  # THIS WONT WORK
print(s1)

#Basic set operations
set1 = {10,20,30}
set2 = {10,20,40}

#union |    => returns set with all elements ( no repitions)
print(set1.union(set2))
print(set1|set2)

#intersection &    => returns set with common elements from both set
print(set1.intersection(set2))
print(set1&set2)

#difference -    => ei (A - B) returns set with elements that are only in A and not same in B
print(set1.difference(set2))
print(set1-set2)

#symmetric difference ^    => returns set of all the elements in both set except common ones
print(set1.symmetric_difference(set2))
print(set1^set2)


#built in set function
print(all(set1))
print(any(set1))
print(len(set1))
print(max(set1))
print(min(set1))
print(sorted(set1))
print(sum(set1))

#enumaret => returns object with index , value
for i in enumerate(set1):
    print(i)




#-------------------------------------------------------------------------------
#Dictionaries
#creating dictionaries
d1 = {}
d2 = dict({"a":1,"b":2})
d3 = {1:'a',2:'b',3:'c',4:'d'}
d4 = {'a':1,'b':2,'c':3,'d':4}
d5 = {tuple('a'):1,tuple('b'):2,tuple('c'):3,tuple('d'):4}
d6 = {1:'a',"b":3,tuple("name"):"steve"}
print(type(d1))
print(type(d2))
print(type(d3))
print(type(d4))
print(type(d5))
print(type(d6))
print(d5)

#accessing values from dict
print(d2["a"])
print(d3[4])
print(d5[tuple('c')])


#traversing
for key,value in list(d4.items()):
    print(key ,":",value)

for key,value in list(d5.items()):
    print(key ,":",value)

for i in d3:
    print(i ,":",d3[i])

#deleting elements
del d5[tuple('d')]
del d4['d']
print(d4,d5)


#updating values 
d4['a'] = "apple"
d5[tuple('a')] = "banana"
print(d4,d5)

#basic dict operations
#adding
d4['d'] = "dog"
d5[tuple('d')] = "new"
print(d4)
print(d5)

#finding length
print(len(d5))


#built in dict functions
#clear
d5.clear()
print(d5)

#copy
d5 = d4.copy()  # as same as d5 = d2
print(d5)

#fromkeys()
keys = {1,2,3}
value = 'abcd'
new_d1 = dict.fromkeys(keys,value)  # value is set same to each element
print(new_d1)
new_d2 = dict.fromkeys(keys,list(value)) # value is set same to each element even in set or list
print(new_d2)

#get
print(d4.get('a'))
print(d4.get('a','apple'))

#values
print(d4.values())

#keys
print(d4.keys())

#pop
poped = d4.pop('a')
print("return value : ", poped)
print(d4)

poped2 = d4.pop("banana","scepecid value if key not present")
print(poped2)

poped3 = d4.popitem()   # returns last element
print("return value : ", poped3)   
print(d4)


#sorting 
new_d3 = {2:'b' ,4:'d',1:'a',3:'c'}
newlist = list(new_d3.keys())
newlist.sort()
sorted_d = {}
for i in newlist:
    sorted_d[i] = new_d3[i]
print(sorted_d)

#dict => tuple
new_tup = tuple(sorted_d.items())  # tuples having tuples inside
print( type(new_tup) ," : ",new_tup)

#dict => set
new_tup = set(sorted_d.items())   # set having tuples inside
print( type(new_tup) ," : ",new_tup)

#dict => list
new_tup = list(sorted_d.items())   # list having tuples inside
print( type(new_tup) ," : ",new_tup)




#-------------------------------------------------------------------------------
# Strings
str_country = "India"
print(str_country[0])
print(str_country[len(str_country)-1])

#string operations
#len
print(len(str_country))

#concatenation
str2 = str_country+" is my country."
print(str2)

#appending
str_country += " is in Asia."
print(str_country)

#repition
print("hello "*3)
print(str2*3)



#strings are immutable
try:
    str = "hello"
    str[0] = 'M'
except:
    print("'str' object does not support item assignment")
# we have to manipulate the above string by creating a new string to make desired changes
new_str = "M" + str[1:]
print(new_str)


#string formatting %
# %d => int
# %s => sequence
# %f => float .., ect
print("%d)The value of %s is %f" % (1,"PI",3.14))
demolist = [1,2,3,4,5]
for i in range(len(demolist)):
    print("list[%d] : %d" %(i , demolist[i]))
print("The whole list is %s" %(demolist))


#string build in functions  
str = "hello there"

#capitalize()  => 1st letter to cap
print(str.capitalize())

#count( countstr ) =>  returns number of times a letlter or a word occures in a string
print(str.count('e'))

#center( widh , filllchar)  => centers only single word with fillchar padding
print("Hello".center(10,"#"))

#endswith( value [, start , end] ) => returns  true if ends with 
print(str.endswith('e'))
print(str.endswith('e',3))
print(str.endswith('e',3,4))

#find() => returns index of 1st occurance
print(str.find('there'))

#index() => returns index of 1st occurance
print(str.index('there'))

#isalpha => returns true if all string characters are alphabet
print("hello".isalpha())
print("hello123".isalpha())

#isdigit => returns true if all string characters are digits
print("1234".isdigit())
print("hello123".isdigit())
print("20 -1 32".isdigit())

#isdecimal => returns true if all string characters are decimal (0-9)
print("1234".isdecimal())
print("hello123".isdecimal())
print("20 -1 32".isdecimal())


#islower => returns true if all string characters are in lower case
print("hello".islower())
print("Hello".islower())


#isupper => returns true if all string characters are in upper case
print("hello".isupper())
print("Hello".isupper())
print("HELLO".isupper())

#isspace => returns true if all string characters are spaces
print("hello hii".isspace())
print("\t ".isspace())


#replace => relaplace phrases of string
print("hello there".replace("there","here"))

#lower => converts all string characters to lower case
print("Hello There".lower())

#upper => converts all string characters to upper case
print("Hello There".upper())

#lstrip => removes all leading white spaces ( front )
print("      Hello There      ".lstrip() + "hello")

#rstrip => removes all trailing  white spaces ( back )
print("      Hello There      ".rstrip() + "hello")

#strip => removes all  white spaces ( front and back )
print("      Hello There      ".strip() + "hello")\

#max => returns highest alphabetical char
print(max("hellothere"))

#min => returns lowest alphabetical char
print(min("hellothere"))

#title => returns first letter of string to upper case
print(str_country.title())

#split => split words into list elements using specified sepretaor and returns list
print(str_country.split())
print(str_country.replace(" ","#"))
print(str_country.split("#"))

#zfill => add 0's at the beggining of the string untill the str+ no of zeros != specified lentgh
print("hello".zfill(10))


#WAP to take inoput of list of name and find the longest one and smallest 
def getLongest():
    n = int(input("Enter the number of countries: "))
    country_list = []
    for i in range(0,n):
        country_list.append(input("Enter %d country name: "%(i+1)))
    longest_word = country_list[0]
    smallest_word = country_list[0]
    for l in country_list:
        if len(l) > len(longest_word):
            longest_word = l  
        if len(l) < len(smallest_word):
            smallest_word = l    
    return longest_word , smallest_word

long , small =  getLongest()
print("The longest Country name is : ",long)
print("The smallest Country name is : ",small)

#traverse each letter of string usingh while loop
msg = "goodmorning"
index = 0
while index < len(msg):
    letter = msg[index]
    print(letter)
    index+= 1


#traverse each letter of string usingh for loop
msg = "goodnight"
index = 0
for index in range(0,len(msg)):
    letter = msg[index]
    print(letter)

#WAP to check number of times a letter repeates in word
str = "hellooooooo"
count = 0
for i in str:
    if i == 'o':
        count += 1
print(count)


#WAP to check number of times a word repeates in sentence
str = "hellooooooo there , whats there "
str = str.lower()
strarr = list(str.split())
count = 0
for i in strarr:
    if i == 'there':
        count += 1
print(count)

"""