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

        J = [['000',
            '0..'],
            ['.0',
            '.0',
            '00'],
            ['0..',
            '000'],
            ['00',
            '0.',
            '0.']]

        L = [['000',
            '0..'],
            ['00',
            '.0',
            '.0'],
            ['..0',
            '000'],
            ['0.',
            '0.',
            '00']]

        T = [['000',
            '.0.'],
            ['.0',
            '00',
            '.0'],
            ['.0.',
            '000'],
            ['0.',
            '00',
            '0.']]


        s = pygame.image.load("assets/pics/s_j_block.png")
        s = pygame.transform.scale(s, (21, 21))
        z = pygame.image.load("assets/pics/z_l_block.png")
        z = pygame.transform.scale(z, (21, 21))
        i = pygame.image.load("assets/pics/t_i_block.png")
        i = pygame.transform.scale(i, (21, 21))
        o = pygame.image.load("assets/pics/o_block.png")
        o = pygame.transform.scale(o, (21, 21))
        j = pygame.image.load("assets/pics/s_j_block.png")
        j = pygame.transform.scale(j, (21, 21))
        l = pygame.image.load("assets/pics/z_l_block.png")
        l = pygame.transform.scale(l, (21, 21))
        t = pygame.image.load("assets/pics/t_i_block.png")
        t = pygame.transform.scale(t, (21, 21))

        self.shapes = [S, Z, I, O, J, L, T]
        self.colours_list = [s, z, i, o, j, l, t]
        self.random_shape_choice = random.choice (self.shapes)
        self.chosen_shape = self.shapes[num]
        self.chosen_colour = self.colours_list[num]
        self.colour = self.colours_list[self.shapes.index(self.random_shape_choice)]
        self.x = 0
        self.y = 0
        self.rotation = 0