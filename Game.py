from Fruit import Fruit
from Rock import Rock
from Star import Star
from Snake import Snake
from pygame.math import Vector2
import pygame
CELL_SIZE = 40
CELL_NUMBER = 20


class Game:
    def __init__(self, screen):
        self.snake = Snake(screen)
        self.fruit = Fruit(screen)
        self.rock = Rock(screen)
        self.star = Star(screen)
        self.screen = screen

        self.star_on = False
        self.last_star = pygame.time.get_ticks()
        self.star_cooldown = 12800

        self.last_rock = pygame.time.get_ticks()
        self.rock_cooldown = 6400

        self.game_font = pygame.font.Font('Fonts/SMASH.ttf', 25)

    def update(self):
        self.snake.move_snake()
        self.check_fail()
        self.check_collision()

    def draw_elements(self):
        now = pygame.time.get_ticks()
        self.draw_grass()
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()
        self.rock.draw_rock()
        if self.star_on:
            self.star.draw_star()

        if now - self.last_rock >= self.rock_cooldown:
            self.rock_cooldown -= 100
            self.last_rock = now
            self.rock.randomize()

        if now - self.last_star >= self.star_cooldown:
            if not self.star_on:
                self.star_on = True
            else:
                self.star_cooldown += 5000
                self.last_star = now
                self.star.randomize()

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.snake.play_crunch_sound()
            self.fruit.randomize()
            self.snake.add_block()

        if self.rock.pos == self.snake.body[0]:
            self.snake.play_oof_sound()
            if len(self.snake.body) < 3:
                self.game_over()
            else:
                self.rock.randomize()
                self.snake.rem_block()

        if self.star_on:
            if self.star.pos == self.snake.body[0]:
                self.snake.play_star_sound()
                self.star.remove_star()
                self.rock_cooldown += 200
                self.snake.add_block()

        for block in self.snake.body[1:]:
            if block == self.fruit.pos:
                self.fruit.randomize()
            if block == self.rock.pos:
                self.rock.randomize()
            if self.star_on:
                if block == self.star.pos:
                    self.star.randomize()

    def check_fail(self):
        if not 0 <= self.snake.body[0].x < CELL_NUMBER or not 0 <= self.snake.body[0].y < CELL_NUMBER:
            self.game_over()

        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        if not self.snake.body[0] == Vector2(6, 10):
            self.snake.play_game_over_sound()
            with open('leaderboard.txt', 'a') as file:
                file.write(';' + str(len(self.snake.body) - 3))

        self.last_star = pygame.time.get_ticks()
        self.star_cooldown = 12800
        self.last_rock = pygame.time.get_ticks()
        self.rock_cooldown = 6400

        self.snake.reset()

    def draw_grass(self):
        grass_color = (167, 209, 61)

        for row in range(CELL_NUMBER):
            if row % 2 == 0:
                for col in range(CELL_NUMBER):
                    if col % 2 == 0:
                        grass_rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                        pygame.draw.rect(self.screen, grass_color, grass_rect)
            else:
                for col in range(CELL_NUMBER):
                    if col % 2 != 0:
                        grass_rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                        pygame.draw.rect(self.screen, grass_color, grass_rect)

    def draw_score(self):
        score_text = str(len(self.snake.body) - 3)
        score_surface = self.game_font.render(score_text, True, (56, 72, 12))
        score_x = int(CELL_SIZE * CELL_NUMBER - 60)
        score_y = int(CELL_SIZE * CELL_NUMBER - 40)
        score_rect = score_surface.get_rect(center=(score_x, score_y))
        apple_rect = self.fruit.apple.get_rect(midright=(score_rect.left - 5, score_rect.centery - 5))

        self.screen.blit(score_surface, score_rect)
        self.screen.blit(self.fruit.apple, apple_rect)
