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

def solve(n: str):
    digits = list(map(int, n))

    current_sum = sum(digits)

    if current_sum <= 9:
        return 0

    reductions = []

    # Leading digit: d -> 1
    reductions.append(digits[0] - 1)

    # Other digits: d -> 0
    for d in digits[1:]:
        reductions.append(d)

    reductions.sort(reverse=True)

    steps = 0

    for reduction in reductions:
        current_sum -= reduction
        steps += 1

        if current_sum <= 9:
            return steps
    
def main():
    try:
        t = int(input())
        soln = []
        for tc in range(1, t+1):
            a = input().strip()
            soln.append(solve(a))

        for s in soln: 
            print(s)
    except (ValueError, IndexError):
        pass 

if __name__ == '__main__':
    main()

