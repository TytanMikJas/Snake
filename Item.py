from pygame.math import Vector2
import random
CELL_NUMBER = 20


class Item:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.pos = Vector2(self.x, self.y)
        self.randomize()

    def randomize(self):
        self.x = random.randint(0, CELL_NUMBER - 1)
        self.y = random.randint(0, CELL_NUMBER - 1)
        self.pos = Vector2(self.x, self.y)