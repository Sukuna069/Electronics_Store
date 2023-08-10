class Item:
    # Атрибуты класса для хранения уровня цен с учетом скидки и созданных экземпляров
    discount_rate = 1.0
    instances = []

    def __init__(self, name, price_per_unit, quantity):
        self.name = name
        self.price_per_unit = price_per_unit
        self.quantity = quantity
        self.__class__.instances.append(self)

    @classmethod
    def set_discount_rate(cls, rate):
        cls.discount_rate = rate

    @classmethod
    def get_average_price(cls):
        total_price = sum(item.price_per_unit for item in cls.instances)
        return total_price / len(cls.instances)

    def get_discounted_price(self):
        return self.price_per_unit * self.discount_rate
