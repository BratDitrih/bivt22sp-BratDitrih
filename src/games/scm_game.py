from games.base_game import Game
import random
import math


class ScmGame(Game):
    def generate_question(self):
        numbers = random.sample(range(1, 20), 3)
        print(f"Question: {numbers[0]} {numbers[1]} {numbers[2]}")
        return self.calculate_lcm(numbers)

    def get_description(self):
        return "Find the smallest common multiple of given numbers."

    def calculate_lcm(self, numbers):
        lcm = numbers[0]
        for num in numbers[1:]:
            lcm = math.lcm(lcm, num)
        return lcm
