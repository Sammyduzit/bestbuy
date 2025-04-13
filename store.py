class Store:

    def __init__(self, product_list):
        self.product_list = product_list


    def add_product(self, product):
        self.product_list.append(product)


    def remove_product(self, product):
        if product in self.product_list:
            self.product_list.remove(product)
        else:
            print(f"{product} is not in the list of products")


    def get_total_quantity(self):
        total_quantity = 0
        for product in self.product_list:
            total_quantity += product.get_quantity()

        return f"Total of {total_quantity} items in store."


    def get_all_products(self):
        active_products = []
        for product in self.product_list:
            if product.is_active():
                active_products.append(product)
        return active_products


    def order(self, shopping_list) -> float:
        total_price = 0
        for item, quantity in shopping_list:
            price = item.buy(quantity)
            total_price += price

        return total_price