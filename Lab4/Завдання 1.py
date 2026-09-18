import math

x = float(input("x = "))

f = (abs(math.sin(2*x) + math.cos(3*x + 1) + math.tan(abs(x) + 0.7)) + math.log10(abs(x - 4)))

print("f(x) = ", f)