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

def solve(points: list):

    """
         Takashi at positoin 0 
         he has to travel to the coordinate with the smallest distanece from current position 
         if two numebrs have the same distance, he chooses the smaller point 
         keep track of the current position 
         then update the postion as it goes on , 
         
         then serach the array to find the optimum route 
         and update the current position 
    """
    # current position
    cnt_pos = 0
    
    # total distance travelled 
    s = 0 

    while len(points) > 0: 
    distance = []
    for i in range(len(points)): 
        distance.append((i, abs(cnt_pos-points[i])))
    # distance.sort(key=lambda x: x[1])
    mn_distance = min(x[i] for x in distance)
    # removing all elements whose distance is not mn mn_distance 
    cnt_pos = min(
            points[i] for i, d in distance 
            if d == mn_distance 
            )
    s += mn_distance 
    points.remove(cnt_pos) 

    return s 

def main():
    try:
        t = 1
        for tc in range(1, t+1):
            n = inp()
            arr = init()
            print(solve(arr))
    except IndexError:
        pass 

if __name__ == '__main__':
    main()



