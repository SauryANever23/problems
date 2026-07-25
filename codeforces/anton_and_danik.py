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

def solve(n, s):
    a = s.count('A')
    d = s.count('D')
    if a > d: 
        print("Anton")
    elif d > a:
        print("Danik")
    else: 
        print("Friendship")

def main():
    try:
        n = inp()
        s = input()
        solve(n,s)
    except (ValueError, IndexError):
        pass 

if __name__ == '__main__':
    main()



