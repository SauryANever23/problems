
n, m = map(int, input().split())

a = list(map(int, input().split()))

b = list(map(int, input().split()))

steps = 0 

for i in range(n-1):
    if b[i] == 0: 
        pass 
    elif b[i] == 1:
        steps += 3 - (a[i]+a[i+1])

print(steps)
