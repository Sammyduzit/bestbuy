from colorama import Fore, init

init(autoreset=True)

def display_menu():
    """
    Display the main menu options.
    :return: None
    """
    print(f"{Fore.MAGENTA}\n\tStore Menu\n"
          "\t----------\n"
          "1. List all products in store\n"
          "2. Show total amount in store\n"
          "3. Make an order\n"
          "4. Quit\n")


def display_products(my_store):
    """
    Display all active products in the store.
    :param my_store: The store instance containing the products.
    :return: None
    """
    active_products = my_store.get_all_products()
    if not active_products:
        print(f"{Fore.YELLOW}No active products available in the store.")
        return

    print("------")
    for index, product in enumerate(active_products, start=1):
        print(f"{Fore.BLUE}{index}. {product.show()}")
    print("------")


def display_total_product_quantity(my_store):
    """
    Display the total quantity of all products in the store.
    :param my_store: The store instance containing the products.
    :return: None
    """
    total_quantity = my_store.get_total_quantity()
    print("------")
    print(f"{Fore.BLUE}Total of {total_quantity} items in store.")
    print("------")


def get_valid_input(prompt, max_value):
    """
    Prompt the user for a valid integer input. Checks if input is in specified range (0 until max_value)
    :param prompt: The input prompt message.
    :param max_value: The maximum allowed value.
    :return: int | None: The validated input, or None if the user cancels.
    """
    while True:
        choice = input(prompt)
        if not choice:
            return None

        try:
            value = int(choice)
        except ValueError:
            print(f"{Fore.RED}Please enter a valid number.")
            continue

        if value <= 0 or value > max_value:
            print(f"{Fore.RED}Please enter a valid number between 1 and {max_value}.")
            continue

        return value


def get_product_number_input(product_list):
    """
    Prompt the user to select a product by its number.
    :param product_list: The list of active products.
    :return: int | None: The selected product number, or None if the user cancels.
    """
    active_products_amount = len(product_list)
    product_prompt = "Which product # do you want? "
    return get_valid_input(product_prompt, active_products_amount)


def get_product_amount_input(product):
    """
    Prompt the user to specify the quantity of a selected product.
    :param product: The selected product.
    :return: int | None: The selected quantity, or None if the user cancels.
    """
    available_product_quantity = product.get_quantity()
    product_amount_prompt = "What amount do you want? "
    return get_valid_input(product_amount_prompt, available_product_quantity)


def display_shopping_list(shopping_list):
    """
    Display the shopping list in a formatted table.
    :param shopping_list: The shopping list.
    :return: None
    """
    if not shopping_list:
        print(f"{Fore.YELLOW}Your shopping list is empty.")
        return

    print("Order Summary:")

    # Print the header
    print(f"{'Product':<30} {'Amount':<10}")
    print("-" * 40)

    # Print each product and its amount
    for product, amount in shopping_list:
        print(f"{product.name:<30} {amount:<10}")


def order_products(my_store):
    """
    Allow the user to make an order by selecting products and quantities.
    :param my_store: The store instance containing the products.
    :return: None
    """
    display_products(my_store)
    shopping_dict = {}
    product_list = my_store.get_all_products()
    if not product_list:
        print(f"{Fore.YELLOW}No products available to order.")
        return

    print("When you want to finish order, enter empty text.")
    while True:
        product_number = get_product_number_input(product_list)
        if not product_number:
            break

        product_index = product_number - 1
        selected_product = product_list[product_index]

        quantity_choice = get_product_amount_input(selected_product)
        if not quantity_choice:
            break

        shopping_dict[selected_product] = shopping_dict.get(selected_product, 0) + quantity_choice

        print(f"{Fore.GREEN}Added {quantity_choice} of {selected_product.name} to your cart.")
        print()

    if shopping_dict:
        # Convert the dictionary back to a list of tuples for processing
        shopping_list = list(shopping_dict.items())
        try:
            total_price = my_store.order(shopping_list)
            print(f"\n{Fore.GREEN}********\nOrder successful!\n")
            display_shopping_list(shopping_list)
            print(f"\nTotal payment: ${total_price:.2f}")
        except Exception as e:
            print(f"{Fore.RED}An error occurred while processing your order: {e}")


def exit_program():
    """
    Exit program.
    :return: None
    """
    print(f"{Fore.GREEN}Exiting the program. Goodbye!")
    exit()