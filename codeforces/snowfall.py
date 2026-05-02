"""

"""
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    A = []  # divisible by 6
    B = []  # divisible by 2 only
    C = []  # divisible by 3 only
    D = []  # divisible by neither

    for x in arr:
        if x % 6 == 0:
            A.append(x)
        elif x % 2 == 0:
            B.append(x)
        elif x % 3 == 0:
            C.append(x)
        else:
            D.append(x)

    # Construct answer
    result = B + D + A + C
    print(*result)

