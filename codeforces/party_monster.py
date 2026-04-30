"""
Yousef has given you an array 𝑎
 of 𝑛
 positive integers.

Let 𝑓(𝑎)
 denote the number of subarrays∗
 of 𝑎
 whose product is divisible by 6
.

More formally, for every pair of indices 𝑙
 and 𝑟
 such that 1≤𝑙≤𝑟≤𝑛
, consider the subarray 𝑎𝑙,𝑎𝑙+1,…,𝑎𝑟
. This subarray is counted if the product of its elements is divisible by 6
.

For example, if 𝑎=[1,6,2]
, then the subarrays whose products are divisible by 6
 are [6]
, [1,6]
, [6,2]
, and [1,6,2]
, so 𝑓(𝑎)=4
.

Your task is to reorder the elements of the array 𝑎
 so that 𝑓(𝑎)
 is minimized. If there are multiple ways to do this, you may output any of them.

∗
An array 𝑏
 is a subarray of an array 𝑎
 if 𝑏
 can be obtained from 𝑎
 by deleting several (possibly zero or all) elements from the beginning and several (possibly zero or all) elements from the end.

Input
The first line of the input contains an integer 𝑡
 (1≤𝑡≤104
) — the number of test cases.

The first line of each test case contains an integer 𝑛
 (1≤𝑛≤2⋅105
) — the size of the array.

The second line of each test case contains 𝑛
 integers 𝑎1,𝑎2,…,𝑎𝑛
 (1≤𝑎𝑖≤109
) — the elements of the array.

It is guaranteed that the sum of 𝑛
 over all test cases does not exceed 2⋅105
.

Output
For each test case, output the array after reordering it in such a way that 𝑓(𝑎)
 is minimized. If there are multiple answers, you may output any of them.


"""
t = int(input())

objs = []
for i in range(t):
    n = int(input())
    parens = input()
    objs.append(parens)

pair = "()"
for obj in objs:
    clear = obj.replace(pair, "")
    # if len(clear) % 2 != 0 or len(set(clear)) == 1:  
    if obj.count("(") == obj.count(")"):
        print("YES")
    else:
        print("NO")

