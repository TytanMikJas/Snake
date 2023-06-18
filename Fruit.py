from Item import Item
import pygame
CELL_SIZE = 40


class Fruit(Item):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.apple = pygame.image.load('Graphics/apple.png').convert_alpha()

    def draw_fruit(self):
        fruit_rect = pygame.Rect(self.pos.x * CELL_SIZE, self.pos.y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        self.screen.blit(self.apple, fruit_rect)