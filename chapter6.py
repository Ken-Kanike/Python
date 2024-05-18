#reading input from keyboard
#WAP for gross salary and net salray where,
# HRA is 10% of basic salary
# TA is 5% of basic salary
# employee pay tax = 2% of total salary

basic = float(input("Enter the basic salary: "))
HRA =(basic*10)/100
TA =(basic*5)/100
gross_sal = basic + HRA + TA
print("Gross salary: ",gross_sal)
Ptax = (gross_sal*2)/100
net_sal = gross_sal - Ptax
print("Net salary = ",net_sal)

# e = mc^2
m = float(input("Enter mass of object in (Kg):"))
c = float(input("Enter velocity of object in (m/s):"))
e = m*(c**2)
print("Monmentum/Energy = ",e)

#binary to decimal
binary = list(input("Enter a binary number:"))
deci_val = 0
for i in range(len(binary)):
    digit = binary.pop()  # reading each digit from LSB
    if digit == '1':  # if 1
        deci_val = deci_val + pow(2,i)  # get 2^i and it to deci_val
print("The decimal value  is ",deci_val)

#decimal => binary ?




#printing value on screen
print("Good Morning")
print("Good Morning\nHave a nice day!")
print("Good Morning\tHave a nice day!")
x = 10
print("x =", x)
a = 100
b = 200
print("Before swap \na = %d \nb = %d"%(a,b))
a ,b = b,a
print("After swap \na = {} \nb = {}".format(a,b))
print(f'The value of a is {a}')
print(f'The value of b is {b}')



# file handling  

#opening a file
# file_obj = open("Filename/path",mode)
f =  open("DemoFile.txt",'w')
#closing a file
f.close()

#opening file using with
with open("DemoFile.txt",'rt') as f:
    print(f.read())
f.close()

#reading from file
#read()
#readline()
#readlines()
#list()
#for loop

#uing read()
f = open("DemoFile.txt",'rt')
print(f.read())   # reads everything in file
f.close()

#uing readline()
f = open("DemoFile.txt",'rt')
print(f.readline())  # reads only one line at a time
print(f.readline())  # print 2nd line
 # so on ....
f.close()

#uing readlines()
f = open("DemoFile.txt",'rt')
print(f.readlines()) # reads all line of files and returns each line as list element
f.close()

#uing list()
f = open("DemoFile.txt",'rt')
print(list(f)) # reads all line of files and returns each line as list element
f.close()

#uing for loop
f = open("DemoFile.txt",'rt')
for line in f:
    print(line)  
f.close()



#Wap to find and print lines in DemoFile.txt starting with 'Welcome' word
f = open("DemoFile.txt",'rt')
for line in f:
    line = line.strip().lower()
    if line.find("welcome") == -1:
        continue
    print(line)
f.close()

#WAP to split the lines of file into words
with open("DemoFile.txt",'rt') as f:
    for line in f:
        word_list = line.split()
        print(word_list)
f.close()


#writing into files
#write()
#writelines()
#write() in 'a' mode
#using write()
f =  open("DemoFile.txt",'wt')
f.write("This is a new written line") # writes simpe line/lines using \n
f.close()

#using writelines()
f =  open("DemoFile.txt",'wt')
lines = ["This is a new written line\n","This is written in Python\n","Welcoome to Python"]
f.writelines(lines) # writes multiple lines using list of lines
f.close()


#appending data into files
f =  open("DemoFile.txt",'a')
f.write("\nThis is another new written line") # writes simpe line/lines using \n
f.close()


#Wap tp write n numbers of lines in a file and then read it
#write
n = int(input("Enter number of lines you want to enter: "))
fwrite = open("DemoFile.txt",'wt')
for i in range(1,n+1):
    line = input("Enter %d line : "%i)
    fwrite.write(line+"\n")
fwrite.close()
#read
fread = open("DemoFile.txt",'rt')
print("The content of file :\n")
print(fread.read())
fread.close()

