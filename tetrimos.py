from ursina import *entity, 

def tetris_board():
    counter_y = 5
    for y in range(20):
        counter_y = counter_y - 0.45
        counter_x = -2.5
        for x in range(10):
            counter_x = counter_x + .45
            block = Entity(model='cube', position= (counter_x, counter_y, 0), color=color.black33, scale=(.4, .4, 0))

def square():
    block1 = Entity(model='')