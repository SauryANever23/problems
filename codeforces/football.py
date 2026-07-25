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
    if '0'*7 in tc or '1'*7 in tc: 
        print("YES")
    else:
        print("NO")

def main():
    try:
        tc = input()
        solve(tc)
    except (ValueError, IndexError):
        pass 

if __name__ == '__main__':
    main()



