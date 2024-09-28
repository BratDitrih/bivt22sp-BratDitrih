import random
from src.cli import welcome_user


def start_game():
    name = welcome_user()
    print("What number is missing in the progression?")

    for _ in range(3):
        correct_answer = generate_progression()
        user_answer = int(input("Your answer: "))
        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")


def generate_progression():
    length = random.randint(5, 10)
    start = random.randint(1, 10)
    step = random.randint(2, 10)
    progression = [start * (step ** i) for i in range(length)]

    index_to_hide = random.randint(0, length - 1)
    answer = progression[index_to_hide]
    progression[index_to_hide] = ".."

    print("Question: " + " ".join(map(str, progression)))
    return answer
