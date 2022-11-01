import math

def euler(n):
    
    sum_e = 0
    for a in range(n):
        euler = 1/math.factorial(a)
        sum_e += euler

    return sum_e

n = int(input("enter n in 1/n!"))
e = euler(n)
print("e= ",e)
