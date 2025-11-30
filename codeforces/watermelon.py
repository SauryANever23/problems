# watermelon

w = int(input())

if (w > 100 or w < 100):
    raise exception("Invald Input")

if (w % 2 == 0):
    print("YES")
else:
    print("NO")
