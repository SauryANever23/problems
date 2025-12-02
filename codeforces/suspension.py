# a game being played 
# initially n players 
# yellow cards: y, and red cards: r (for fouls)
# two ways pllayers can be suspended
# --> 2 y or 1 red 
# once suspended, out of game, n-- 
# determine the maximum number of people suspended from game 

# for y and r 
# 

t = int(input())
suspensions=[]
for _ in range(t):
    n = int(input())
    num = 0 
    cards = list(map(int, input().split()))
     
    if cards[0] % 2 ==0:
        if ((cards[0]/2)+cards[1]) < n:
            num = cards[1] + (cards[0]/2)
        elif cards[1] == n:
            num = cards[1]
        elif ((cards[0]/2)+cards[1]) >= n:
            num = cards[1]+(cards[0]/2)

    else:
        if ((cards[0]-1)/2) + cards[1] < n: 
            num = cards[1] + ((cards[0]-1)/2)
        elif ((cards[0]-1)/2) + cards[1] >= n:
            num = cards[1] + (cards[0]-1)/2
    
    suspensions.append(num)

for suspension in suspensions:
    print(int(suspension))


