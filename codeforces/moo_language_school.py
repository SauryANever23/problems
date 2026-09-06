import collections 
import heapq 
from itertools import batched
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
    n, k = invr()
    s = insr()
    sl = list(s)
    feilds = [list(fild) for fild in batched(sl, k)]
    count =0 
    for i in feilds: 
        if '0' not in ''.join(i): 
            count +=1 
    print(count)

def main():
    try:
        t = inp()
        for tc in range(1, t+1):
            solve(tc)
    except (ValueError, IndexError):
        pass 

if __name__ == '__main__':
    main()



