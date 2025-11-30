# team problem
# to give solutions implemented
# solutions implement iff atleast two of the know the solution 

n = int(input())

final_cnt = 0;
for _ in range(n):
    arr = list(map(int, input()))
    count = 0
    for i in range(3):
        if arr[i] == 1:
            count += 1
    if count >= 2:
        final_cnt += 1
print(final_cnt)





