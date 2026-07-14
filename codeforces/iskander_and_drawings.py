
t = int(input())

size = []
pages = []
for i in range(t):
    n = int(input())
    s = input()
    size.append(n)
    pages.append(s)

soln = []
for i in range(t):
    hash_list = pages[i].split("*")
    len_list = [len(i) for i in hash_list if len(i) != 0]
    # tot_len = max(len_list)
    time = []
    for seg in len_list: 
        time.append((seg+1)//2)
    if len(time) != 0:
        soln.append(max(time))
    else:
        soln.append(0)
for sol in soln:
    print(sol)


                



