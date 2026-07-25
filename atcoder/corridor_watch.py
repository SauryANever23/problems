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

def solve(m: int, d: int, s: str):
    cells = list(s)
    count = 0
    for i in range(len(cells)):
        if cells[i] != 'G':
            for j in range(len(cells)):
                if cells[j] == 'G':
                    if abs(i-j) <= d:
                        count += 1
    return count 

def main():
    try:
        m, d = invr() 
        s = input() 
        print(solve(m,d,s))
    except (ValueError, IndexError):
        pass 

if __name__ == '__main__':
    main()



