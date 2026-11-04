import random
import os

# Функція для отримання унікальних слів
def unique_words(filename):
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read()

    words = text.split()
    unique = []

    for word in words:
        word = word.strip(".,!?;:")
        if word.lower() not in [w.lower() for w in unique]:
            unique.append(word)

    return unique


# Отримання списку унікальних слів
words = unique_words(r"E:\Labs\ICS-14\Lab12\Завдання2\text.txt")

# Введення кількості випадкових слів
print("Поточна кількість унікальних слів у тексті:", len(words))
N = int(input("Введіть кількість слів N: "))

if 0 <= N <= len(words):
    print("Випадкові слова:")
    print(*random.sample(words, N), sep="\n")
else:
    print("Помилка! Введіть N від 0 до", len(words))
