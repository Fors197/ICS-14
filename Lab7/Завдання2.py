words = []

line = input("Введіть рядок слів (або натисніть Enter для завершення): ")

while line != "":
    for word in line.split():
        if word not in words:
            words.append(word)

    line = input()

result = " ".join(words)

print("Результат:", result)