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

def solve(tc: int):
    n, d = invr()
    x = init()

    k = []
    cnt = []
    for i in range(0, n): 
        count = 0
        for j in range(n):
            if (j != i):
                if (abs(x[i] - x[j]) >= d): 
                    count+=1
        cnt.append(count)

    for i in range(n): 
        if cnt[i] == (n-1): 
            k.append(i+1)

    if (len(k) == 0):
        print(0)
        print(" ")
        return 
    else: 
        print(len(k))
        for i in range(len(k)):
            print(k[i], end=" ")

def main():
    t = 1
    for tc in range(1, t+1):
        solve(tc)

if __name__ == '__main__':
    main()



