T = ("Eagle", 2.3, 4, 3.4, "hello", 6.3)

numbers = list(T)
real_numbers = []

for item in numbers:
    if isinstance(item, float):
        real_numbers.append(item)

if len(real_numbers) > 0:
    average = sum(real_numbers) / len(real_numbers)
    print("Дійсні числа:", real_numbers)
    print("Середнє арифметичне:", average)
else:
    print("У списку немає дійсних чисел")