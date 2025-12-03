#  

t = int(input())

for i in range(t):
    n=int(input())
    a = list(map(int, input().split()))
    b = []
    for i in range(n-1):
        obj = a[i+1]-a[i]
        b.append(obj)
    print(a, "\n", b)
