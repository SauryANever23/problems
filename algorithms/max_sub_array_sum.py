
"""
Max subarray sum using different algorytms in python
"""

import time 
import sys 

def max_subarray_sum(arr: list) -> tuple: 
    start_time = time.perf_counter()
    best = 0 
    for i in range(len(arr)):
        for j in range(i):
            sm = 0
            for k in range(j):
                sm = sum(arr[j:k])
            best = max(best, sm)
    end_time = time.perf_counter()

    elapsed = (end_time - start_time) * 1000
    return (best, f"{elapsed:.3f}")
    
def max_subarrary(arr: list) -> tuple: 
    pass
def main():
    # arr = list(map(int, input().split()))
    arr = list(map(int, "-1 2 4 -3 5 2 -5 2".split()))
    print(max_subarray_sum(arr))

if __name__ == '__main__':
    main()
