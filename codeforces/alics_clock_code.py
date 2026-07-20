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
    if int(s[0]) + int(s[2]) == int(s[1]) or int(s[1]) == int(s[2]):
        result = "YES"
    else:
        result = "NO"
    return result 

def main():
    try:
        t = 1
        for _ in range(1, t+1):
            tc = input()
            print(solve(tc))
    except (ValueError, IndexError):
        pass 

if __name__ == '__main__':
    main()



