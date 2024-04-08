s1=input("Enter Name")
print(s1)
countu=0
countl=0
for ch in s1:
    if ch.isupper():
        countu+=1
    if ch.islower():
        countl+=1
print("Total lower char :",countl)
print("Total upper char :",countu)
