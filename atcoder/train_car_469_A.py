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

def solve(n: int, k: int):
    train = [0 for i in range(n)]
    x = 0 
    for i in range(n, k, -1):
        x += 1 
    return x
        

def main():
    try:
        t = 1
        for tc in range(1, t+1):
            n, k = invr()
            print(solve(n, k))
    except (ValueError, IndexError):
        pass 

if __name__ == '__main__':
    main()



