from abc import ABC, abstractmethod


class Game(ABC):
    @abstractmethod
    def generate_question(self):
        pass

    @abstractmethod
    def get_description(self):
        pass
