import pygame

# this is no good. I think this needs to be a list 
# like every tutorial out there is saying 
def ooh(self, win):
    o_block = pygame.image.load("assets/o_block.png")
    win.blit(o_block, (self.x, self.y))
    win.blit(o_block, (self.x + 30, self.y))
    win.blit(o_block, (self.x, self.y + 30))
    win.blit(o_block, (self.x + 30, self.y + 30))

def tee(self, win):
    tee_block = pygame.image.load("assets/t_i_block.png")
    win.blit(tee_block, (self.x, self.y))
    win.blit(tee_block, (self.x + 30, self.y))
    win.blit(tee_block, (self.x + 60, self.y))
    win.blit(tee_block, (self.x + 30, self.y + 30))

def eye(self, win):
    eye_block = pygame.image.load("assets/t_i_block.png")
    win.blit(eye_block, (self.x -30, self.y))
    win.blit(eye_block, (self.x, self.y))
    win.blit(eye_block, (self.x + 30, self.y))
    win.blit(eye_block, (self.x + 60, self.y))


# shapes based on lists test. 
Z = [['.....',
      '.00..',
      '..00.'],
     ['...0.',
      '..00.',
      '..0..']]