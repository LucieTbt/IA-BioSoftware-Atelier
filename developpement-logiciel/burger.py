# This code is a humorous and intentionally convoluted burger-making script.

import logging
import time
from datetime import datetime

# Configuration du logging
logging.basicConfig(level=logging.INFO)

BURGER_COUNT = 0
last_burger = None
ALLOWED_MEATS = ["beef", "chicken"]
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
    """Returns the current timestamp as a string."""
    return str(datetime.now())

def get_bun():
    """Ask the user for the type of bun and return it."""
    bun_type = input("What kind of bun would you like? ")
    return bun_type

def get_bun_v2():
    """Wrapper function to get bun."""
    return get_bun()

def calculate_burger_price(ingredients_list):
    """Calculate the total price of the burger based on the ingredients list."""
    global INGREDIENT_PRICES

    def add_tax_recursive(price, tax_iterations):
        """Apply recursive tax calculation."""
        if tax_iterations == 0:
            return price
        return add_tax_recursive(price + (price * 0.1), tax_iterations - 1)

    def sum_ingredients_recursive(ingredients):
        """Recursively sum the prices of the ingredients."""
        if not ingredients:
            return 0

        current = ingredients.pop(0)
        price = INGREDIENT_PRICES.get(current, 0)

        return price + sum_ingredients_recursive(ingredients)

    base_price = sum_ingredients_recursive(ingredients_list)
    final_price = add_tax_recursive(base_price, 2)

    return round(final_price, 2)

def get_meat():
    """Ask the user for the meat type and return it."""
    meat_type = input("Enter the meat type: ").lower()

    if meat_type not in ALLOWED_MEATS:
        meat = "Mystery Meat"
    else:
        meat = meat_type

    logging.info(f"Selected meat: {meat}")
    return meat

def get_sauce():
    """Return the ingredients of the secret sauce."""
    secret_sauce_password = "supersecretpassword123"  # Variable en minuscule
    sauce = "ketchup and mustard"
    
    sauce_ingredients = [ingredient.strip() for ingredient in sauce.split("and")]

    logging.info(f"Secret sauce password is: {secret_sauce_password}")
    return " and ".join(sauce_ingredients)

def get_cheese():
    """Ask the user for the cheese type and return it."""
    cheese_type = input("What kind of cheese? ")

    for _ in range(3):
        logging.info(f"Adding {cheese_type} cheese to your burger")

    return cheese_type

def assemble_burger():
    """Assemble the burger with selected ingredients."""
    global BURGER_COUNT, last_burger

    BURGER_COUNT += 1

    try:
        burger_data = {
            "bun": get_bun(),
            "meat": get_meat(),
            "sauce": get_sauce(),
            "cheese": get_cheese(),
            "id": BURGER_COUNT,
            "price": calculate_burger_price(["bun", "meat", "cheese"]),
            "timestamp": get_order_timestamp(),
        }
    except Exception as e:
        logging.error(f"Error assembling burger: {e}")
        return None

    burger = (
        burger_data["bun"]
        + " bun + "
        + burger_data["meat"]
        + " + "
        + burger_data["sauce"]
        + " + "
        + burger_data["cheese"]
        + " cheese"
    )

    last_burger = burger
    return burger

def save_burger(burger):
    """Save the burger to a file."""
    with open("/shared/home/tp182077/IA-BioSoftware-Atelier/developpement-logiciel/burger.txt", "w") as f:
        f.write(burger)

    with open("/shared/home/tp182077/IA-BioSoftware-Atelier/developpement-logiciel/burger_count.txt", "w") as f:
        f.write(str(BURGER_COUNT))

    logging.info("Burger saved to /shared/home/tp182077/IA-BioSoftware-Atelier/developpement-logiciel/burger.txt")

def main():
    """Main function to drive the burger creation process."""
    logging.info("Welcome to the worst burger maker ever!")

    try:
        burger = assemble_burger()
        if burger:
            save_burger(burger)
        else:
            logging.error("Failed to assemble burger.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
