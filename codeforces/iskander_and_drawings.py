
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
    lines = list(pages[i])
    clean_lines = [l for l in lines if l != "*"]
    if '*' not in pages[i]:
        soln.append(n//2)
    elif len(clean_lines) == 0: 
        soln.append(0)
    else:
        count = 0 
        break_lines = pages[i].split('*')
        for index in range(len(break_lines)): 
            if len(break_line[index]) in [1, 2]:
                count += 1 
            else: 
                



