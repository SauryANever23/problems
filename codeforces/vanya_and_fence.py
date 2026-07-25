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

def solve(n: int, h: int, a: list):
    w_arr = []
    for i in a: 
        if i > h: 
            w_arr.append(2)
        else: 
            w_arr.append(1)
    return sum(w_arr)

def main():
    try:
        n, h = invr()
        a = init()
        print(solve(n,h, a))
    except (ValueError, IndexError):
        pass 

if __name__ == '__main__':
    main()



