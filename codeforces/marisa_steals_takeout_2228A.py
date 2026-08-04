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

def solve(n: int, w: list):
    count = 0 
    count += w.count(0)
    n1 = w.count(2)
    n2 = w.count(1)
    count += min(n1, n2)
    count += (max(n1, n2)-min(n1,n2))//3 if (max(n1,n2)-min(n1,n2)%2==0) else 0
    return count 

def main():
    try:
        t = inp()
        for tc in range(1, t+1):
            n = inp()
            w = init()
            print(solve(n, w))
    except (ValueError, IndexError):
        pass 

if __name__ == '__main__':
    main()



