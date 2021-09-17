from ursina import *

def tetris_board():
    counter_y = 5
    for y in range(20):
        counter_y = counter_y - 0.45
        counter_x = -2.5
        for x in range(10):
            counter_x = counter_x + .45
            block = Entity(model='cube', position= (counter_x, counter_y, 0), color=color.black33, scale=(.4, .4, 0))

def square():
    block_x = -2.5
    block_y = 5
    block1 = Entity(model='', position=(block_x, block_y, 1), color = color.yellow, scale = (.4, .4, 0))