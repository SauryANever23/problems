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

    n = int(input())
    a = init()
    
    coins = [0,0,0] 
    
    for i in a: 
        # the numer that we add must be postitive, so how do we do that? 
        amt = str(i)
        ret = 1000 - int(amt[-3:])
        r = str(ret) 
        if len(r) == 3:
            coins[0] += int(r[2])
            coins[1] += int(r[1])
            coins[2] += int(r[0])
        elif len(r) == 2: 
            coins[0] += int(r[1])
            coins[1] += int(r[0])
        elif len(r) == 1: 
            coins[0] += int(r[0])
    print(coins[0], coins[1], coins[2])



def main():
    t = 1
    for tc in range(1, t+1):
        solve(tc)

if __name__ == '__main__':
    main()



