class Product:

    def __init__(self, name, price, quantity):
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        if not name:
            raise ValueError("Name can not be empty.")

        if not isinstance(price, (float, int)):
            raise TypeError("Price must be an integer or float.")
        if price < 0:
            raise ValueError("Price can not be negative.")
        if not price:
            raise ValueError("Price can not be zero.")

        if not isinstance(quantity, int):
            raise TypeError("Quantity must be a whole number.")
        if quantity < 0:
            raise ValueError("Quantity can not be negative.")
        if not quantity:
            raise ValueError("Quantity can not be zero.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True


    def is_active(self):
        return self.active


    def deactivate(self):
        self.active = False


    def activate(self):
        self.active = True


    def get_quantity(self):
        return self.quantity


    def set_quantity(self, quantity):
        if quantity < 0:
            raise ValueError("Quantity can not be negative.")
        self.quantity = quantity
        if self.quantity > 0:
            self.activate()
        elif self.quantity == 0:
            self.deactivate()



    def show(self):
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"


    def buy(self, quantity):
        if not isinstance(quantity, int):
            raise TypeError("Quantity must be a whole number.")
        if quantity > self.quantity:
            raise ValueError(f"Only {self.quantity} piece(s) left in the store")
        if quantity < 0:
            raise ValueError("Quantity can not be negative.")
        self.quantity -= quantity
        if self.quantity == 0:
            self.deactivate()
        return quantity * self.price



bose = Product("Bose QuietComfort Earbuds", price=50, quantity=115)
mac = Product("MacBook Air M2", price=1450, quantity=100)

print(bose.show())
print(bose.is_active())
print(bose.buy(50))
print(bose.show())
print(bose.is_active())
print()
print(mac.show())
print(mac.buy(100))
print(mac.show())
print(mac.is_active())
print()
print(bose.show())
print(mac.show())
print()
bose.set_quantity(1000)
mac.set_quantity(1000)
print(mac.is_active())
print(mac.show())
print(bose.show())
