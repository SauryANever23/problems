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
def invr():     return map(int, input().split()

def solve(n, s):
    if n == 0:
        return 0
    cnt = []
    or_s = dict.fromkeys(s)
    un_s = list(pr_s)
    for i in range(1, len(un_s)):
        cnt.append((un_s[i], un_s.count(un_s[i])))
    min_pair = min(un_s)
    val, count = min_pair 
    ls = list(s)
    if ls.index(val) != 1 or ls.index(val) != n: 
        ls.remove(val)
    else: 
        un_s.remove(min_pair)
        min_pair = min(un_s) 
        val, count = min_pair 
        ls.remove(val)
    # now for lenght of compressed string 
    s = ''.join(ls) 
    new = []
    for i in range(1, n): 
        for j in range(i):
            if len(set(s[i:j])) == 1: 
                new.append(s[i]) 

    return len(new)

        
def main():
    try:
        t = inp()
        for tc in range(1, t+1):
            n = int(input())
            s = insr()
            print(solve(n, s))
    except (ValueError, IndexError):
        pass 

if __name__ == '__main__':
    main()



