N = int(input("Введіть число: "))

# Таблиця множення
def tabl1(N):
    for K in range(1, N + 1):
        print(f"\nТаблиця множення на {K}:")
        for i in range(1, 11):
            print(f"{K} * {i} = {K * i}")


# Таблиця Піфагора
def tabl2(N):
    for K in range(1, N + 1):
        for i in range(1, N + 1):
            print(f"{K * i:4}", end="")
        print()


tabl1(N)

print("\nТаблиця Піфагора:")
tabl2(N)
