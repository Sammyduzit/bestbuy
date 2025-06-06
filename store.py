from typing import List
from products import Product

class Store:
    """
    A class to represent a store that manages a list of products.
    """
    def __init__(self, product_list):
        """
         Initialize a new Store instance.
        :param product_list: List of Product instances to initialize the store with.
        """
        if not all(isinstance(product, Product) for product in product_list):
            raise TypeError("All items in product_list must be instances of Product.")
        self.product_list = product_list


    def add_product(self, product):
        """
        Add a product to the store's product list.
        If the product already exists, updates quantity.
        :param product: Product to add to the store.
        :return: None
        """
        #Check if product already is in product list, if yes, update quantity
        for existing_product in self.product_list:
            if existing_product.name == product.name:
                existing_product.set_quantity(existing_product.get_quantity() + product.get_quantity())
                return
        self.product_list.append(product)



    def remove_product(self, product_name):
        """
        Remove a product from the store's product list.
        :param product_name: Product (by name) to remove from the store.
        :return: None
        :raises: ValueError: If the product is not found in the store's product list.
        """
        for product in self.product_list:
            if product.name == product_name:
                self.product_list.remove(product)
                return
        raise ValueError(f"Product {product_name} is not in the store.")


    def get_total_quantity(self) -> int:
        """
        Calculate the total quantity of all products in the store.
        :return: Total quantity of all products in the store.
        """
        total_quantity = sum(product.get_quantity() for product in self.product_list)
        return total_quantity


    def get_all_products(self) -> List["Product"]:
        """
        Get a list of all active products in the store.
        :return: List[Product]: A list of all active products
        """
        active_products = [product for product in self.product_list if product.is_active()]
        return active_products


    def order(self, shopping_list) -> float:
        """
        Process an order for a given shopping list.
        :param shopping_list: A list of tuples, where each tuple consists of a product instance and its quantity
        :return: float: Total price of the order.
        :raises: ValueError: If any product in the shopping list is invalid or inactive.
        """
        total_price = 0.0
        for item, quantity in shopping_list:
            if not isinstance(item, Product):
                raise TypeError(f"Invalid product: {item}")
            if not item.is_active():
                raise ValueError(f"Product {item.name} is not active.")
            try:
                price = item.buy(quantity)
                total_price += price
            except Exception as e:
                print(f"Error processing {item.name}: {e}")

        return total_price