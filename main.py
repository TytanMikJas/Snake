import sys
import pygame
import pygame_gui
from Game import Game
from button import Button
from datetime import datetime
from pygame.math import Vector2


def easy_play(reset, body):
    if reset:
        main_game.snake.reset()
    change = True
    easy_music = pygame.mixer.Sound('Sounds/easy_music.mp3')
    easy_music.play()
    main_game.snake.body = body
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == SCREEN_UPDATE:
                main_game.update()
                change = True
            if event.type == pygame.KEYDOWN:
                if change:
                    if event.key == pygame.K_w:
                        if main_game.snake.direction.y != 1:
                            main_game.snake.direction = Vector2(0, -1)
                    if event.key == pygame.K_s:
                        if main_game.snake.direction.y != -1:
                            main_game.snake.direction = Vector2(0, 1)
                    if event.key == pygame.K_a:
                        if main_game.snake.direction.x != 1:
                            main_game.snake.direction = Vector2(-1, 0)
                    if event.key == pygame.K_d:
                        if main_game.snake.direction.x != -1:
                            main_game.snake.direction = Vector2(1, 0)
                    if event.key == pygame.K_ESCAPE:
                        easy_music.stop()
                        main_menu()
                    if event.key == pygame.K_p:
                        easy_music.stop()
                        pause(main_game.snake.body)
                change = False

        screen.fill((175, 215, 70))
        main_game.draw_elements()
        pygame.display.update()
        clock.tick(120)


def leader_board():
    menu_font = pygame.font.Font('Fonts/SMASH.ttf', 50)
    buttons_font = pygame.font.Font('Fonts/SMASH.ttf', 30)

    leaders = count_leaders()

    while True:
        screen.blit(pygame.image.load("Graphics/menu_background.jpg").convert_alpha(), (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = menu_font.render("LEADERBOARD", True, "#08542b")
        MENU_RECT = MENU_TEXT.get_rect(center=(400, 100))

        BACK_BUTTON = Button(image=pygame.image.load("Graphics/Play Rect.png"), pos=(400, 700),
                             text_input="Back", font=buttons_font, base_color="#d7fcd4", hovering_color="White")

        screen.blit(MENU_TEXT, MENU_RECT)

        # Display 5 players from the leaders variable
        player_font = pygame.font.Font('Fonts/SMASH.ttf', 45)
        y_offset = 200
        for i, player in enumerate(leaders[:5]):
            player_text = player_font.render(f"{i + 1}. {player[0]}  -   {player[1]}", True, "#000000")
            player_rect = player_text.get_rect(center=(400, y_offset))
            screen.blit(player_text, player_rect)
            y_offset += 100

        BACK_BUTTON.change_color(MENU_MOUSE_POS)
        BACK_BUTTON.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK_BUTTON.check_for_input(MENU_MOUSE_POS):
                    main_menu(False)

        pygame.display.update()


def pre_play():
    menu_font = pygame.font.Font('Fonts/SMASH.ttf', 75)
    MENU_TEXT = menu_font.render("Input username:", True, "#08542b")
    MENU_RECT = MENU_TEXT.get_rect(center=(400, 100))

    while True:
        screen.blit(pygame.image.load("Graphics/menu_background.jpg").convert_alpha(), (0, 0))
        screen.blit(MENU_TEXT, MENU_RECT)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
                with open('leaderboard.txt', 'a') as file:
                    file.write('\n' + str(datetime.now().strftime("%d/%m/%Y %H:%M:%S")) + ";" + event.text)
                menu_sound.stop()
                easy_play(True, [Vector2(6, 10), Vector2(5, 10), Vector2(4, 10)])

            MANAGER.process_events(event)

        MANAGER.update(clock.tick(60) / 1000)

        MANAGER.draw_ui(screen)

        pygame.display.update()


def main_menu(play_sound=True):
    menu_font = pygame.font.Font('Fonts/SMASH.ttf', 75)
    buttons_font = pygame.font.Font('Fonts/SMASH.ttf', 50)
    if play_sound:
        menu_sound.play()

    while True:
        screen.blit(pygame.image.load("Graphics/menu_background.jpg").convert_alpha(), (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = menu_font.render("MAIN MENU", True, "#08542b")
        MENU_RECT = MENU_TEXT.get_rect(center=(400, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("Graphics/Play Rect.png"), pos=(400, 275),
                             text_input="PLAY", font=buttons_font, base_color="#d7fcd4", hovering_color="White")
        LEADERBOARD_BUTTON = Button(image=pygame.image.load("Graphics/Options Rect.png"), pos=(400, 450),
                                    text_input="LEADERBOARD", font=buttons_font, base_color="#d7fcd4",
                                    hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("Graphics/Quit Rect.png"), pos=(400, 625),
                             text_input="QUIT", font=buttons_font, base_color="#d7fcd4", hovering_color="White")

        screen.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, LEADERBOARD_BUTTON, QUIT_BUTTON]:
            button.change_color(MENU_MOUSE_POS)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.check_for_input(MENU_MOUSE_POS):
                    pre_play()
                if LEADERBOARD_BUTTON.check_for_input(MENU_MOUSE_POS):
                    leader_board()
                if QUIT_BUTTON.check_for_input(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


def pause(body):
    menu_font = pygame.font.Font('Fonts/SMASH.ttf', 25)
    MENU_TEXT = menu_font.render("PAUSE, press any key to resume", True, "#08542b")
    MENU_RECT = MENU_TEXT.get_rect(center=(400, 100))

    while True:
        screen.blit(MENU_TEXT, MENU_RECT)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                easy_play(False, body)

        MANAGER.update(clock.tick(60) / 1000)

        pygame.display.update()


def count_leaders():
    with open('leaderboard.txt', 'r') as file:
        lines = file.readlines()

    leaderboard = {}
    for line in lines[1:]:
        values = line.strip().split(';')
        if len(values) < 3:
            continue
        nick = values[1]
        score = int(values[2])
        if nick in leaderboard:
            if score > leaderboard[nick]:
                leaderboard[nick] = score
        else:
            leaderboard[nick] = score

    sorted_leaderboard = sorted(leaderboard.items(), key=lambda x: x[1], reverse=True)

    top_5 = [[nick, score] for nick, score in sorted_leaderboard[:5]]
    return top_5


if __name__ == '__main__':
    CELL_SIZE = 40
    CELL_NUMBER = 20
    pygame.init()
    screen = pygame.display.set_mode((CELL_NUMBER * CELL_SIZE, CELL_NUMBER * CELL_SIZE))
    clock = pygame.time.Clock()
    SCREEN_UPDATE = pygame.USEREVENT
    pygame.time.set_timer(SCREEN_UPDATE, 150)
    main_game = Game(screen)
    input_font = pygame.font.Font('Fonts/SMASH.ttf', 40)

    MANAGER = pygame_gui.UIManager((800, 800))
    test_rect = pygame.Rect((200, 200), (400, 50))
    text_input = pygame_gui.elements.UITextEntryLine(relative_rect=test_rect, manager=MANAGER)

    menu_sound = pygame.mixer.Sound('Sounds/menu_music.mp3')

    main_menu()
