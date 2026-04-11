"""

"""

t = int(input())

arr = list(map(int, input().split()))
sort_arr = arr.sort()

negeted_arr = [-1*sort_arr[i] for i in range(0, len(sort_arr)-1)]
print(negeted_arr)
