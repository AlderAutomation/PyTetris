import pygame
import random
import introscreen

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


def music(song):
    pygame.mixer.init()
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(-1)


def main():
    music("assets/audio/music1.wav")
    intro_screen = introscreen.intro_menu(win_x, win_y)
    intro_screen.draw_intro()

    run = True

    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()

        # if keys[pygame.K_a]:
        #     if not active_piece.x <= 305:
        #         active_piece.x -= active_piece.vel
        # elif keys[pygame.K_d]:
        #     if not active_piece.x >= 440:
        #         active_piece.x += active_piece.vel

        if keys[pygame.K_RETURN] and intro_screen.is_start == True:
            intro_screen.is_start = False

        intro_screen.switch_win()

        # if active_piece.y <= 520:
        #     active_piece.y += active_piece.vel


    pygame.quit()



if __name__ == "__main__":
    main()