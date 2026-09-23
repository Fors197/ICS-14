import math

a = float(input("a = "))
b = float(input("b = "))
h = float(input("h = "))

x = a

for i in range(int((b - a) / h) + 1):
    f = pow(math.e, x) + pow(abs(x), 1/2)
    print("x =", x, "f(x) =", f)
    x += h