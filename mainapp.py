import pygame
import random
import introscreen
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



def redraw_win():
    win.blit(bg, (0,0))
    draw_play_area()
    # draw_piece()
    pygame.display.update()


def draw_play_area():
    play_x = 275
    play_y = 50
    play_width = 250
    play_hieght = 500
    pygame.draw.rect(win, (0,0,0), (play_x, play_y, play_width, play_hieght))


def convert_shape(shape):
    positions = []
    formatt = shape.shape[shape.rotation % len(shape.shape)]

    for i, line in enumerate(formatt):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                positions.append((j * 26, i * 26))

    return positions




def main():
    # Intro Screen Loop
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
            break



    # Main menu Loop
    main_Menu = mainmenu.main_menu(800,600)
    main_Menu.draw_main()
    main_Menu.draw_game_cursor(195, 148)
    main_Menu.draw_music_cursor(320, 360)
    main_Menu.music()

    main_menu_loop = True

    while main_menu_loop:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                main_menu_loop = False

            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_ESCAPE:
                    print("ESC was pressed. Quitting....")
                    pygame.quit()

                main_Menu.update(event.key)

        if main_Menu.is_start == True:
            continue
        elif main_Menu.is_start == False:
            game_mode = main_Menu.game_cursor
            music_select = main_Menu.music_cursor
            break

    pygame.quit()
    print (game_mode)
    print (music_select)




if __name__ == "__main__":
    main()