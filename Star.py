from Item import Item
from pygame.math import Vector2
import pygame
CELL_SIZE = 40
CELL_NUMBER = 20


class Star(Item):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.star = pygame.image.load('Graphics/star.png').convert_alpha()

    def draw_star(self):
        star_rect = pygame.Rect(self.pos.x * CELL_SIZE, self.pos.y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        self.screen.blit(self.star, star_rect)

    def remove_star(self):
        self.x = CELL_NUMBER
        self.y = CELL_NUMBER
        self.pos = Vector2(self.x, self.y)
