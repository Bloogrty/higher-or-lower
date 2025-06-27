from art import logo, vs
from game_data import data
import random


def format_data(product):
    product_name = product["name"]
    product_description = product["description"]
    product_brand = product["brand"]
    return f"{product_name}, a {product_description} from {product_brand}"


def check_answer(user_guess, a_price, b_price):
    if a_price > b_price:
        return user_guess == "a"
    else:
        return user_guess == "b"


def game():
    print(logo)
    score = 0

    # generate random product
    product_b = random.choice(data)

    while True:
        # product into position
        product_a = product_b
        product_b = random.choice(data)

        if product_a == product_b:
            product_b = random.choice(data)

        print(f"Product A: {format_data(product_a)}")
        print(vs)
        print(f"Product B: {format_data(product_b)}")

        # User guess
        guess = input("Which one burns more cash? Type 'A' or 'B': ").lower()

        # clear screen
        print("\n" * 20)
        print(logo)

        # get price
        a_price_count = product_a["price"]
        b_price_count = product_b["price"]

        # check is correct
        is_correct = check_answer(guess, a_price_count, b_price_count)

        if is_correct:
            score += 1
            print(
                f"Correct, my tech-savvy Sultan! Current score: {score}. Keep flexing!"
            )
        else:
            print(
                f"Wrong guess! Final score: {score}. No more caviar tech dreams for you."
            )
            return False


game()
