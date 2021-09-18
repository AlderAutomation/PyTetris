import pygame
import random

from pygame import color

pygame.init()

win_x = 800
win_y = 600

win = pygame.display.set_mode((win_x, win_y))
pygame.display.set_caption("PyTetris")
run = True
clock = pygame.time.Clock()
    

def redraw_win():
    win.fill((0,0,0))
    pygame.display.update()


play_x = 300
play_y = 100
play_width = 200
play_hieght = 400
play_area = pygame.draw.rect(win, (255,0,0), (play_x, play_y, play_width, play_hieght))



while run:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.draw.rect(win, (255,0,0), (play_x, play_y, play_width, play_hieght))
    redraw_win()

pygame.quit()