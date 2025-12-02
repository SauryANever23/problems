# area of square = m x n
# area of flagstone = a x a 
# no cutting stones, 
# how many flagstones required to fill the square? 

n, m, a = map(int, input().split())
p = 0 
def small(a, b):
    if a > b:
        return b
    elif a == b:
        return a
    else:
        return a 
def big(a, b):
    if a > b:
        return a 
    elif a ==b:
        return a
    else:
        return b

width = small(m, n)

lenght = big(m, n)

if (a >= width):
    if lenght % a == 0:
        p = lenght / a 
    else:
        p = (lenght // a) + 1
elif (a < width):
    pass
print(int(p))



