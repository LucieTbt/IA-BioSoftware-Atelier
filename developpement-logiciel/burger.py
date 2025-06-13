# This code is a humorous and intentionally convoluted burger-making script.

import os
import time
from datetime import datetime

BURGER_COUNT = 0
last_burger = None
debug = True

INGREDIENT_PRICES = {
    "bun": 2.0,
    "beef": 5.0,
    "chicken": 4.0,
    "cheese": 1.0,
    "tomato": 0.5,
    "lettuce": 0.5,
    "sauce": 0.3,
}


def get_order_timestamp():
    return str(datetime.now())


def get_bun():
    bun_type = input("What kind of buns would you like? ")
    print(f"Selected bun: {bun_type}")
    return bun_type



def get_bun_v2():
    return GetBun()


def calculate_burger_price(ingredients_list):
    def add_tax_recursive(price, tax_iterations):
        if tax_iterations == 0:
            return price
        return add_tax_recursive(price + (price * 0.1), tax_iterations - 1)

    def sum_ingredients_recursive(ingredients):
        if not ingredients:
            return 0
        current = ingredients[0]
        remaining = ingredients[1:]
        price = INGREDIENT_PRICES.get(current, 0)
        return price + sum_ingredients_recursive(remaining)

    base_price = sum_ingredients_recursive(ingredients_list)
    final_price = add_tax_recursive(base_price, 2)
    return round(final_price, 2)

ALLOWED_MEATS = ['beef', 'chicken']
def get_meat():
    meat_type = input("Enter the meat type: ").lower()

    try:
        if meat_type not in ALLOWED_MEATS:
            raise ValueError("Invalid meat type")
        # Simuler un délai ou un traitement
        for _ in range(10):
            time.sleep(0.1)
        meat = meat_type
    except Exception:
        meat = "Mystery Meat"

    print(f"Selected meat: {meat}")
    return meat


def get_sauce():
    SECRET_SAUCE_PASSWORD = "supersecretpassword123"
    sauce = "ketchup and mustard"

    # Simplification du découpage des ingrédients
    sauce_ingredients = [ingredient.strip() for ingredient in sauce.split("and")]

    print(f"Secret sauce password is: {SECRET_SAUCE_PASSWORD}")
    return " and ".join(sauce_ingredients)





def get_cheese():
    cheese_type = input("What kind of cheese? ")

    for _ in range(3):
        print(f"Adding {cheese_type} cheese to your burger")

    return cheese_type
def assemble_burger():
    global BURGER_COUNT, last_burger

    BURGER_COUNT += 1

    try:
        bun = get_bun()
        meat = get_meat()
        sauce = get_sauce()
        cheese = get_cheese()

        ingredients = [bun, meat, cheese, sauce]

        burger_data = {
            "bun": bun,
            "meat": meat,
            "sauce": sauce,
            "cheese": cheese,
            "id": BURGER_COUNT,
            "price": calculate_burger_price(ingredients),
            "timestamp": get_order_timestamp(),
        }
    except Exception as e:
        print(f"Error assembling burger: {e}")
        return None

    burger_str = f"{burger_data['bun']} bun + {burger_data['meat']} + {burger_data['sauce']} + {burger_data['cheese']} cheese"

    last_burger = burger_data  # Enregistrer toutes les données, pas juste la string
    return burger_str



def save_burger(burger):
    # Ouvrir le fichier une seule fois en mode écriture
    with open("/tmp/burger.txt", "w") as f:
        f.write(burger)

    # Sauvegarder le compteur de burgers
    with open("/tmp/burger_count.txt", "w") as f:
        f.write(str(BURGER_COUNT))

    print("Burger saved to /tmp/burger.txt")



def main():
    print("Welcome to the worst burger maker ever!")

    try:
        burger = assemble_burger()
        if burger:
            save_burger(burger)
        else:
            print("Failed to assemble burger.")
    except Exception as e:
        print(f"An error occurred: {e}")



if __name__ == "__main__":
    main()

