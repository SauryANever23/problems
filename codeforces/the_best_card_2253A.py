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



def solve(n: int):
    """
    n = 2, 3, 4 .. n+1 
    for any x and y cards 
    if the numbers are divisible by the other, the smaller card wins, 
    if not the larger cards win 
    
    for one card to win against every othe card 
    the number of cards must be prime. 
    
    """
    

def main():
    try:
        t = inp()
        for tc in range(1, t+1):
            n = inp()
            print(solve(n))
    except (ValueError, IndexError):
        pass 

if __name__ == '__main__':
    main()



