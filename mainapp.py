import pygame
import random

from pygame import color

pygame.init()

win_x = 800
win_y = 600

win = pygame.display.set_mode((win_x, win_y))
bg = pygame.image.load("assets/forrest.png")
bg = pygame.transform.scale(bg, (win_x, win_y))
pygame.display.set_caption("PyTetris")
run = True
clock = pygame.time.Clock()



class piece():
    def __init__(self) -> None:
        self.x = 125
        self.y = 50
        self.vel = 5



    

def redraw_win():
    win.blit(bg, (0,0))
    pygame.display.update()


def draw_play_area():
    play_x = 275
    play_y = 50
    play_width = 250
    play_hieght = 500
    pygame.draw.rect(win, (0,0,0), (play_x, play_y, play_width, play_hieght))


while run:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    redraw_win()
    draw_play_area()
    pygame.display.update()


pygame.quit()