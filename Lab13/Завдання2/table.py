class TABLE:
    def __init__(self, inventory_number, color, year, price):
        self.inventory_number = inventory_number
        self.color = color
        self.year = year
        self.price = price

    def change_inventory_number(self, new_number):
        self.inventory_number = new_number

    def change_price(self, new_price):
        self.price = new_price

    def show_info(self):
        print("Інвентарний номер:", self.inventory_number)
        print("Колір:", self.color)
        print("Рік виготовлення:", self.year)
        print("Ціна:", self.price, "грн")
        print("-" * 30)
