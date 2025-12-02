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
    num += cards[1]
    if cards[0] % 2 == 0:
        num += cards[0]/2 
    else:
        cards[0] -= 1 
        num += cards[0]/2
    suspensions.append(num)

for suspension in suspensions:
    print(suspension)


