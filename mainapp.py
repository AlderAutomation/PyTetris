import pygame
import random
import tetrimos

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
    def __init__(self, shape) -> None:
        self.vel = 1
        self.shape = shape
        self.x = 375
        self.y = 50

    def draw_piece(self):
        if self.shape == "o":
            tetrimos.ooh(self, win)
        elif self.shape == "t":
            tetrimos.tee(self, win)
        elif self.shape == "i":
            tetrimos.eye(self, win)
        else:
            print("noob")
    

def redraw_win():
    win.blit(bg, (0,0))
    draw_play_area()
    active_piece.draw_piece()
    pygame.display.update()


def draw_play_area():
    play_x = 275
    play_y = 50
    play_width = 250
    play_hieght = 500
    pygame.draw.rect(win, (0,0,0), (play_x, play_y, play_width, play_hieght))

shape = "i"
active_piece = piece(shape)


while run:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        if not active_piece.x <= 305:
            active_piece.x -= active_piece.vel
    elif keys[pygame.K_d]:
        if not active_piece.x >= 440:
            active_piece.x += active_piece.vel

    if active_piece.y <= 520:
        active_piece.y += active_piece.vel
    redraw_win()

pygame.quit()