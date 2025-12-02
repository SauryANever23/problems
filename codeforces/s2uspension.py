# suspension greedy 

t = int(input())

suspension=[]
for _ in range(t):
    n = int(input())
    cards = list(map(int, input().split()))
    num = 0 
    num += cards[1]
    if num < n:
        if (cards[0] % 2) == 0:
            num += cards[0]/2
        else:
            num += (cards[0]-1)/2
    suspension.append(num)

for i in suspension:
    print(int(i))

