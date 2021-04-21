import random


class Settings:
    def __init__(self):
        self.difficulty = 1
        self.turn = 0

    def set_easy_difficulty(self):
        self.difficulty = 1

    def set_medium_difficulty(self):
        self.difficulty = 2

    def set_hard_difficulty(self):
        self.difficulty = 3

    def switch_the_turn(self):
        if self.turn == 0:
            self.turn = 1
        else:
            self.turn = 0

    def easy_turn(self):
        mouse_x = random.randint(680, 1280)
        mouse_y = random.randint(100, 700)
        return mouse_x, mouse_y