#wap to read from one file and write into another file and diplay copied data
#copy data
file1 = open("DemoFile.txt",'rt')
file2 = open("DemoFile2.txt",'wt')
for line in file1:
    file2.write(line +"\n")
file1.close()
file2.close()
#diplay copied data
file2 = open("DemoFile2.txt",'rt')
print(file2.read())
file2.close()


#renaming a file
import os
os.rename("DemoFile.txt","DemoFile1.txt")
print("File is renamed!")


# deleting  a file
import os
os.remove("DemoFile1.txt")
print("File is removed!")

#seek() and tell()
file2 = open("DemoFile2.txt",'rt')
print("The content of file :")
print(file2.read())
print("The current position of cursor:")
print(file2.tell()) #prints the current position of cursor
file2.seek(0) #moves cursor to initial position
print("The current position of cursor:")
print(file2.tell())
file2.seek(10) #moves cursor to 10 bytes ahead in file
print(file2.read())
file2.close()



#dirctory methods
#getcwd() => get current working directory
import os
print(os.getcwd())

#listdir() => display all files and sub-directory inside directory
import os
print(os.listdir())

#mkdir() => create a new  directory
import os
os.mkdir("DemoPyDirectory")
print(os.listdir())

#rmdir() => remove file or  directory
import os
os.rmdir("DemoPyDirectory")
print(os.listdir())

#file handling programs
#WAP to count vowels and consonenet in a file
f = open("DemoFile2.txt",'r')
v = set("aeiou")
c = set("bcdfghjklmnpqrstvwxyz")
v_count = 0
c_count = 0
for letter in f.read():
    if letter.lower() in v:
        v_count+=1
    elif letter.lower() in c:
        c_count+=1
f.close()
print("Nuumber of vowels =",v_count)
print("Nuumber of consonents =",c_count)


#WAP to count total number of lines in a file
f = open("DemoFile2.txt",'r')
line_count = 0
for line in f:
    line_count +=1
f.close()
print("Number of lines =",line_count)


#WAP to count total number of words in a file
f = open("DemoFile2.txt",'r')
w_count = 0
for line in f:
    word = line.split()
    w_count +=len(word)
f.close()
print("Number of words =",w_count )


#WAP to count total number of chars in a file
#same code as for words


#WAP to count blank spaces in a file
f = open("DemoFile2.txt",'r')
s_count = 0
for line in f:
    word = line.split()
    for letter in word:
        if(letter.isspace):
            s_count+=1
f.close()
print("Number of spaces =",s_count )


#WAP to copy data from one file into another
lines = []
with open("DemoFile2.txt",'r') as f2:
    lines = f2.readlines()
f2.close()
with open("DemoFile.txt",'w') as f1:
    for line in lines:
        f1.write(line)
f2.close()


#exception handling
#Eg using division of two numbers
try:
    a = int(input("Enter value of a: "))
    b = int(input("Enter value of b: "))
    c = float(a/b)
except ValueError:
    print("You have entered wrong data")
except ZeroDivisionError:
    print("Divide by zero error")
else:
    print("The result is: ",c)     

#raise
# syntax raise[Exception[,args[,traceback]]]
def NegativeNum(num):
    if num <0:
        raise "Number is Negative"
    
#user defined exception
#WAP user defined exception to get only positive number
class Error(Exception):
    #Base class for other exception
    pass

class NegavtiveValue(Error):
    pass

class ZeroValue(Error):
    pass

while True:
    try:
        i_num = int(input("Enter a number:"))
        if i_num < 0:
            raise NegavtiveValue
        elif i_num == 0:
            raise ZeroValue
        break
    except NegavtiveValue:
        print("Negative number try again!")
        print()
    except ZeroValue:
        print("Zero number try again.")
        print()
print("The Number is Positive")

#WAP to raise divid eby zero error using user def error
class DivideByZero(Exception):
    pass

try:
    a = int(input("Enter value of a: "))
    b = int(input("Enter value of b: "))
    if b == 0:
        raise DivideByZero
    c = float(a/b)
except DivideByZero:
    print("Divide by zero error")
else:
    print("The result is: ",c)   