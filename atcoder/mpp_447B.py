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

def solve(s: str):
    if len(set(list(s))) == len(s):
        return ""
    ls = list(s)
    chars = set(list(s))

    letterCount = [(i, ls.count(i)) for i in chars]

    maxCount = max(letterCount, key=lambda item: item[1])

    removeLetters = [i[0] for i in letterCount if i[1] == maxCount[1]]
    for i in range(len(removeLetters)):
        for j in range(maxCount[1]): 
            ls.remove(removeLetters[i])
            
    return ''.join(ls)
    
def main():
    try:
        t = 1
        for tc in range(1, t+1):
            s = input().strip()
            print(solve(s))
    except (ValueError, IndexError):
        pass 

if __name__ == '__main__':
    main()



