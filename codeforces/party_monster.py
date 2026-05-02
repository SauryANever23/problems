"""
Yousef has given you a sequence 𝑠
 of length 𝑛
 consisting only of characters '(
' and ')
'. You are allowed to perform the following operation at most once:

Choose a substring∗
 of 𝑠
 and remove it. Then, you may reinsert the removed characters back into the remaining string one by one. Each character can be placed at any arbitrary position, independently of the others.
Yousef wants you to determine whether it is possible to obtain a regular bracket sequence†
 after performing the operation at most once.

∗
A substring is a contiguous subsegment of a string. For example, "acab" is a substring of "abacaba" (it starts in position 3
 and ends in position 6
), but "aa" or "d" aren't substrings of this string. So the substring of the string 𝑠
 from position 𝑙
 to position 𝑟
 is 𝑠[𝑙,𝑟]=𝑠𝑙𝑠𝑙+1…𝑠𝑟
.

†
A regular bracket sequence is a bracket sequence that can be transformed into a correct arithmetic expression by inserting the characters 1
 and +
 between the original characters of the sequence. For example:

bracket sequences ()()
 and (())
 are regular (the resulting expressions are: (𝟷)+(𝟷)
 and ((𝟷+𝟷)+𝟷)
);
bracket sequences )(
, (
 and )
 are not.
Input
The first line contains an integer 𝑡
 (1≤𝑡≤104
) — the number of test cases. The descriptions of the test cases follow.

The first line of each test case contains a single integer 𝑛
 (1≤𝑛≤2⋅105
) — the length of the string 𝑠
.

The second line of each test case contains a sequence 𝑠
 of length 𝑛
 consisting only of characters '(
' and ')
'.

It is guaranteed that the sum of 𝑛
 over all test cases does not exceed 2⋅105
.

Output
For each test case, output "YES" if the sequence can be made regular, and "NO" otherwise.

You can output the answer in any case (upper or lower). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive responses.
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

