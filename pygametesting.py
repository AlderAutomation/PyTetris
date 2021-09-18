import pygame
from pygame.constants import K_SPACE
import os

pygame.init() 

win_x = 1040
win_y = 600

win = pygame.display.set_mode((win_x, win_y)) 
pygame.display.set_caption("PyTetris")


# x,y draws to top left. 
# Top right would be x + width
# Bottom left woulf be y + height



# player variables 
x = 50
y = 50
width = 40
height = 60
vel = 20
is_jump = False
jump_count = 10
left = False
right = False
walk_count = 0


RI1 = pygame.image.load(os.path.join("assets", "RM1.png"))
RI2 = pygame.image.load(os.path.join("assets", "RM2.png"))
LI1 = 
LI2 = 

walk_left = [RI1, RI2]
walk_right = pygame.transform.flip(pygame.image.load(os.path.join("assets", "RM1.png")), True, False)

bg = pygame.image.load(os.path.join("assets", "forrest.png"))
char = pygame.image.load(os.path.join("assets", "RMStand.png"))
run = True
clock = pygame.time.Clock()

def redraw_window():
    global walk_count

    win.blit(bg, (0,0))
    
    if walk_count + 1 >= 30:
        walk_count = 0

    if left:
        win.blit(walk_left[walk_count // 5], (x,y))
        walk_count += 1
    elif right:
        win.blit(walk_right[walk_count // 5], (x,y))
        walk_count += 1
    else:
        win.blit(char, (x,y))


    pygame.display.update() 


while run:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] and x > vel:
        x -= vel
        left = True
        right = False

    elif keys[pygame.K_d] and x < win_x - vel - width:
        x += vel
        right = True
        left = False

    else:
        right = False
        Left = False
        walk_count = 0


    if not(is_jump):
        if keys[pygame.K_SPACE]:
            is_jump = True
            right = False
            left = False
            walk_count = 0
    else:
        if jump_count >= -10:
            y -= (jump_count * abs(jump_count)) * 0.5
            jump_count -= 1
        else:
            jump_count = 10
            is_jump = False

    redraw_window()

pygame.quit() # if we exit the loop this will execute
