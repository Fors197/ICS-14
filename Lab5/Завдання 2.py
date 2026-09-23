import math

ax = int(input("Введіть x точки A(x, y): "))
ay = int(input("Введіть y точки A(x, y): "))
bx = int(input("Введіть x точки B(x, y): "))
by = int(input("Введіть y точки B(x, y): "))
cx = int(input("Введіть x точки C(x, y): "))
cy = int(input("Введіть y точки C(x, y): "))

ak = (abs(ax) + abs(ay))
bk = (abs(bx) + abs(by))
ck = (abs(cx) + abs(cy))

if (ak <= bk and ak <= ck):
    print(f"Точка A({ax}, {ay}) найближча до початку координат")
elif (bk <= ak and bk <= ck):
    print(f"Точка B({bx}, {by}) найближча до початку координат")
else:
    print(f"Точка C({cx}, {cy}) найближча до початку координат")