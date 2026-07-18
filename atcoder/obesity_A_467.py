h, w = map(int, input().split())

h = h/100 

bmi = w / h / h

if bmi >= 25:
    print("Yes")
else:
    print("No")
