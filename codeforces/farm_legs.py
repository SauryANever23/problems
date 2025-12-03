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
    legs = int(input())
    if legs % 2 == 0:
        chicks = legs/2 
        cows = legs/4 
        config = min(chicks, cows)+1
    else:
        config = 0
    num.append(int(config))
        
for j in num:
    print(j)
