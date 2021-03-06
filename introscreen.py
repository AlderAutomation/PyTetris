# this is going to be for splash screens and game mode selectors
import pygame


class intro_menu:
    def __init__(self, x, y) -> None:
        self.win_x, self.win_y = x, y
        self.intro_bg = pygame.image.load("assets/pics/Start.png")
        self.intro_bg = pygame.transform.scale(self.intro_bg, (self.win_x, self.win_y))
        self.intro_win = pygame.display.set_mode((self.win_x, self.win_y))
        self.is_start = True


    def draw_intro(self):
        self.intro_win.blit(self.intro_bg, (0,0))
        pygame.display.update() 


    def redraw_win(self):
        self.intro_win.blit(self.intro_bg, (0,0))


    def update(self, eventkey):
        self.screen_input(eventkey)


    def screen_input(self, eventkey):
        if eventkey == pygame.K_RETURN or eventkey == pygame.K_KP_ENTER and self.is_start == True:
            self.is_start = False
