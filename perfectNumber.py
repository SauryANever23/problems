"""
Trying to find perfect numbers
"""

def is_perfect(n: int) -> bool:
    div_array = []
    for i in range(n):
        if n % i == 0:
            div_array.append(i)
    div_array.remove(n)
    sm = sum(div_array)
    if sm == n:
        return True 

def main():
    for i in range(10000):
        if is_perfect(i):
            print(i)

if __name__ == '__main__':
    main()
