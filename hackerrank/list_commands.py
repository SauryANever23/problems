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
            ins(int(n_list[1]), int(n_list[2]))
        elif n_list[0].lower() == "print":
            print(lst)
        elif n_list[0].lower() == 'remove':
            rm(int(n_list[1]))
        elif n_list[0].lower() == 'sort':
            lst.sort()
        elif n_list[0].lower() == 'append':
            lst.append(int(n_list[1]))
        elif n_list[0].lower() == 'pop':
            lst.pop(int(lst[-1]))
        elif n_list[0].lower() == 'reverse':
            lst.reverse()

        else:
            print("Invalid input")
