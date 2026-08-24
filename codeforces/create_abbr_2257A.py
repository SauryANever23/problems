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

def solve():

    n,m = invr()
    w = []
    for i in range(n):
        s = input().strip()
        w.append(s)
    a = []
    for i in range(m):
        s = input().strip()
        a.append(s)
    
    fl = [i[0].upper() for i in w]
    abv = []
    
    remaining = a[:]

    while remaining:
    changed = False

    for x in remaining[:]:
    if set(x).issubset(set(fl + abv)):
        abv.append(x[0])
        remaining.remove(x)
        changed = True

    if not changed:
    break

print("YES" if not remaining else "NO")

def main():
    try:
        t = inp()
        for tc in range(1, t+1):
            solve()
    except (ValueError, IndexError):
        pass 

if __name__ == '__main__':
    main()



