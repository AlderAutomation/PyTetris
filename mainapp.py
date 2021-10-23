import pygame
import introscreen
import levelselect 
import mainmenu
from pygame import color

pygame.init()


# Global Vars
win_x, win_y = 800, 600
win = pygame.display.set_mode((win_x, win_y))
bg = pygame.image.load("assets/pics/playfield.png")
bg = pygame.transform.scale(bg, (win_x, win_y))
pygame.display.set_caption("PyTetris")
run = True
clock = pygame.time.Clock()
game_mode = ""
music_select = ""
level_flag = ""

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
                    pygame.quit()

                intro_screen.update(event.key)

        if intro_screen.is_start == True:
            continue
        elif intro_screen.is_start == False:
            screen_switch_sound()
            break


def main_menu_loop():
    global game_mode, music_select
    main_Menu = mainmenu.main_menu(800,600)
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
                    pygame.quit()

                main_Menu.update(event.key)

        main_Menu.cursor_animation()

        if main_Menu.is_start == True:
            continue
        elif main_Menu.is_start == False:
            game_mode = main_Menu.game_cursor
            music_select = main_Menu.music_cursor
            screen_switch_sound()
            break


def level_select_loop():
    global level_flag

    level_select_win = levelselect.level_selecter(800, 600)
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
                    pygame.quit()

                level_select_win.update(event.key)

        level_select_win.cursor_animation()
        level_select_win.draw_levels()

        if level_select_win.is_start == True:
            continue
        elif level_select_win.is_start == False:
            level_flag = level_select_win.level_flag
            screen_switch_sound()
            break



def screen_switch_sound():
    switch_sound = pygame.mixer.Sound("assets/audio/effects/Switch_screen.wav")
    pygame.mixer.Sound.play(switch_sound)


def main():

    intro_screen_loop()
    
    main_menu_loop()
    print (game_mode)
    print (music_select)

    level_select_loop()
    print(level_flag)



if __name__ == "__main__":
    main()
    pygame.quit()

    