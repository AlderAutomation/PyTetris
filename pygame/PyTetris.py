import pygame 
import random
import Tetrimos

screen_width = 1080
screen_height = 640
play_width = 300
play_height = 600
block_size = 30
top_left_x = (screen_width - play_width) // 2
top_left_y = screen_height - play_height

shapes = [Tetrimos.S_Block, Tetrimos.Z_Block, Tetrimos.J_Block, Tetrimos.J_Block, Tetrimos.L_Block, Tetrimos.I_Block, Tetrimos.O_Block]
shape_colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]

def create_grid(locked_positions{}):
    grid = [[(0,0,0) for x in range(10)] for x in range(20)]

    for i in range(len(grid)):
        for j in range(grid(i)):
            if (j,i) in locked_positions:
                c = locked_positions[(j,i)]
                grid[i][j] = c
    return grid 

    