import random
import math
from src.cli import welcome_user


def start_game():
    name = welcome_user()
    print("Find the smallest common multiple of given numbers.")

    for _ in range(3):
        correct_answer = generate_numbers()
        user_answer = int(input("Your answer: "))
        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")


def generate_numbers():
    numbers = random.sample(range(1, 20), 3)
    print(f"Question: {numbers[0]} {numbers[1]} {numbers[2]}")
    return calculate_lcm(numbers)


def calculate_lcm(numbers):
    lcm = numbers[0]
    for num in numbers[1:]:
        lcm = math.lcm(lcm, num)
    return lcm
