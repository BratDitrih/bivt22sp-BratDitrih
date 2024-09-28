from games.base_game import Game
import random


class ProgressionGame(Game):
    def generate_question(self):
        length = random.randint(5, 10)
        start = random.randint(1, 10)
        step = random.randint(2, 10)
        progression = [start * (step ** i) for i in range(length)]

        index_to_hide = random.randint(0, length - 1)
        answer = progression[index_to_hide]
        progression[index_to_hide] = ".."

        print("Question: " + " ".join(map(str, progression)))
        return answer

    def get_description(self):
        return "What number is missing in the progression?"
