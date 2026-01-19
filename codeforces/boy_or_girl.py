"""
This is his method: if the number of distinct characters in one's user name is odd, then he is a male, otherwise she is a female. You are given the string that denotes the user name, please help our hero to determine the gender of this user by his method.

Input
The first line contains a non-empty string, that contains only lowercase English letters — the user name. This string contains at most 100 letters.

Output
If it is a female by our hero's method, print "CHAT WITH HER!" (without the quotes), otherwise, print "IGNORE HIM!" (without the quotes).
"""

m = input()

ml = list(m)
mls = set(ml)
val=len(mls)
if val % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
