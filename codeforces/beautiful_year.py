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

def is_distinct(n: int):
    if len(set(list(str(n)))) == len(list(str(n))):
        return True
    return False

def solve(n: str):
    # what is a beautiful year? 
    # any year with all distince numbers 
    # give a year, take the first three letters 
    next_year = n
    while True: 
        next_year += 1 
        if is_distinct(next_year):
            return next_year


def main():
    try:
        n = input()
        print(solve(n))
    except (ValueError, IndexError):
        pass 

if __name__ == '__main__':
    main()



