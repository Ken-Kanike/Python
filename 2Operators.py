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
    print("a != b")

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
b = 4
if( a > b and a != b):
    print("a > b and a!= b : true")
else : 
    print("a > b and a!= b : false")

if( a > b or a != b):
    print("a > b or a!= b : true")
else : 
    print("a > b or a!= b : false")

if( not(a > b and a != b)):
    print("not(a > b and a!= b): true")
else : 
    print("not(a > b and a!= b) : false")

# --- Completed Sections Below ---

print("\n--- Identity Operators (is, is not) ---")
# 'is' checks memory identity (same object in RAM via id()), whereas '==' checks equality of values.
x = [1, 2, 3]
y = [1, 2, 3]
z = x

print(f"x == y (values equal): {x == y}")
print(f"x is y (same memory object): {x is y}")      # False: different list objects in memory
print(f"x is z (same reference): {x is z}")           # True: z references x
print(f"x is not y: {x is not y}")
print(f"id(x)={id(x)}, id(y)={id(y)}, id(z)={id(z)}")

print("\n--- Membership Operators (in, not in) ---")
# Checks whether a value is present in a sequence (string, list, tuple, set, dict)
fruits = ["apple", "banana", "cherry"]
print(f"'banana' in fruits: {'banana' in fruits}")
print(f"'orange' not in fruits: {'orange' not in fruits}")
text = "Master Python Programming"
print(f"'Python' in text: {'Python' in text}")
user_dict = {"name": "Alex", "role": "Developer"}
print(f"'role' in user_dict (checks keys): {'role' in user_dict}")

print("\n--- Bitwise Operators (&, |, ^, ~, <<, >>) ---")
# Operate directly on binary representations of integers
p = 5  # 0b0101
q = 3  # 0b0011
print(f"p = {p} ({bin(p)}), q = {q} ({bin(q)})")
print(f"Bitwise AND (p & q): {p & q} ({bin(p & q)})")       # 0b0001 = 1
print(f"Bitwise OR (p | q):  {p | q} ({bin(p | q)})")       # 0b0111 = 7
print(f"Bitwise XOR (p ^ q): {p ^ q} ({bin(p ^ q)})")       # 0b0110 = 6
print(f"Bitwise NOT (~p):    {~p} ({bin(~p)})")             # -(p+1) = -6
print(f"Left Shift (p << 1): {p << 1} ({bin(p << 1)})")     # 0b1010 = 10 (multiply by 2^1)
print(f"Right Shift (p >> 1):{p >> 1} ({bin(p >> 1)})")     # 0b0010 = 2  (floor divide by 2^1)

print("\n--- Walrus Operator := (Assignment Expression) ---")
# Added in Python 3.8: Assigns values to variables as part of an expression
# Useful in while loops, list comprehensions, and if checks
sample_data = "Hello, Pythonista"
if (n := len(sample_data)) > 10:
    print(f"String length is {n}, which is greater than 10!")

# Operator Precedence summary:
# 1. () Parentheses
# 2. ** Exponentiation
# 3. +x, -x, ~x Unary
# 4. *, /, //, % Multiplication, Division
# 5. +, - Addition, Subtraction
# 6. <<, >> Bitwise shifts
# 7. & Bitwise AND
# 8. ^ Bitwise XOR
# 9. | Bitwise OR
# 10. Comparisons (==, !=, <, <=, >, >=), Identity (is), Membership (in)
# 11. not, and, or Logical
