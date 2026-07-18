n = int(input())

total = 10000
last = 10000
for i in range(n):
    a, b, s = input().split()
    A, B = int(a), int(b)
    if s == 'take':
        total -= (B-A)
    else:
        total -= B 

    last -= (B-A)

print(last - total)




