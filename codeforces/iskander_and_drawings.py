
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
        soln.append(int(size[i]/2))
    elif len(clean_lines) == 0: 
        soln.append(0)
    elif pages[i].startswith('*') or pages[i].endswith('*'): 
        clean = pages[i]
        soln.append(len(clean)//2)
    else:
        count = 0 
        break_lines = pages[i].split('*')

        for index in range(len(break_lines)//2): 
            if len(break_lines[index]) in [1, 2]:
                count += 1 
                
            
        soln.append(count)
                
for sol in soln:
    print(sol)

                



