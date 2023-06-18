from pygame.math import Vector2
import pygame
CELL_SIZE = 40


class Snake:
    def __init__(self, screen):
        self.screen = screen
        self.body = [Vector2(6, 10), Vector2(5, 10), Vector2(4, 10)]
        self.direction = Vector2(1, 0)
        self.new_block = False
        self.del_block = False

        self.head_up = pygame.image.load('Graphics/head_up.png').convert_alpha()
        self.head_down = pygame.image.load('Graphics/head_down.png').convert_alpha()
        self.head_right = pygame.image.load('Graphics/head_right.png').convert_alpha()
        self.head_left = pygame.image.load('Graphics/head_left.png').convert_alpha()

        self.tail_up = pygame.image.load('Graphics/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load('Graphics/tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load('Graphics/tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load('Graphics/tail_left.png').convert_alpha()

        self.body_vertical = pygame.image.load('Graphics/body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load('Graphics/body_horizontal.png').convert_alpha()

        self.body_tr = pygame.image.load('Graphics/body_tr.png').convert_alpha()
        self.body_tl = pygame.image.load('Graphics/body_tl.png').convert_alpha()
        self.body_br = pygame.image.load('Graphics/body_br.png').convert_alpha()
        self.body_bl = pygame.image.load('Graphics/body_bl.png').convert_alpha()

        self.crunch_sound = pygame.mixer.Sound('Sounds/crunch.wav')
        self.oof_sound = pygame.mixer.Sound('Sounds/oof.wav')
        self.star_sound = pygame.mixer.Sound('Sounds/star.wav')
        self.game_over_sound = pygame.mixer.Sound('Sounds/game_over.wav')


    def draw_snake(self):
        self.update_head_graphics()
        self.update_tail_graphics()

        for i, block in enumerate(self.body):
            x_pos = block.x * CELL_SIZE
            y_pos = block.y * CELL_SIZE
            block_rect = pygame.Rect(x_pos, y_pos, CELL_SIZE, CELL_SIZE)

            if i == 0:
                self.screen.blit(self.head, block_rect)
            elif i == len(self.body) - 1:
                self.screen.blit(self.tail, block_rect)
            else:
                prev_block = self.body[i + 1] - block
                next_block = self.body[i - 1] - block
                if prev_block.x == next_block.x:
                    self.screen.blit(self.body_vertical, block_rect)
                elif prev_block.y == next_block.y:
                    self.screen.blit(self.body_horizontal, block_rect)
                else:
                    if prev_block.x == -1 and next_block.y == -1 or prev_block.y == -1 and next_block.x == -1:
                        self.screen.blit(self.body_tl, block_rect)
                    elif prev_block.x == -1 and next_block.y == 1 or prev_block.y == 1 and next_block.x == -1:
                        self.screen.blit(self.body_bl, block_rect)
                    elif prev_block.x == 1 and next_block.y == -1 or prev_block.y == -1 and next_block.x == 1:
                        self.screen.blit(self.body_tr, block_rect)
                    elif prev_block.x == 1 and next_block.y == 1 or prev_block.y == 1 and next_block.x == 1:
                        self.screen.blit(self.body_br, block_rect)

    def move_snake(self):
        if self.new_block:
            body_copy = self.body[:]
            self.new_block = False
        elif self.del_block:
            body_copy = self.body[:-2]
            self.del_block = False
        else:
            body_copy = self.body[:-1]
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy[:]

    def add_block(self):
        self.new_block = True

    def rem_block(self):
        self.del_block = True

    def update_head_graphics(self):
        head_direction = self.body[1] - self.body[0]
        if head_direction == Vector2(1, 0):
            self.head = self.head_left
        elif head_direction == Vector2(-1, 0):
            self.head = self.head_right
        elif head_direction == Vector2(0, 1):
            self.head = self.head_up
        elif head_direction == Vector2(0, -1):
            self.head = self.head_down

    def update_tail_graphics(self):
        tail_direction = self.body[-2] - self.body[-1]
        if tail_direction == Vector2(1, 0):
            self.tail = self.tail_left
        elif tail_direction == Vector2(-1, 0):
            self.tail = self.tail_right
        elif tail_direction == Vector2(0, 1):
            self.tail = self.tail_up
        elif tail_direction == Vector2(0, -1):
            self.tail = self.tail_down

    def play_crunch_sound(self):
        self.crunch_sound.play()

    def play_oof_sound(self):
        self.oof_sound.play()

    def play_star_sound(self):
        self.star_sound.play()

    def play_game_over_sound(self):
        self.game_over_sound.play()

    def reset(self):
        self.body = [Vector2(6, 10), Vector2(5, 10), Vector2(4, 10)]
        self.direction = Vector2(0, 0)
