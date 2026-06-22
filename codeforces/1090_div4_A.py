a = int(input()) 

total = []
for _ in range(a):
    nums = list(map(int, input().split()))
    total.append(nums)

tot_sum = []

for num in total: 
    new = sorted(num)
    s = sum([-new[i] for i in range(len(new)-1)])+new[6]
    tot_sum.append(s)

for tot in tot_sum: 
    print(tot)


