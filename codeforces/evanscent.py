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

def solve_2(n, s):
    runs = 1
    for i in range(1, n):
        if s[i] != s[i - 1]:
            runs += 1

    ans = runs

    for i in range(1, n - 1):
        cur = runs

        # deleting a single-character block
        if s[i] != s[i - 1] and s[i] != s[i + 1]:
            cur -= 1

            # merge two equal neighboring blocks
            if s[i - 1] == s[i + 1]:
                cur -= 1

        ans = min(ans, cur)

    return ans

def solve_3(n, s):
    nls = list(s)
    nls.pop()
    nls.remove(s[0])
    if n == 0:
        return 0
    cnt = []
    or_s = dict.fromkeys(nls)
    un_s = list(or_s)
    for i in range(0, len(un_s)):
        cnt.append((un_s[i], nls.count(un_s[i])))
    val, count = min(cnt)
    ls = list(s)
    ls.remove(val)
    ls = list(s[0])+list(s)+list(s[n-1])
    # now for lenght of compressed string 
    s = ''.join(ls) 
    return len(set(s))

def solve(n, s): 
    

def main():
    t = inp()
    for tc in range(1, t+1):
        n = int(input())
        s = input().strip()
        print(solve(n, s))

if __name__ == '__main__':
    main()



