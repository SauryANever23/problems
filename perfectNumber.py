"""
Trying to find perfect numbers
"""
import time 

def is_perfect(n: int) -> bool:
    div_array = []
    for i in range(1, n):
        if n % i == 0:
            div_array.append(i)
    sm = sum(div_array)
    if sm == n:
        return True 

def main():
    star_time = time.perf_counter()
    for i in range(10000):
        if is_perfect(i):
            print(i)
    end_time = time.perf_counter()
    time_elapsed = end_time - star_time
    print(f"Elapsed Time: {time_elapsed:0.4f} seconds")

if __name__ == '__main__':
    main()
