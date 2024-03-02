#operators in python
# Arithmatic    +  -  *  /  %   **exponent  //floor division
# Relational    >  >=  <=   ==   != or <>not equalto 
# Assignment    =  +=  -=  *=  /=  %= 
# Logical       and or not
# Identity      is   is not 
# Membership    in   not in
# Bitwise       &   |   ^   ~   <<   >>
a = 2
b = 4

print( a ," ", b)

print("\nArithmatic")
print("+ :", a + b)
print("- :", a - b)
print("* :", a * b)
print("/ :", a / b)
print("% :", a % b)
print("** :", a ** b)
print("// :", a // b)

print("\nRelational")
if a > b :
    print("a is greater")
if a >= b :
    print("a is greater then = b")
if a < b :
    print("a is smaller")
if a <= b :
    print("a is smaller then = b")
if a == b :
    print("a == b")
if a != b :
    print("a != b");
# if a <> b :
#     print("a <>");

print("\nAssignment")
a = b
print("a = b :", a )
a += b
print("a += b :", a )
a -= b
print("a -= b :", a )
a *= b
print("a *= b :", a )
a /= b
print("a /= b :", a )
a %= b
print("a %= b :", a)    

print("\nLogical")
a = 2
b= 4
if( a > b and a!= b):
    print("a > b and a!= b : true")
else : 
    print("a > b and a!= b : false")

if( a > b or a!= b):
    print("a > b or a!= b : true")
else : 
    print("a > b or a!= b : false")

if( not(a > b and a!= b)):
    print("not(a > b and a!= b): true")
else : 
    print("not(a > b and a!= b) : false")

