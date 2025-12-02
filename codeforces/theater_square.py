# area of square = m x n
# area of flagstone = a x a 
# no cutting stones, 
# how many flagstones required to fill the square? 

n, m, a = map(int, input().split())

def small(a, b):
    if a > b:
        return b 
    else:
        return a 
def big(a, b):
    if a > b:
        return a 
    else:
        return b

width = small(m, n)

lenght = big(m, n)

if (a >= width):
    p = lenght // a 
print(p)



