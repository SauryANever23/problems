if __name__ == '__main__':
    N = int(input())
    
    lst = []

    def ins(e, i):
        lst.insert(e, i)
    
    def prt(lst):
        print(lst)

    def rm(e):
        lst.remove(e)

    def app(e):
        lst.append(e)

    for i in range(N):
        n = input()
        n_list = n.split()

        if n_list[0].lower() == "insert":
            ins(n_list[1], n_list[2])
        elif n_list[0].lower()
