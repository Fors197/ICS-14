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

dist_a = math.sqrt(pow(ax, 2) + pow(ay, 2) )
dist_b = math.sqrt(pow(bx, 2)  + pow(by, 2) )
dist_c = math.sqrt(pow(cx, 2) + pow(cy, 2) )

if(ak <= bk and ak <= ck):
    name = "A"
    dist = dist_a
elif(bk <= ak and bk <= ck):
    name = "B"
    dist = dist_b
else:
    name = "C"
    dist = dist_c

print(f"Точка з найменшою сумою відстаней до осей: {name}")
print(f"Відстань від точки {name} до початку координат: {dist}")