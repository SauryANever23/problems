t = int(input())

nums = []

for i in range(t):
    (x, y) = tuple(map(int, input().split()))
    nums.append((x, y))

for num in nums:
    x, y = num
    if x % 2 == 0 or y % 2 == 0:
        print("YES")
    else:
        print("NO")
    
 
