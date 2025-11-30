# bit++ language
# operation ++, --
# variable x only with initial value 0 

x = 0
n = int(input())

for _ in range(n):
    statement = input()
    if "+" in statement:
        x += 1
    elif "-" in statement:
        x -= 1 
print(x)
