'''
#even odd

#greated among 3 -> Nested if e.g
a = 220
b = 220
c = 30 
if a == b and a > c and b > c :
    print(a," and ", b ," are equal and greater")
elif c == b and c > a and b > a :
    print(c," and ", b ," are equal and greater")
elif a ==  c and a > c and c > b :
    print(a," and ", c ," are equal and greater")
elif( a == b and b == c):
    print("all are equal")
else:
    if( a > b and a > c):
        print(a ,"  is greater number")
    elif( b > a and b > c):
        print(b ,"  is greater number")
    else:
        print(c ,"  is greater number")

#wap for grades

#sum and avg of n natural numbers
n = int ( input("Enter number"))
sum = 0
avg = 0.0
i = 1
while i<=n:
    sum += n
    i+=1
avg = sum/n
print("Sum of n  naturla numbers = ", sum)
print("Avg of n  naturla numbers = ", avg)

#wap to create a table of sqaure and exponential of n numbers
n = int(input("Enter number : "))
i = 1
print("Number | Sqauare  | Exponential")
while i <= n:
    print( i ,"   |   ",i*i,"   |   ",i**i)
    i+= 1

#WAP to print all even and odd numbers till n  and also count if even and odd
n = int(input("Enter number : "))
i = 1
even = []
odd = []
while i!=0 and i <= n :
    if(i%2 == 0):
        even.append(i)
    else:
        odd.append(i)
    i += 1
print("Even numbers between 0 to n = ",even)
print("No Even numbers between 0 to n = ",len(even))
print("Odd numbers between 0 to n = ",odd)
print("No Odd numbers between 0 to n = ",len(odd))

#wap fibbonacci i.e  = 0 1 1 2 3 5 ....
n = int( input("Enter n number of series :"))
a = 0
b = 1
i = 0
while( i<= n):
    print(a , end=" ")
    c = a + b
    a = b
    b = c
    i+=1

#arm srtong number i.e: 371 = 3**3+7**3+1**3
num = int(input("Enter number: "))
copy = num
sum = 0
while num > 0:
    digit = num % 10 # seperate numbers
    sum = sum + (digit**3) # make cube and sum seperated numbers
    num = num//10 # removed added number from the main number
if(copy == sum):
    print(copy , " is an Armstrong number")
else:
     print(copy , " is not an Armstrong number")


#sum of  n numbers using for loop
n = int(input("Enter number : "))
sum = 0 
for i in range(n+1):
    sum = sum+i;
print(sum)

#multiplication table using for loop
n = int(input("Enter number : "))
for i in range(1,11):
    print( n , " * " , i  ," = " , i*n)

#prime number  ,,,,,,,,,,,,,,,,,,not sure
num = int(input("Enter number : "))
if( num > 1):
    for i in range(2,num):
        if( num%i == 0):
            print(num , " is not a prime number")
        else:
            print(num , " is  a prime number")
else:
    print(num , " is not a prime number")


#GCD of 2 numbers

#patterns
'''