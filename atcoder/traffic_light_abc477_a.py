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

def solve():
    a = ['B', 'Y', 'R']
    s = insr()
    i = a.index(s)
    if (s=='R'):
        print('B')
        return
    print(a[(i%3)+1])

def main():
    t = 1
    for tc in range(1, t+1):
        solve()

if __name__ == '__main__':
    main()



