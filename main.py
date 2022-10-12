a = int(input("First number"))
b = int(input("Second number")) 
if a>b:
    x, y = a, b
    a = y
    b = x
r=a%b
while r:
    a=b
    b=r
    r=a%b
print('OBEB:', b)
