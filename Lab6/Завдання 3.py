import math

a = float(input("a = "))
b = float(input("b = "))
h = float(input("h = "))

x = a

len=[]

while x <= b:
    f = pow(math.e, x) + pow(abs(x), 1/2)
    print("x =", x, "f(x) =", f)
    x += h
    len.append(f)
print(len)