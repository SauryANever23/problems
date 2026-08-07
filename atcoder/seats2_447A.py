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

def solve(n, m):
    empty_seats = n-m
    if empty_seats >= m or abs(m-empty_seats) == 1:
        return "Yes"
    else: 
        return "No"

def main():
    try:
        t = 1
        for tc in range(1, t+1):
            n, m = map(int, input().split())
            print(solve(n,m))
    except (ValueError, IndexError):
        pass 

if __name__ == '__main__':
    main()



