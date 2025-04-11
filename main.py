import products
import store


def main():
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250),
                    ]

    best_buy = store.Store(product_list)
    all_products = best_buy.get_all_products()
    print(best_buy.get_total_quantity())
    print(best_buy.order([(all_products[0], 100), (all_products[1], 2)]))
    print(best_buy.get_all_products())


if __name__ == "__main__":
    main()