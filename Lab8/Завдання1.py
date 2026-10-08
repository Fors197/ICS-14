numbers = []

print("Введіть 7 цілих чисел:")
for i in range(7):
    num = int(input(f"Елемент {i + 1}: "))
    numbers.append(num)

print("\nДодатні дільники кожного елемента:")

for num in numbers:
    if num == 0:
        print(f"Дільники для {num}: будь-яке число (крім 0)")
        continue
    
    abs_num = abs(num)
    divisors = []

    for d in range(1, abs_num + 1):
        if abs_num % d == 0:
            divisors.append(str(d))

    print(f"Дільники для {num}:", " ".join(divisors))