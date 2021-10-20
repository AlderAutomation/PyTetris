import pygame

class level_selecter():
    def __init__(self, bglocal: str, x: int, y: int) -> None:
        self.win_x, self.win_y = x, y
        self.menu_bg = pygame.image.load(bglocal)
        self.menu_bg = pygame.transform.scale(self.menu_bg, (self.win_x, self.win_y))
        self.menu_win = pygame.display.set_mode((self.win_x, self.win_y))
        self.is_start = True


    def draw_main(self):
        self.menu_win.blit(self.menu_bg, (0,0))
        pygame.display.update() 


    def redraw_win(self):
        self.menu_win.blit(self.menu_bg, (0,0))
        pygame.display.update()


    def draw_game_cursor(self, x: int, y: int, flip=True):
        self.game_cursor = "A"
        self.g_cursor_x, self.g_cursor_y = x, y
        self.cursor = pygame.image.load("assets/pics/Cursor.png")
        self.menu_win.blit(self.cursor, (self.g_cursor_x, self.g_cursor_y))
        self.menu_win.blit(pygame.transform.flip(self.cursor, True, False), (x+180,y))
        pygame.display.update()


    def update(self, eventkey):
        self.screen_input(eventkey)


    def screen_input(self, eventkey):
        if eventkey == pygame.K_RETURN or eventkey == pygame.K_KP_ENTER and self.is_start == True:
            self.is_start = False


def main():
    level_select = level_selecter("assets/pics/ALevelSelect.png", 800, 600)
    level_select.draw_main()

    level_select_loop = True

    while level_select_loop:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                main_menu_loop = False

            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_ESCAPE:
                    print("ESC was pressed. Quitting....")
                    pygame.quit()

                level_select.update(event.key)







if __name__ == "__main__":
    main()