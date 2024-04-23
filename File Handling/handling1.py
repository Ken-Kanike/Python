#open syntax
# filePointer = open('filename.type','mode','buffering','encoding' default- None,'errors'default- None,'newline'default- None,'closefd'default- True)

# file modes 
# r = read -- by default
# w = write ( if file exists , deletes all data  + overrites ) ( create if not exist )
# a = appends code if file exists 
# x = exclusive  ( operation fails if a file exists )
# b = binary mode
# rb = read binary
# rw = write binary
# r+ = read + write
# w+ = write + read
# a+ = appending + write



#open and close a file
#normal
try:
    f = open("File Handling/demo1.txt")
    print("File Successfully Opened")
    f.close()
except FileNotFoundError:
     print("File Not Found")

# try - finally 

try:
    f = open("File Handling/demo1.txt")
    print("File Successfully Opened")
    f.close()
except FileNotFoundError:
     print("File Not Found")
finally:
     f.close()


# using with  ( auto close )
with open("File Handling/demo1.txt") as f:
     print("File Successfully Opened")




#read binary  ( no encoding )
f = open("File Handling/demo1.txt" ,'rb')
data = f.read()
print(data)
f.close()

#read str
f = open("File Handling/demo1.txt")
data = f.read()
print(data)
f.close()





#buffering
f = open("File Handling/demo1.txt",mode='r' ,buffering=10,encoding='utf-8')
print(f)
f.close()
f = open("File Handling/demo1.txt",mode='w+' ,buffering=10)
print(f)
f.close()



#accessing file data ( file object variables )
f = open("File Handling/demo1.txt",'r')
print("File Name : ",f.name)
print("File Mode : ",f.mode)
print("File Closed : ",f.closed)
print("File Encoding : ",f.encoding)
f.close()
print("File Closed : ",f.closed)

#file object methods
f = open("File Handling/demo1.txt")
print("File Readable?: ",f.readable())
print("File Writeable?: ",f.writable())
f.close()
f = open("File Handling/demo1.txt",'w')
print("File Readable?: ",f.readable())
print("File Writeable?: ",f.writable())
f.close()
f = open("File Handling/demo1.txt",'w+')
print("File Readable?: ",f.readable())
print("File Writeable?: ",f.writable())
f.close()
f = open("File Handling/demo1.txt",'r+')
print("File Readable?: ",f.readable())
print("File Writeable?: ",f.writable())
f.close()



#check if file exist or not using os module
import os
fname = input("Enter a file name : ")
if os.path.isfile(fname):
     print("File exists")
else:
     print("File not found")

# f = open("File Handling/demo1.txt","w+")
# f.write("Hello World")
# data = f.read()
# print(data)
# f.close()
