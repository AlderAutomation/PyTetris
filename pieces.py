# for tetrimos layouts and draw specifics
import pygame 
import random

class Piece():
    def __init__(self, num: int = 0) -> None:

        # Shapes
        S = [['.00',
            '00.'],
            ['0.',
            '00',
            '.0']]


        Z = [['00.',
            '.00',],
            ['.0.',
            '00.',
            '0..']]

        I = [['0000.'],
            ['0',
            '0',
            '0',
            '0']]

        O = [['00',
            '00']]

        J = [['.....',
            '.0...',
            '.000.',
            '.....',
            '.....'],
            ['.....',
            '..00.',
            '..0..',
            '..0..',
            '.....'],
            ['.....',
            '.....',
            '.000.',
            '...0.',
            '.....'],
            ['.....',
            '..0..',
            '..0..',
            '.00..',
            '.....']]

        L = [['.....',
            '...0.',
            '.000.',
            '.....',
            '.....'],
            ['.....',
            '..0..',
            '..0..',
            '..00.',
            '.....'],
            ['.....',
            '.....',
            '.000.',
            '.0...',
            '.....'],
            ['.....',
            '.00..',
            '..0..',
            '..0..',
            '.....']]

        T = [['.....',
            '..0..',
            '.000.',
            '.....',
            '.....'],
            ['.....',
            '..0..',
            '..00.',
            '..0..',
            '.....'],
            ['.....',
            '.....',
            '.000.',
            '..0..',
            '.....'],
            ['.....',
            '..0..',
            '.00..',
            '..0..',
            '.....']]


        s = pygame.image.load("assets/pics/s_j_block.png")
        z = pygame.image.load("assets/pics/z_l_block.png")
        i = pygame.image.load("assets/pics/t_i_block.png")
        o = pygame.image.load("assets/pics/o_block.png")
        j = pygame.image.load("assets/pics/s_j_block.png")
        l = pygame.image.load("assets/pics/z_l_block.png")
        t = pygame.image.load("assets/pics/t_i_block.png")

        self.shapes = [S, Z, I, O, J, L, T]
        self.colours_list = [s, z, i, o, j, l, t]
        self.random_shape_choice = random.choice (self.shapes)
        self.chosen_shape = self.shapes[num]
        self.chosen_colour = self.colours_list[num]
        self.colour = self.colours_list[self.shapes.index(self.random_shape_choice)]
        self.x = 0
        self.y = 0
        self.rotation = 0