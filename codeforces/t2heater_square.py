# optimised theather_square code 
# formula for ceilling 
# as the problem is two dimentional, 
# calculate the tiles required in both m and n dimentions 
import math 

n, m, a = map(int, input())

# ceilling division 
lenght_flagstones = math.ceil(n/a)
width_flagstones = math.ceil(m/a)

print(lenght_flagstones*width_flagstones)




