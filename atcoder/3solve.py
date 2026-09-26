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
    q = inp()
    s = insr()
    t = insr()
    qs = []
    for i in range(q):
        l, r = invr()
        qs.append((l, r))
    
    for i in range(q):
        l, r = qs[i]
        if t in s[l-1:r]:
            print('YES')
        else:
            print('NO')

def main():
    t = 1
    for tc in range(1, t+1):
        solve(tc)
        

if __name__ == '__main__':
    main()



