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
    """
    an array = [0 0 0 0 ]
    take a subsqeunce, 
    any set of numebr whose sum is divisble by 3 
    then remove one sequence from thenumbers 
    and repeat, 
    """ 
    count = 0 
    count += w.count(0)
    w = [i for i in w if i != 0]
    n1 = w.count(2)
    n2 = w.count(1)
    if n1 == n2: 
        count += n1
    else: 
        count += min(n1, n2)
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



