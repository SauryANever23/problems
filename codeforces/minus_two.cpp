from collections import Counter
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

def solve():
    n = inp()
    a = init()
    """
    // we can reduce as may times as we like by 2, 
    // abs 

    // all odd numbers amount to 1 in the end 
    // all even numebr either 0 or 2, if the number are divisilbe by 4, they both are in the same sta     te, if they are not divisible for 4, they are in differtm state 
    """ 
    o = [i for i in a if i % 2 !=0]
    e1 = [i for i in a if i%4==0]
    e2 = [i for i in a if (i%4!=0 and i%2==0)]

    print(max(len(o), len(e1), len(e2)))
  
def main():
    try:
        t = inp()
        for tc in range(1, t+1):
            solve()
   
    finally: 
        pass
if __name__ == '__main__':
    main()



