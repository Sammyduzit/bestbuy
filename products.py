class Product:

    def __init__(self, name, price, quantity):
        """
        Initializing a new Product instance.
        :param name: Name of the product. Must be a non-empty string.
        :param price: Price of the product. Must be an integer greater than zero.
        :param quantity: Quantity of the product in stock. Must be a positive integer.
        """
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


    def is_active(self) -> bool:
        """
        Check if the product is active.
        :return: bool: True if product is active, False otherwise.
        """
        return self.active


    def deactivate(self):
        """
        Deactivate the product, marking it as unavailable for purchase.
        :return: None
        """
        self.active = False


    def activate(self):
        """
        Activate the product, marking it as available for purchase.
        :return: None
        """
        self.active = True


    def get_quantity(self) -> int:
        """
        Get the current quantity of the product in stock.
        :return: int: Quantity of the product in stock.
        """
        return self.quantity


    def set_quantity(self, quantity):
        """
        Set the quantity of the product.
        :param quantity: The new quantity of the product. Must be a non-negative integer.
        :return: None
        :raises: ValueError: If quantity is negative.
        """
        if quantity < 0:
            raise ValueError("Quantity can not be negative.")
        self.quantity = quantity
        if self.quantity > 0:
            self.activate()
        elif self.quantity == 0:
            self.deactivate()



    def show(self) -> str:
        """
        Return a string representation of the product's details (name, price, quantity)
        :return: String with the product's name, price, and quantity.
        """
        return f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}"


    def buy(self, quantity) -> float:
        """
        Buy a specified quantity of the product.
        :param quantity: Number of items to buy. Must be a positive integer and not exceed the available stock.
        :return: float: Total cost of the purchase.
        :raises:    TypeError: If the quantity is not an integer.
                    ValueError: If the quantity is invalid (negative or exceeds stock).
        """
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

