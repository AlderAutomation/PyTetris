import pygame


def ooh(self, win):
    self.x = 375
    self.y = 50
    o_block = pygame.image.load("assets/o_block.png")
    win.blit(o_block, (self.x, self.y))
    win.blit(o_block, (self.x + 30, self.y))
    win.blit(o_block, (self.x, self.y + 30))
    win.blit(o_block, (self.x + 30, self.y + 30))

def tee(self, win):
    self.x = 375
    self.y = 50 
    tee_block = pygame.image.load("assets/t_i_block.png")
    win.blit(tee_block, (self.x, self.y))
    win.blit(tee_block, (self.x + 30, self.y))
    win.blit(tee_block, (self.x + 60, self.y))
    win.blit(tee_block, (self.x + 30, self.y + 30))

def eye(self, win):
    self.x = 350
    self.y = 50 
    eye_block = pygame.image.load("assets/t_i_block.png")
    win.blit(eye_block, (self.x, self.y))
    win.blit(eye_block, (self.x + 30, self.y))
    win.blit(eye_block, (self.x + 60, self.y))
    win.blit(eye_block, (self.x + 90, self.y))
