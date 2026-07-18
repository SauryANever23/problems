n = int(input())

total = 10000
last = 10000
for i in range(n):
    a, b, s = input().split()
    A, B = int(a), int(b)
    if s == 'take':
        total -= A
    else:
        total -= B

    last -= A

print(last - total)




