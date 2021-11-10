import pygame
import introscreen
import levelselect 
import mainmenu
import game
from pygame import color

pygame.init()

win_x, win_y = 768, 672
pygame.display.set_caption("PyTetris")
clock = pygame.time.Clock()
# set in main loop only
GAME_MODE = ""
MUSIC_FLAG = ""
# set in level select loop only
LEVEL_FLAG = ""


def screen_switch_sound():
    pygame.mixer.init()
    switch_sound = pygame.mixer.Sound("assets/audio/effects/Switch_screen.wav")
    pygame.mixer.Sound.play(switch_sound)


def speed_selector(level: int) -> float:
    if LEVEL_FLAG == 0:
        speed = .80
    elif LEVEL_FLAG == 1:
        speed = .70
    elif LEVEL_FLAG == 2:
        speed = .60
    elif LEVEL_FLAG == 3:
        speed = .50
    elif LEVEL_FLAG == 4:
        speed = .40
    elif LEVEL_FLAG == 5:
        speed = .30
    elif LEVEL_FLAG == 6:
        speed = .20
    elif LEVEL_FLAG == 7:
        speed = .10
    elif LEVEL_FLAG == 8:
        speed = .09
    elif LEVEL_FLAG == 9:
        speed = .08

    return speed


def intro_screen_loop() -> None:
    intro_screen = introscreen.intro_menu(win_x, win_y)
    intro_screen.draw_intro()

    intro_loop_run = True

    while intro_loop_run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_ESCAPE:
                    print("ESC was pressed. Quitting....")
                    pygame.quit()

                intro_screen.update(event.key)

        if intro_screen.is_start == True:
            continue
        elif intro_screen.is_start == False:
            screen_switch_sound()
            break


def main_menu_loop() -> None:
    global GAME_MODE, MUSIC_FLAG
    main_Menu = mainmenu.main_menu(win_x, win_y)
    main_Menu.draw_main()
    main_Menu.draw_game_cursor(190, 165)
    main_Menu.draw_music_cursor(305, 405)
    main_Menu.music()

    main_menu_loop = True

    while main_menu_loop:
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_ESCAPE:
                    print("ESC was pressed. Quitting....")
                    pygame.quit()

                main_Menu.update(event.key)
    
        if main_Menu.is_start == True:
            main_Menu.cursor_animation()
            continue
        elif main_Menu.is_start == False:
            GAME_MODE = main_Menu.game_cursor
            MUSIC_FLAG = main_Menu.music_cursor
            screen_switch_sound()
            break


def level_select_loop() -> None:
    global LEVEL_FLAG

    level_select_win = levelselect.level_selecter(win_x, win_y)
    level_select_win.draw_main()
    level_select_win.draw_level_cursor(160, 230)
    level_select_win.draw_levels()

    level_select_loop = True

    while level_select_loop:
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_ESCAPE:
                    print("ESC was pressed. Quitting....")
                    pygame.quit()

                level_select_win.update(event.key)


        if level_select_win.is_start == True:
            level_select_win.cursor_animation()
            level_select_win.draw_levels()
            continue
        elif level_select_win.is_start == False:
            LEVEL_FLAG = level_select_win.level_flag
            screen_switch_sound()
            break


def  game_screen_loop() -> None:
    global LEVEL_FLAG

    game_win = game.game(win_x, win_y, LEVEL_FLAG)
    game_win.draw_win()
    game_win.load_hi_scores()
    game_win.count_piece()
    game_win.fall_speed = speed_selector(LEVEL_FLAG)

    game_running = True
    fall_time = 0

    while game_running:
        fall_time += clock.get_rawtime()
        clock.tick()

        while game_win.pause == True:
            pause_bg = pygame.image.load("assets/pics/pause_screen.png")
            pause_bg = pygame.transform.scale(pause_bg, (game_win.game_x, game_win.game_y))
            pause_win = pygame.display.set_mode((game_win.game_x, game_win.game_y))
            pause_win.blit(pause_bg, (0,0))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_running = False

                if event.type == pygame.KEYDOWN :
                    if event.key == pygame.K_RETURN:
                        game_win.pause = False

        if fall_time/1000 > game_win.fall_speed:
            fall_time = 0
            game_win.current_piece.y += 25
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_ESCAPE:
                    print("ESC was pressed. Quitting....")
                    pygame.quit()

            game_win.screen_input(event)

        if game_win.current_piece.y > 60:
            game_win.draw_current_piece()

        if game_win.current_piece.y >= 551:
            game_win.current_piece = game_win.swap_next_with_current_piece()
            game_win.count_piece()
        
        pygame.display.update()
        game_win.draw_win()


def main():

    intro_screen_loop()
    
    main_menu_loop()

    level_select_loop()

    game_screen_loop()



if __name__ == "__main__":
    main()
    pygame.quit()

    