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
    

def main():
    try:
        n = inp()
        s = input().strip()
        t = n
        for tc in range(1, t+1):
            print(solve(n,s))
    except (ValueError, IndexError):
        pass 

if __name__ == '__main__':
    main()



