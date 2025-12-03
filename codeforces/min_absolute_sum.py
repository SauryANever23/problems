#  

t = int(input())

for i in range(t):
    n=int(input())
    a = list(map(int, input().split()))
    b = []
    min=0
    for i in range(n-1):
        obj = a[i+1]-a[i]
        b.append(obj)
    for i in b:
        min += i
    min = abs(min)


