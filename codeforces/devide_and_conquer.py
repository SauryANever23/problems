t = int(input())

vals = []
for i in range(t):
    v = tuple(map(int, input().split()))

    vals.append(v)

for val in vals:
    x, y = val 
    if x % y == 0: 
        print("YES")
    else:
        print("NO")
