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

def solve(tc: str, b:str):
    ltc = list(tc)
    new = ''.join(ltc[::-1])
    if new == b: 
        print("YES")
    else:
        print("NO")

def main():
    try:
        tc = input().strip()
        b = input().strip()
        solve(tc,b)
    except (ValueError, IndexError):
        pass 

if __name__ == '__main__':
    main()



