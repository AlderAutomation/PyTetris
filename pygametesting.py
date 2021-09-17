import pygame
from pygame.constants import K_SPACE

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


run = True

while run:
    pygame.time.delay(100) #this will delay game 0.1 milliseconds

    for event in pygame.event.get(): # event listener
        if event.type == pygame.QUIT: # close button
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] and x > vel:
        x -= vel

    if keys[pygame.K_d] and x < win_x - vel - width:
        x += vel

    if not(is_jump):
        if keys[pygame.K_w] and y > vel:
            y -= vel

        if keys[pygame.K_s] and y < win_y - vel - height:
            y += vel

        if keys[pygame.K_SPACE]:
            is_jump = True
    else:
        if jump_count >= -10:
            y -= (jump_count * abs(jump_count)) * 0.5
            jump_count -= 1
        else:
            jump_count = 10
            is_jump = False


    win.fill((0,0,0))
    pygame.draw.rect(win, (255,0,0), (x, y, width, height)) # Draw a rectangle 
    pygame.display.update() # updates the screen to show rect

pygame.quit() # if we exit the loop this will execute
