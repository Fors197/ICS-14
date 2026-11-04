class TABLE:
    def __init__(self, inventory_number, color, year, price):
        self.number = inventory_number
        self.color = color
        self.year = year
        self.price = price

    # Метод зміни інвентарного номера
    def change_inventory_number(self, new_number):
        self.number = new_number

    # Метод зміни ціни
    def change_price(self, new_price):
        self.price = new_price

    # Метод виведення інформації
    def show_info(self):
        print("Інвентарний номер:", self.number)
        print("Колір:", self.color)
        print("Рік виготовлення:", self.year)
        print("Ціна:", self.price, "грн")
        print("-" * 30)


# Створення списку об'єктів класу TABLE
tables = [
    TABLE(101, "Коричневий", 2020, 2500),
    TABLE(102, "Білий", 2022, 3200),
    TABLE(103, "Чорний", 2023, 4000)
]

# Виведення інформації про столи
print("Список столів:")
for table in tables:
    table.show_info()

# Зміна даних першого столу
tables[0].change_inventory_number(201)
tables[0].change_price(3000)

# Виведення оновленої інформації
print("Після зміни даних:")
tables[0].show_info()
