from collections import Counter
import csv

with open("words.txt", "r", encoding="utf-8") as file:
    words = file.read().split()

counts = Counter(words)

with open("words.csv", "w", newline="", encoding="utf-8-sig") as file:
    writer = csv.writer(file)

    writer.writerow(["Слово", "Частота"])

    for word, count in counts.items():
        writer.writerow([word, count])

print("Частоту слів записано у файл words.csv")
