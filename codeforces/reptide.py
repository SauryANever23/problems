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

def solve(a,b,c):

    mx = max(a,b,c)
    mn = min(a,b,c)
    vals = [a,b,c]
    vals.remove(mx)
    vals.remove(mn)
    md = vals[0]
    if len(set([a,b,c])) <= 2: 
        return 0
        
    return min(mx-md, md-mn)

def main():
    t = inp()
    for tc in range(1, t+1):
        a,b,c = invr()
        print(solve(a,b,c))

if __name__ == '__main__':
    main()



