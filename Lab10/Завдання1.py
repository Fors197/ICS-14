import random

with open("numbers.txt", "r") as file:
    numbers = file.readlines()

with open("full_numbers.txt", "w") as file:
    for number in numbers:
        series = number.strip()
        full_number = series + str(random.randint(1000, 9999))
        file.write(full_number + "\n")

print("Номери успішно записано у файл full_numbers.txt")
