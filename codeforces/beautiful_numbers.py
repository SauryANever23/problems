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
    
    # using the greedy approach 
    # checking how much a number is reducable 
    
    reduce = []

    nums = list(map(int, list(n)))
    
    current_sum = sum(nums)

    if current_sum <= 9: 
        return 0 

    reduce.append(nums[0]-1)
    
    for d in nums[1:]:
        recude.append(d)

    for re in reduce: 
        current_sum -= re 
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

