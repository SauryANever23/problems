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

def solve(n,a,b):
    if b <= a: 
        cost = (n // 3)*b 
        n = n % 3 
        if n % 2 == 0:
            cost += (n // 2)* b 
            n = n %2  
        else: 
            cost += b 
            n -= 1
            cost += (n//2)*b
        return cost 
    else: 
        if 3*a >= b: 
            cost = (n//3)*b 
            n = n % 3 
            if n % 2 == 0: 
                if 2*a >= b: 
                    cost += (n//2)*b 
                    n = n%2 
                else: 
                    cost += (n//2)*a 
                    n = n%2 
            else: 
                cost += a 
                n -= 1 
                cost += (n//2)*min(a, b) 
            return cost
        else: 
            cost = (n)*a 
            return cost 
        
        


def main():
    try:
        t = inp()
        for tc in range(1, t+1):
            n, a, b = invr()
            print(solve(n,a,b))
    except (ValueError, IndexError):
        pass 

if __name__ == '__main__':
    main()



