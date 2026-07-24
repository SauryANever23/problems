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

def solve(tc: str):
    digits = set(list(tc))
    if len(digits) == 2 and '4' in digits and '7' in digits:
        print("YES")
    else:
        print("NO")

def main():
    try:
        t = 1
        for tc in range(1, t+1):
            solve(insr())
    except (ValueError, IndexError):
        pass 

if __name__ == '__main__':
    main()



