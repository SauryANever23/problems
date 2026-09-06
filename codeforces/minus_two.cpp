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
    
    if len(set(a)) == 1: 
        print(n)
        return 

    ao = [i for i in a if i %2 != 0]
    ae = [i for i in a if i %2 == 0]
    ae1 = [i for i in ae if i % 4 == 0]   
    ae2 = [i for i in ae if i % 4 != 0]
    # how do i figure out if thiery on the same state?? 
    print(max(len(ao), len(ae1), len(ae2)))
    # count = Counter(a)
    # print(count.most_common(1)[0][1])

def main():
    try:
        t = inp()
        for tc in range(1, t+1):
            solve()
   
    finally: 
        pass
if __name__ == '__main__':
    main()



