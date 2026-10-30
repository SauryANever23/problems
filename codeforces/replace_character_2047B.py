def solve(tc): 
    n = int(input())
    s = input()
    sl = list(s)
    sls = set(list(s))
    
    freq = [sl.count(a) for a in sls]
    ch = [a for a in sls]
    
    if freq.count(max(freq)) > 1: 
        mx = min([a for a in ch if freq[ch.index(a)] == max(freq)])
    else: 
        mx = ch[freq.index(max(freq))]
    if freq.count(min(freq)) > 1: 
        mn = max([a for a in ch if freq[ch.index(a)] == min(freq)]) 
    else: 
        mn = ch[freq.index(min(freq))]

        
    w = s.replace(mn, mx, 1)
    
    return w 

def main():
    ans = []
    t = int(input())
    for tc in range(1, t+1):
        ans.append(solve(tc))

    print('\n'.join(ans))

if __name__ == '__main__':
    main()



