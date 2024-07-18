

class Phone:
    """Telefon obyektlari uchun shablon"""
    def __init__(self, make: str, model: str, price: int) -> None:
        self.make, self.model, self.price = make, model, price

    @property
    def price(self):
        return self.__dict__['price']

    @price.setter
    def price(self, value):
        if not isinstance(value, int):
            raise ValueError("Qiymat berishda hatolikka yo'l qo'yildi")
        else:
            self.__dict__['price'] = value


phone = Phone('Samsung', 'Galaxy A10', 120)
print(phone.price)
