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
    """
    F(x) = sum of digits of the number x 
    x is beautiful if 

    F(F(x)) = F(x)

    which numebrs are beautiful? 
    -> single digit numbers 
    
    37 - not beautiful 
    replae 7 with 3 or 2 or 1 , we get a beautiful number, 

    basically change the digits such that thier sums are single digit 
    
    """ 
    steps = 0
    
    nums = list(map(int, list(n)))

    s_nums = sorted(nums)
    i = 0
    while True: 
        if sum(nums) == sum(list(map(int, list(''.join(s_nums))))):
            return steps 
        if i >= len(s_nums):
            return steps 
        if s_nums[i] != nums[0]:
            s_nums[i] = 0 
            steps += 1 
        i += 1 

    
def main():
    try:
        t = inp()
        soln = []
        for tc in range(1, t+1):
            soln.append(solve(input()))

        for s in soln: 
            print(s)
    except (ValueError, IndexError):
        pass 

if __name__ == '__main__':
    main()



