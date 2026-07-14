"""
let m, n (m<n) be 2 digit number then the total no of pair (m, n)  such that gcd = 6 is ___
"""
import math 
import random 

total = 0 

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

m = nums[random.randint(0, 9)]*10 + nums[random.randint(0, 9)]


