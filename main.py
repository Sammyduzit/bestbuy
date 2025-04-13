import colorama

import products
import store
from colorama import Fore

colorama.init(autoreset=True)

def exit_program():
    print(f"{Fore.GREEN}Exiting the program. Goodbye!")
    exit()


def display_products(my_store):
    active_products = my_store.get_all_products()
    print("------")
    for i, product in enumerate(active_products, start=1):
        print(f"{i}. {product.show()}")
    print("------")


def display_menu():
    print("\n\tStore Menu\n"
          "\t----------\n"
          "1. List all products in store\n"
          "2. Show total amount in store\n"
          "3. Make an order\n"
          "4. Quit\n")


def display_total_product_quantity(my_store):
    print("------")
    print(my_store.get_total_quantity())
    print("------")


def get_product_number_input(product_list):
    while True:
        product_choice = input("Which product # do you want? ")
        if not product_choice:
            break

        active_products_amount = len(product_list)
        try:
            product_number = int(product_choice)
        except ValueError:
            print(f"{Fore.RED}Please enter a valid number")
            continue

        if product_number > active_products_amount or 0 >= product_number:
            print(f"{Fore.RED}Please enter a valid number in the range between 1 and {active_products_amount}")
            continue
        else:
            return product_number



def get_product_amount_input():
    pass


def order_products(my_store):
    display_products(my_store)
    shopping_list = []
    product_list = my_store.get_all_products()
    print("When you want to finish order, enter empty text.")
    while True:
        product_choice = input("Which product # do you want? ")
        if not product_choice:
            break

        active_products_amount = len(product_list)
        try:
            product_number = int(product_choice)
        except ValueError:
            print(f"{Fore.RED}Please enter a valid number")
            continue
        if product_number > active_products_amount or 0 >= product_number:
            print(f"{Fore.RED}Please enter a valid number in the range between 1 and {active_products_amount}")
            continue


        while True:
            quantity_choice = input("What amount do you want? ")
            if not quantity_choice:
                break

            try:
                quantity_choice = int(quantity_choice)
            except ValueError:
                print(f"{Fore.RED}Please enter a valid number")
                continue

            product_index = product_number - 1
            available_product_quantity = product_list[product_index].get_quantity()
            if quantity_choice > available_product_quantity or quantity_choice <= 0:
                print(f"{Fore.RED}Please enter a valid number in the range between 1 and {available_product_quantity}")
                continue
            else:
                shopping_list.append((product_list[product_index], quantity_choice))
                print()
                break
        if not shopping_list:
            break

    if shopping_list:
        total_price = my_store.order(shopping_list)
        print(f"********\nOrder successful! Total payment: {total_price}")


def start(my_store):
    display_menu()
    user_choice = input("Please choose a number: ")
    dispatcher = {
        "1": display_products,
        "2": display_total_product_quantity,
        "3": order_products,
        "4": exit_program,
    }
    if user_choice in dispatcher:
        dispatcher[user_choice](my_store)
    else:
        print("Invalid input, please enter a number between 1-4.")




def main():
    # setup initial stock of inventory
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250)
                    ]
    best_buy = store.Store(product_list)
    while True:
        start(best_buy)




    # all_products = best_buy.get_all_products()
    # for product in all_products:
    #     print(product.show())





    # product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
    #                 products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    #                 products.Product("Google Pixel 7", price=500, quantity=250),
    #                 ]
    #
    # best_buy = store.Store(product_list)
    # all_products = best_buy.get_all_products()
    # print(best_buy.get_total_quantity())
    # print(best_buy.order([(all_products[0], 100), (all_products[1], 2)]))
    # print(best_buy.get_all_products())


if __name__ == "__main__":
    main()