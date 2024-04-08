def test_prime(num):
    if(num==1):
        return True
    else:
        for x in range(2,num):
            if(num%x==0):
                return False
            return True
print(test_prime(167))        
        
    
