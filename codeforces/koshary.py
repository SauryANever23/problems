"""
Yousef is at the coordinates (0,0)
 and wants to reach a plate of Koshary at (𝑥,𝑦)
.

To get there, Yousef takes long steps. From any point (𝑎,𝑏)
, a long step moves him to:

(𝑎+2,𝑏)
 or (𝑎,𝑏+2)
However, Yousef is allowed to take at most one short step during his entire journey. A short step moves him to:

(𝑎+1,𝑏)
 or (𝑎,𝑏+1)
Can Yousef reach the exact coordinates (𝑥,𝑦)
 of the Koshary plate?

Input
The first line contains an integer 𝑡
 (1≤𝑡≤100
) — the number of test cases.

Each test case contains two integers 𝑥
 and 𝑦
 (1≤𝑥,𝑦≤10
) — the coordinates of the Koshary plate.

Output
For each test case, output "YES" if Yousef can reach the Koshary plate and "NO" otherwise.

You can output the answer in any case (upper or lower). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive responses.
"""

t = int(input())

nums = []

for i in range(t):
    (x, y) = tuple(map(int, input().split()))
    nums.append((x, y))

for num in nums:
    x, y = num
    if x % 2 == 0 or y % 2 == 0:
        print("YES")
    else:
        print("NO")
    
    

