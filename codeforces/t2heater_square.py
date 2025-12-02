# optimised theather_square code 
# formula for ceilling 
# as the problem is two dimentional, 
# calculate the tiles required in both m and n dimentions 

n, m, a = map(int, input())

# ceilling division 
lenght_flagstones = (n+a-1)//a 
width_flagstones = (m+a-1)//a 

print(lenght_flagstones*width_flagstones)




