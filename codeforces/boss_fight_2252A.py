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

def solve(n: int, a: list):
    """
    check if the list has duplicates? 
    if does not sum it directly 
    if does 
    the place the two duplicates at the last 
    what if has multiples duplicates, 
    find the largest dupliates and place them before teh smaller ones 
    but if you have just 2 duplicates, 
    you dont have to paly them together, 
    
    so how to actually solve this problem? 
    first sort is desciding roder 
    then find the duplicates 
    place the duplicated not together 
    """
    hasdupes = len(a) != len(set(a))
    a.sort(reverse=True)
    sep = Counter(a)
    dupes = [i for i, count in sep.items() if count > 1]
    rest = []
    for i in range(n):
        if a[i] in dupes:
            rest.append(a[i])
            a.remove(a[i])
    rest.sort(reverse=True)
    if len(rest) > len(a): 
        sm += sum(a)
        sm += sum(rest[:-(len(rest)-len(a))])
        return sm 
    

def main():
    try:
        t = inp()
        for tc in range(1, t+1):
            n = inp()
            a = init()
            print(solve(n, a))
    except (ValueError, IndexError):
        pass 

if __name__ == '__main__':
    main()



