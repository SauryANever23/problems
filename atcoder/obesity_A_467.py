h, w = map(int, input().split())

bmi = w / ((h/100) * (h/100))

if int(bmi) >= 25:
    print("Yes")
else:
    print("No")
