import pygame
import introscreen
import levelselect 
import mainmenu
from pygame import color

pygame.init()


win_x, win_y = 800, 600
pygame.display.set_caption("PyTetris")
run = True
clock = pygame.time.Clock()
# set in main loop only
GAME_MODE = ""
MUSIC_FLAG = ""
# set in level select loop only
LEVEL_FLAG = ""


def screen_switch_sound():
    switch_sound = pygame.mixer.Sound("assets/audio/effects/Switch_screen.wav")
    pygame.mixer.Sound.play(switch_sound)


def intro_screen_loop():
    intro_screen = introscreen.intro_menu(win_x, win_y)
    intro_screen.draw_intro()

    intro_loop_run = True

    while intro_loop_run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                intro_loop_run = False

            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_ESCAPE:
                    print("ESC was pressed. Quitting....")
                    intro_loop_run = False

                intro_screen.update(event.key)

        if intro_screen.is_start == True:
            continue
        elif intro_screen.is_start == False:
            screen_switch_sound()
            break


def main_menu_loop():
    global GAME_MODE, MUSIC_FLAG
    main_Menu = mainmenu.main_menu(win_x, win_y)
    main_Menu.draw_main()
    main_Menu.draw_game_cursor(195, 148)
    main_Menu.draw_music_cursor(320, 360)
    main_Menu.music()

    main_menu_loop = True

    while main_menu_loop:
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                main_menu_loop = False

            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_ESCAPE:
                    print("ESC was pressed. Quitting....")
                    main_menu_loop = False

                main_Menu.update(event.key)

        main_Menu.cursor_animation()

        if main_Menu.is_start == True:
            continue
        elif main_Menu.is_start == False:
            GAME_MODE = main_Menu.game_cursor
            MUSIC_FLAG = main_Menu.music_cursor
            screen_switch_sound()
            break


def level_select_loop():
    global LEVEL_FLAG

    level_select_win = levelselect.level_selecter(win_x, win_y)
    level_select_win.draw_main()
    level_select_win.draw_level_cursor(168, 205)
    level_select_win.draw_levels()

    level_select_loop = True

    while level_select_loop:
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                level_select_loop = False

            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_ESCAPE:
                    print("ESC was pressed. Quitting....")
                    level_select_loop = False

                level_select_win.update(event.key)

        level_select_win.cursor_animation()
        level_select_win.draw_levels()

        if level_select_win.is_start == True:
            continue
        elif level_select_win.is_start == False:
            LEVEL_FLAG = level_select_win.level_flag
            screen_switch_sound()
            break


def main():

    intro_screen_loop()
    
    main_menu_loop()

    level_select_loop()



if __name__ == "__main__":
    main()
    pygame.quit()

    