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

def solve(k,x):
    """
    3n+1 problem 
    
    for k is the numebr of steps and x is what you get, then find the iniital value
    """
    if k > 1: 
        return x*(int(math.pow(2,k)))
    else: 
        return 2*x

def main():
    try:
        t = inp()
        for tc in range(1, t+1):
            i, j = invr()
            print(solve(i,j))
    except (ValueError, IndexError):
        pass 

if __name__ == '__main__':
    main()



