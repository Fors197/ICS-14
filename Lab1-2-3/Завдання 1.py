number = int(input("Введіть п'ятизначне число:"))
a = number // 10000
b = number % 10
c = (number // 1000) % 10
d = (number // 100) % 10
print("Добуток першої та останньої цифр", a * b)
print("Сума другої і третьої цифр", c + d)
