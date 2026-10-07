import random

M = int(input("Введіть кількість рядків (M): "))
N = int(input("Введіть кількість стовпчиків (N): "))

A = []
for i in range(M):
    row = []
    for j in range(N):
        row.append(random.randint(0, 1))
    A.append(row)

print("\nПочатковий масив A:")
for row in A:
    for val in row:
        print(val, end=" ")
    print()

for row in A:
    ones_count = row.count(1)

    if ones_count % 2 != 0:
        row.append(1)
    else:
        row.append(0)

print("\nМасив після додавання стовпчика:")
for row in A:
    for val in row:
        print(val, end=" ")
    print()