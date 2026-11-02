import collections 
import heapq 
import itertools 
import math 
import os 
import sys 

# setting recursive limits 
sys.setrecursionlimit(2000000)

input = sys.stdin.readline 
def print(*args, sep=" ", end="\n"):
    sys.stdout.write(sep.join(map(str, args)) + end)

def inp():      return int(input())
def init():     return list(map(int, input().split()))
def insr():     return input().strip()
def invr():     return map(int, input().split())

def solve(tc: int):
    s = []
    for i in range(5):
        sn = input()
        s.append(sn)

    # first of all horizontal cas else:
        
    steps = []
    cnt1 = 0
    cnt2 = 0
    for i in range(5):
        if s[i].count('.') == 0: 
            return 0 

    
    if all(s[i][i] == 'o' for i in range(5)) or all(s[i][4-i] == 'o' for i in range(5)): 
        return 0 

    vals = []
    for i in range(5):
        cnt2 = 0
        for j in range(5): 
            if s[j][i] == 'o':
                cnt2+=1 
        vals.append(cnt2)

    if max(vals) == 5: 
        return 0
    


    # for horizonal 
    h = []
    for i in range(5): 
        num = list(s[i]).count('.')
        h.append(num)

    steps.append(min(h))

    #for vertical 
    v = []
    for i in range(5): 
        cnt = 0
        for j in range(5): 
            if s[j][i] == '.': 
                cnt+=1 
        v.append(cnt)

    steps.append(min(v))

    # for diagonal 

    d1 = sum(s[i][i] == '.' for i in range(5))
    d2 = sum(s[i][i] == '.' for i in range(5))
    steps.append(min(d1, d2))

    return min(steps)

   
    


def main():
    t = 1
    for tc in range(1, t+1):
        print(solve(tc))

if __name__ == '__main__':
    main()



