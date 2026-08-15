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

def solve(a,b):
    if (a+b == 9) or (a/b == 9.0) or (a*b==9) or (a-b==9):
        return "Nine"
    else:
        return "Nein"

def main():
    try:
        t = 1
        for tc in range(1, t+1):
            a, b = invr()
            print(solve(a,b))
    except (ValueError, IndexError):
        pass 

if __name__ == '__main__':
    main()



