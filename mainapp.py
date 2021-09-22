import pygame
import random

from pygame import color

pygame.init()


# Global Vars
win_x = 800
win_y = 600
win = pygame.display.set_mode((win_x, win_y))
bg = pygame.image.load("assets/forrest.png")
bg = pygame.transform.scale(bg, (win_x, win_y))
pygame.display.set_caption("PyTetris")
run = True
clock = pygame.time.Clock()

# Shapes
Z = [['.....',
      '.00..',
      '..00.'],
     ['...0.',
      '..00.',
      '..0..']]

I = [['.....'], 
     ['.0000'], 
     ['.....']]


class piece():
    def __init__(self, shape_input) -> None:
        self.vel = 1
        self.shape = shape_input
        self.x = 375
        self.y = 50
        self.rotation = 0

    def draw_piece(self):
        if self.shape == "z":
            self.shape = Z
        else:
            pass

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

shapes_list = [Z, I]

shape_input = "z"
active_piece = piece(shape_input)

for i in active_piece.shape:
    for j in i:
        print (j)


def music():
    pygame.mixer.init()
    pygame.mixer.music.load("assets/music1.mp3")
    pygame.mixer.music.play()
    # pygame.error: Unrecognized audio format


# music()
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