from src.item import Item

# Создаем товары
item1 = Item("Item1", 100, 10)
item2 = Item("Item2", 150, 5)

# Устанавливаем скидку
Item.set_discount_rate(0.85)

# Выводим среднюю стоимость товара
avg_price = Item.get_average_price()
print(f"Average price: {avg_price}")

# Выводим скидку для каждого товара
print(f"Discounted price for {item1.name}: {item1.get_discounted_price()}")
print(f"Discounted price for {item2.name}: {item2.get_discounted_price()}")

