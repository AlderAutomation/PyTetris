import pygame
import random

from pygame import color

pygame.init()


# Global Vars
win_x = 800
win_y = 600
win = pygame.display.set_mode((win_x, win_y))
intro_win = pygame.display.set_mode((win_x, win_y))
intro_bg = pygame.image.load("assets/pics/press_start.png")
intro_bg = pygame.transform.scale(intro_bg, (win_x, win_y))
bg = pygame.image.load("assets/pics/forrest.png")
bg = pygame.transform.scale(bg, (win_x, win_y))
pygame.display.set_caption("PyTetris")
run = True
clock = pygame.time.Clock()
is_start = False

# Shapes
Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]

I = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]

class piece():
    def __init__(self, shape_input) -> None:
        self.vel = 1
        self.shape = shape_input
        self.x = 375
        self.y = 50
        self.rotation = 0

        if self.shape == Z:
            self.block = pygame.image.load("assets/pics/z_l_block.png")
        elif self.shape == I:
            self.block = pygame.image.load("assets/pics/t_i_block.png")
        else:
            pass


def redraw_win():
    win.blit(bg, (0,0))
    draw_play_area()
    draw_piece()
    pygame.display.update()


def draw_intro():
    intro_win.blit(intro_bg, (0,0))
    pygame.display.update() 


def switch_win(is_start):
    if is_start:
        redraw_win()
    else:
        draw_intro()

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


shapes = [Z, I]
active_piece = piece(random.choice(shapes))

shape_pos = convert_shape(active_piece)

def draw_piece():
    for i in range(len(shape_pos)):
        x, y = shape_pos[i]
        win.blit(active_piece.block, (active_piece.x + (x-50), active_piece.y + (y-75)))


def music():
    pygame.mixer.init()
    pygame.mixer.music.load("assets/audio/music1.wav")
    pygame.mixer.music.play(-1)


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

    if keys[pygame.K_RETURN]:
        is_start = True

    if active_piece.y <= 520:
        active_piece.y += active_piece.vel

    switch_win(is_start)

pygame.quit()