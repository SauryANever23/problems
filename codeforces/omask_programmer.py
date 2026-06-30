
t = int(input())

def find_min_moves(a, b, x):
    steps = 0
    while (a != b): 
        if x > a and x > b: 
            return 0 
        elif (a - b) > x:

                
soln = []
for i in range(t):
    a, b, x = map(int, input().split())
    soln.append(find_min_moves(a,b,x))

for i in soln:
    print(i)

