# next round 

n, k = map(int, input().split())
print(n, k)
scores = list(map(int, input().split()))

count = 0
for i in scores:
    if i > k:
        print(i,k,i>=k)
        count+=1 

print(count)
