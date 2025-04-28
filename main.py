import products
import store
from colorama import Fore, init
import ui

init(autoreset=True)


def initialize_store():
    """
    Initializes the store with a predefined set of products.

    :return: An instance of store.Store containing the initial product inventory.
    """
    # Setup initial stock of inventory
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250)
    ]
    return store.Store(product_list)


def start(my_store):
    """
    Start the main menu loop.
    :param my_store: The store instance containing the products.
    :return: None
    """
    ui.display_menu()
    user_choice = input("Please choose a number: ")
    dispatcher = {
        "1": lambda: ui.display_products(my_store),
        "2": lambda: ui.display_total_product_quantity(my_store),
        "3": lambda: ui.order_products(my_store),
        "4": lambda: ui.exit_program(),
    }

    action = dispatcher.get(user_choice)
    if action:
        action()
    else:
        print(f"{Fore.RED}Invalid input. Please enter a number between 1 and {len(dispatcher)}.")


def main():
    """
    This program simulates a store management system where users can view products,
    check total quantities, and order products.

    The program runs in a loop, displaying a menu of options for interaction with the store's inventory.
    :return: None
    """
    best_buy = initialize_store()

    try:
        while True:
            start(best_buy)
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting...")
    except Exception as e:
        print(f"{Fore.RED}An error occurred: {e}")


if __name__ == "__main__":
    main()