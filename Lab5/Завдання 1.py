import math

x = int(input("Ввдеіть число: "))

if (x >= 3.86):
    f = pow((2.25*x + pow(x, 2) + math.log(abs(x)))), 1/2
    print('f =', f)
elif (1.54 < x < 3.86):
    f = pow(math.e, 2) + (12 * pow(x, 2) - 1) / (x + 9)
    print('f =', f)
elif (x <= 1.54):
    f = math.log(abs(x)) - pow(x, x)
    print('f =', f)