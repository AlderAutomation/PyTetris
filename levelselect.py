import pygame

class level_selecter():
    def __init__(self, bglocal: str, x: int, y: int) -> None:
        self.level_x, self.level_y = x, y
        self.level_bg = pygame.image.load(bglocal)
        self.level_bg = pygame.transform.scale(self.level_bg, (self.level_x, self.level_y))
        self.level_win = pygame.display.set_mode((self.level_x, self.level_y))
        self.is_start = True
        self.cursor = [pygame.image.load("assets/pics/Level_Cursor.png"), pygame.image.load("assets/pics/CursorBlank.png")]
        self.l_cursor_index = 0

    def draw_main(self):
        self.level_win.blit(self.level_bg, (0,0))
        pygame.display.update() 


    def redraw_win(self):
        self.level_win.blit(self.level_bg, (0,0))
        pygame.display.update()


    def draw_level_cursor(self, x: int, y: int):
        self.l_cursor_x, self.l_cursor_y = x, y
        self.level_win.blit(self.cursor[int(self.l_cursor_index)], (self.l_cursor_x, self.l_cursor_y))
        pygame.display.update()


    def cursor_animation(self):
        self.l_cursor_index += 1
        if self.l_cursor_index >= len(self.cursor):self.l_cursor_index = 0
        self.redraw_win()
        self.draw_level_cursor(self.l_cursor_x, self.l_cursor_y)


    def update(self, eventkey):
        self.screen_input(eventkey)


    def screen_input(self, eventkey):
        if eventkey == pygame.K_RETURN or eventkey == pygame.K_KP_ENTER and self.is_start == True:
            self.is_start = False
            pygame.quit()
        if eventkey == pygame.K_d:
            self.cursor_sound()


    def cursor_sound(self):
        cursor_sound = pygame.mixer.Sound("assets/audio/effects/Cursor_Move.wav")
        pygame.mixer.Sound.play(cursor_sound)


def main():
    clock = pygame.time.Clock()
    pygame.mixer.init()
    level_select = level_selecter("assets/pics/A_Level_Select.png", 800, 600)
    level_select.draw_main()
    level_select.draw_level_cursor(175, 210)

    level_select_loop = True

    while level_select_loop:
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                level_select_loop = False

            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_ESCAPE:
                    print("ESC was pressed. Quitting....")
                    pygame.quit()


                level_select.update(event.key)

        level_select.cursor_animation()






if __name__ == "__main__":
    main()