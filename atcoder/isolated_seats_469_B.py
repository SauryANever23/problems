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

def solve_failed(n: int, s: str):
    count = 0 
    chair_chunks = [s[i:i+3] for i in range(0, n, 3)]
    for i in chair_chunks:
        # check left 
        if set(list(i)) == {'x'}:
            count += 1 
        else: 
            if i == 'xxo' or i == 'oxx':
                count +=1 
    return count 

def solve(n: int, s: str):
    count = 0 
    # for the middle elements
    if n != 1:
        for i in range(1, n-1):
            if s[i] == 'x' and s[i+1] == 'x' and s[i-1] == 'x':
                count += 1 

        # for the border elemnt
        if s[0] == 'x' and s[1] == 'x':
            count += 1 

        # for right element
        if s[n-1] == 'x' and s[n-2] == 'x':
            count += 1
    else:
        if s == 'x':
            count += 1

    return count
def main():
    try:
        t = 1
        for tc in range(1, t+1):
            n = inp()
            s = insr()
            print(solve(n, s))
    except (ValueError, IndexError):
        pass 

if __name__ == '__main__':
    main()



