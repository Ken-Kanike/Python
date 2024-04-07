#simple fucntion    def = definition
def simple_functions():
    print("Hello World!\n")

simple_functions() #function call


#retrun
def add():
    a = int(input("Enter num 1 : "))
    b = int(input("Enter num 2 : "))
    return a+b

print ("Sum of two nums = ", add())


#fucntion arguments
def add(a,b): 
    print("\na = ",a)
    print("b = ",b)
    print ("Sum of two nums = ", a+b)

add(10,20)
add(b=10,a=20)
add( int(input("Enter num1:")) , int(input("Enter num2:")) ) 


#types
# 1) No Arg No Return
# 2) With Arg No Return
# 3) No Arg Wirh Return
# 4) With Arg With Return


#default arguments
#  rule    function( noDefaultArg , noDefaultArg , DefaultArg  ,,.... necessary now till the end , noDefaultArg)
def sum3(a, b = 5 , c = 5):
    print(a+b+c)

sum3(5)
sum3(5,10)
sum3(2,2,2)


#Break & Continue
print("\nBreak Example : print 1-5")
i = 1
while(i <= 5):
    if i < 4:
        print(i)
        i += 1
    else:
        print("Break at " , i)
        i += 1
        break
    
print("\nContinue Example : print 1-5")
i = 1
while(i <= 5):
    if i == 4:
        print(i)
        i += 1
    else:
        print("Continue at ", i)
        i += 1
        continue