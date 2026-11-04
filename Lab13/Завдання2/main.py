from table import TABLE

# Створення списку об'єктів
tables = [
    TABLE(101, "Коричневий", 2020, 2500),
    TABLE(102, "Білий", 2022, 3200),
    TABLE(103, "Чорний", 2023, 4000)
]

# Виведення інформації
print("Список столів:")
for table in tables:
    table.show_info()

# Зміна даних першого столу
tables[0].change_inventory_number(201)
tables[0].change_price(3000)

print("Після зміни даних:")
tables[0].show_info()
