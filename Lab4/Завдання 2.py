import math

x = float(input("x = "))
y = float(input("y = "))

F = (pow((math.sqrt(math.pow(x,3) + math.pow(y,3))), 1/4) + math.sin(3*x + 1) + math.log(abs(x)) - math.pow(math.e, y-x))

print("F = ", F)