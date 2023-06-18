from Item import Item
import pygame
CELL_SIZE = 40
CELL_NUMBER = 20


class Rock(Item):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.rock = pygame.image.load('Graphics/rock.png').convert_alpha()

    def draw_rock(self):
        rock_rect = pygame.Rect(self.pos.x * CELL_SIZE, self.pos.y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        self.screen.blit(self.rock, rock_rect)