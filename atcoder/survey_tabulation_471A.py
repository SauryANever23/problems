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

def solve(soln):
    """
    find the numebr of same inputs 

    first normalise the array  

    then iterate thorught each elemtn in array from the set and ask thier freaquency in 
    the orginal array 
    if freaq is greater than 1, then add if to the count 
    """
    # firstly normalizing the input 
    soln = [i.lower() for i in soln]

    # keep counter 
    count = []

    # make a set of leemts 
    set_soln = set(soln)

    # iterate to check thorugh the elemtns 
    for i in set_soln: 
        cnt = soln.count(i) 
        count.append(cnt)
    return max(count) 
    
def main():
    try:
        t = inp()
        soln_arr = []
        for tc in range(1, t+1):
            a = input().strip()
            soln_arr.append(a)

        print(solve(soln_arr))
    except (ValueError, IndexError):
        pass 

if __name__ == '__main__':
    main()



