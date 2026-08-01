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

def solve(n: int, s: str):
    count = 0 
    chair_chunks = [s[i:i+3] for i in range(0, n, 3)]
    for i in chair_chunks:
        if i == 'xxx' or i == 'xx':
            count += 1 
    return count 

def main():
    try:
        t = 1
        for tc in range(1, t+1):
            n = inp()
            s = insr()
            print(solve(n, s))
    except (ValueError, IndexError):
        pass 

if __name__ == '__main__':
    main()



