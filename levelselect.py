import pygame

class level_selecter():
    def __init__(self, x: int, y: int) -> None:
        self.level_x, self.level_y = x, y
        self.level_bg = pygame.image.load("assets/pics/A_Level_Select.png")
        self.level_bg = pygame.transform.scale(self.level_bg, (self.level_x, self.level_y))
        self.level_win = pygame.display.set_mode((self.level_x, self.level_y))
        self.cursor = [pygame.image.load("assets/pics/Level_Cursor.png"), pygame.image.load("assets/pics/CursorBlank.png")]
        self.is_start = True
        self.l_cursor_index = 0
        self.levels = pygame.image.load("assets/pics/A_Level_Select_Numbers.png")
        self.levels = pygame.transform.scale(self.levels, (270,115))
        self.level_flag = 0


    def draw_main(self):
        self.level_win.blit(self.level_bg, (0,0))
        pygame.display.update() 


    def draw_level_cursor(self, x: int, y: int):
        self.l_cursor_x, self.l_cursor_y = x, y
        self.level_win.blit(self.cursor[int(self.l_cursor_index)], (self.l_cursor_x, self.l_cursor_y))
        pygame.display.update()


    def cursor_animation(self):
        self.l_cursor_index += 1
        if self.l_cursor_index >= len(self.cursor):self.l_cursor_index = 0
        self.draw_main()
        self.draw_level_cursor(self.l_cursor_x, self.l_cursor_y)
        self.draw_levels()


    def update(self, eventkey):
        self.screen_input(eventkey)


    def cursor_sound(self):
        cursor_sound = pygame.mixer.Sound("assets/audio/effects/Cursor_Move.wav")
        pygame.mixer.Sound.play(cursor_sound)

    
    def draw_levels(self):
        self.level_win.blit(self.levels, (145, 215))
        pygame.display.update()


    def screen_input(self, eventkey):
        if eventkey == pygame.K_RETURN or eventkey == pygame.K_KP_ENTER and self.is_start == True:
            self.is_start = False
        if eventkey == pygame.K_d:
            self.cursor_sound()
            if self.level_flag == 0:
                self.draw_main()
                self.draw_level_cursor(210, 230)
                self.draw_levels()
                self.level_flag = 1
            elif self.level_flag == 1:
                self.draw_main()
                self.draw_level_cursor(260, 230)
                self.draw_levels()
                self.level_flag = 2
            elif self.level_flag == 2:
                self.draw_main()
                self.draw_level_cursor(310, 230)
                self.draw_levels()
                self.level_flag = 3
            elif self.level_flag == 3:
                self.draw_main()
                self.draw_level_cursor(360, 230)
                self.draw_levels()
                self.level_flag = 4
            elif self.level_flag == 4:
                self.draw_main()
                self.draw_level_cursor(160, 280)
                self.draw_levels()
                self.level_flag = 5
            elif self.level_flag == 5:
                self.draw_main()
                self.draw_level_cursor(210, 280)
                self.draw_levels()
                self.level_flag = 6
            elif self.level_flag == 6:
                self.draw_main()
                self.draw_level_cursor(260, 280)
                self.draw_levels()
                self.level_flag = 7
            elif self.level_flag == 7:
                self.draw_main()
                self.draw_level_cursor(310, 280)
                self.draw_levels()
                self.level_flag = 8
            elif self.level_flag == 8:
                self.draw_main()
                self.draw_level_cursor(360, 280)
                self.draw_levels()
                self.level_flag = 9
        if eventkey == pygame.K_a:
            self.cursor_sound()
            if self.level_flag == 1:
                self.draw_main()
                self.draw_level_cursor(160, 230)
                self.draw_levels()
                self.level_flag = 0
            elif self.level_flag == 2:
                self.draw_main()
                self.draw_level_cursor(210, 230)
                self.draw_levels()
                self.level_flag = 1
            elif self.level_flag == 3:
                self.draw_main()
                self.draw_level_cursor(260, 230)
                self.draw_levels()
                self.level_flag = 2
            elif self.level_flag == 4:
                self.draw_main()
                self.draw_level_cursor(310, 230)
                self.draw_levels()
                self.level_flag = 3
            elif self.level_flag == 5:
                self.draw_main()
                self.draw_level_cursor(360, 230)
                self.draw_levels()
                self.level_flag = 4
            elif self.level_flag == 6:
                self.draw_main()
                self.draw_level_cursor(160, 280)
                self.draw_levels()
                self.level_flag = 5
            elif self.level_flag == 7:
                self.draw_main()
                self.draw_level_cursor(210, 280)
                self.draw_levels()
                self.level_flag = 6
            elif self.level_flag == 8:
                self.draw_main()
                self.draw_level_cursor(260, 280)
                self.draw_levels()
                self.level_flag = 7
            elif self.level_flag == 9:
                self.draw_main()
                self.draw_level_cursor(310, 280)
                self.draw_levels()
                self.level_flag = 8
        if eventkey == pygame.K_w:
            self.cursor_sound()
            if self.l_cursor_y == 280:
                self.l_cursor_y = 230
                self.level_flag = self.level_flag - 5
        if eventkey == pygame.K_s:
            self.cursor_sound()
            if self.l_cursor_y == 230:
                self.l_cursor_y = 280
                self.level_flag = self.level_flag + 5

