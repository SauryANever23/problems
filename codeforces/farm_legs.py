# counts n legs 
# chicken: legs 2, cows: legs: 4 
# find number of configuations 
# for every p cows, there are 2p chickens

t = int(input())

def fact(n):
    fac=1
    while n>=1:
        fac = fac*n 
        n-=1 
    return fac

# combinatinos 
num = []
for i in range(t):
    n = int(input())
    if n % 2 == 0:
        config = (fact(n))/((fact(2))*fact(3))
    else:
        config = 0
    num.append(config)
        
for j in num:
    print(j)
