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

def solve(s: str):
    s_l = list(map(int, s.split()))
    for i in range(len(s)):
        for j in range(i):
            if int(s[i:j]) % 4 == 0: 
                s_l.pop(j)
    return len(s) - len(s_l)

def main():
    try:
        t = inp()
        for tc in range(1, t+1):
            solve(input().strip())
    except (ValueError, IndexError):
        pass 

if __name__ == '__main__':
    main()



