def string_test(s1):
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
s1=input("Enter name : ")
string_test(s1)
