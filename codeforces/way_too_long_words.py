# way to long words: if len > 10 
# abbreviation format: first lennter<between: number of letters between them: int>last letter

n = int(input())

def abbrev(word: str):
    fl, ll = word[0], word[-1]
    num = len(word) - 2 
    return fl+str(num)+ll
# using list for words and function call to return the abbrev values
word_arr = []
for _ in range(n):
    word = input()
    word_arr.append(word)

for i in range(len(word_arr)):
    if len(word_arr[i]) <= 10:
        print(word_arr[i])
    else:
        print(abbrev(word_arr[i]))
