# next round 

n, k = map(int, input().split())
scores = list(map(int, input().split()))

k_pos = scores[k]

count = 0
for i in scores:
    if i >= k_pos:
        count+=1 

print(count)
