import pygame

class level_selecter():
    def __init__(self, bglocal: str, x: int, y: int) -> None:
        self.level_x, self.level_y = x, y
        self.level_bg = pygame.image.load(bglocal)
        self.level_bg = pygame.transform.scale(self.level_bg, (self.level_x, self.level_y))
        self.level_win = pygame.display.set_mode((self.level_x, self.level_y))
        self.cursor = [pygame.image.load("assets/pics/Level_Cursor.png"), pygame.image.load("assets/pics/CursorBlank.png")]
        self.is_start = True
        self.l_cursor_index = 0
        self.levels = pygame.image.load("assets/pics/A_Level_Select_Numbers.png")
        self.levels = pygame.transform.scale(self.levels, (275,107))
        self.level_flag = 0


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
            if self.level_flag == 0:
                self.redraw_win()
                self.draw_level_cursor(218, 205)
                self.level_flag = 1
            elif self.level_flag == 1:
                self.redraw_win()
                self.draw_level_cursor(268, 205)
                self.level_flag = 2
            elif self.level_flag == 2:
                self.redraw_win()
                self.draw_level_cursor(318, 205)
                self.level_flag = 3
            elif self.level_flag == 3:
                self.redraw_win()
                self.draw_level_cursor(368, 205)
                self.level_flag = 4
            elif self.level_flag == 4:
                self.redraw_win()
                self.draw_level_cursor(168, 255)
                self.level_flag = 5
            elif self.level_flag == 5:
                self.redraw_win()
                self.draw_level_cursor(218, 255)
                self.level_flag = 6
            elif self.level_flag == 6:
                self.redraw_win()
                self.draw_level_cursor(268, 255)
                self.level_flag = 7
            elif self.level_flag == 7:
                self.redraw_win()
                self.draw_level_cursor(318, 255)
                self.level_flag = 8
            elif self.level_flag == 8:
                self.redraw_win()
                self.draw_level_cursor(368, 255)
                self.level_flag = 9
        if eventkey == pygame.K_a:
            self.cursor_sound()
            if self.level_flag == 1:
                self.redraw_win()
                self.draw_level_cursor(168, 205)
                self.level_flag = 0
            elif self.level_flag == 2:
                self.redraw_win()
                self.draw_level_cursor(218, 205)
                self.level_flag = 1
            elif self.level_flag == 3:
                self.redraw_win()
                self.draw_level_cursor(268, 205)
                self.level_flag = 2
            elif self.level_flag == 4:
                self.redraw_win()
                self.draw_level_cursor(318, 205)
                self.level_flag = 3
            elif self.level_flag == 5:
                self.redraw_win()
                self.draw_level_cursor(368, 205)
                self.level_flag = 4
            elif self.level_flag == 6:
                self.redraw_win()
                self.draw_level_cursor(168, 255)
                self.level_flag = 5
            elif self.level_flag == 7:
                self.redraw_win()
                self.draw_level_cursor(218, 255)
                self.level_flag = 6
            elif self.level_flag == 8:
                self.redraw_win()
                self.draw_level_cursor(268, 255)
                self.level_flag = 7
            elif self.level_flag == 9:
                self.redraw_win()
                self.draw_level_cursor(318, 255)
                self.level_flag = 8
        if eventkey == pygame.K_w:
            self.cursor_sound()
            if self.l_cursor_y == 255:
                self.l_cursor_y = 205
                self.level_flag = self.level_flag - 4
        if eventkey == pygame.K_s:
            self.cursor_sound()
            if self.l_cursor_y == 205:
                self.l_cursor_y = 255
                self.level_flag = self.level_flag + 4


    def cursor_sound(self):
        cursor_sound = pygame.mixer.Sound("assets/audio/effects/Cursor_Move.wav")
        pygame.mixer.Sound.play(cursor_sound)

    
    def draw_levels(self):
        self.level_win.blit(self.levels, (154, 194))
        
        pygame.display.update()


def main():
    clock = pygame.time.Clock()
    pygame.mixer.init()
    level_select = level_selecter("assets/pics/A_Level_Select.png", 800, 600)
    level_select.draw_main()
    level_select.draw_level_cursor(168, 205)

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
        level_select.draw_levels()






if __name__ == "__main__":
    main()