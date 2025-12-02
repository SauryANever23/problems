# suspension greedy 

t = int(input())

suspension=[]
for _ in range(t):
    n = int(input())
    cards = list(map(int, input().split()))
    num = 0 
    num = cards[1] + (cards[0]//2)
    
    suspension.append(min(num, n))

for i in suspension:
    print(int(i))

"""
alternative method:

y, r = map(int, input().split())

elms_by_r = r 
elems_by_y = y//2 

total_elms = r + y//2 

suspension.append(min(total_elims, n))
"""

