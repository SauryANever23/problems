#  

t = int(input())

for i in range(t):
    n=int(input())
    a = list(map(int, input().split()))
    b = []
    for elem, i in enumerate(a):
        obj = a[i+1]-a[i]
        b.append(obj)
    print(a, "\n", b)
