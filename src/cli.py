from games.base_game import Game
from games.scm_game import ScmGame
from games.progression_game import ProgressionGame


def welcome_user():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    return name


def start_game(game: Game):
    name = welcome_user()
    print(game.get_description())

    for _ in range(3):
        correct_answer = game.generate_question()
        user_answer = int(input("Your answer: "))
        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")


def start_scm_game():
    start_game(ScmGame())


def start_progression_game():
    start_game(ProgressionGame())
