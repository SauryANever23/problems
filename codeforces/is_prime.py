
def is_prime(n: int) -> bool: 
    if n == 2 or n == 3: 
        return True 

    if n % 2 == 0 or n % 3 == 0: 
        return False
    count = 0 
    for i in range(1, n//2):
        if n % i == 0: 
            count += 1 

    if count == 1: 
        return True
    else: 
        return False

if __name__ == '__main__':
    n = int(input())
    print(is_prime(n))
