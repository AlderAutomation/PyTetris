import pygame 

class main_menu:
    def __init__(self, x: int, y: int) -> None:
        self.win_x, self.win_y = x, y
        self.menu_bg = pygame.image.load("assets/pics/MainMenu2.png")
        self.menu_bg = pygame.transform.scale(self.menu_bg, (self.win_x, self.win_y))
        self.menu_win = pygame.display.set_mode((self.win_x, self.win_y))
        self.is_start = True
        self.cursor = [pygame.image.load("assets/pics/Cursor.png"), pygame.image.load("assets/pics/CursorBlank.png")]
        self.cursor_index = 0
        self.game_cursor = "A"
        self.music_cursor = "1"


    def draw_main(self):
        self.menu_win.blit(self.menu_bg, (0,0))
        pygame.display.update() 


    def redraw_win(self):
        self.menu_win.blit(self.menu_bg, (0,0))
        pygame.display.update()


    def draw_game_cursor(self, x: int, y: int, flip=True):
        self.g_cursor_x, self.g_cursor_y = x, y
        self.menu_win.blit(self.cursor[int(self.cursor_index)], (self.g_cursor_x, self.g_cursor_y))
        self.menu_win.blit(pygame.transform.flip(self.cursor[int(self.cursor_index)], True, False), (self.g_cursor_x+180,self.g_cursor_y))
        pygame.display.update()


    def draw_music_cursor(self, x: int, y: int):
        self.m_cursor_x, self.m_cursor_y = x, y
        self.menu_win.blit(self.cursor[int(self.cursor_index)], (self.m_cursor_x, self.m_cursor_y))
        self.menu_win.blit(pygame.transform.flip(self.cursor[int(self.cursor_index)], True, False), (self.m_cursor_x+230,self.m_cursor_y))
        pygame.display.update()


    def cursor_animation(self):
        self.cursor_index += 1
        if self.cursor_index >= len(self.cursor):self.cursor_index = 0
        self.redraw_win()
        self.draw_game_cursor(self.g_cursor_x, self.g_cursor_y)
        self.draw_music_cursor(self.m_cursor_x, self.m_cursor_y)


    def screen_input(self, eventkey):
        # game mode selector controls
        if eventkey == pygame.K_d:
            if self.game_cursor == "A":
                self.redraw_win()
                self.draw_game_cursor(495, 148)
                self.draw_music_cursor(self.m_cursor_x, self.m_cursor_y)
                self.game_cursor = "B"
        if eventkey == pygame.K_a:
            if self.game_cursor == "B":
                self.redraw_win()
                self.draw_game_cursor(195, 148)
                self.draw_music_cursor(self.m_cursor_x, self.m_cursor_y)
                self.game_cursor = "A"
        #  music selector controls 
        if eventkey == pygame.K_s:
            if self.music_cursor == "1":
                self.redraw_win()
                self.draw_music_cursor(320, 405)
                self.draw_game_cursor(self.g_cursor_x, self.g_cursor_y)
                self.music_cursor = "2"
                self.music()
            elif self.music_cursor == "2":
                self.redraw_win()
                self.draw_music_cursor(320, 447)
                self.draw_game_cursor(self.g_cursor_x, self.g_cursor_y)
                self.music_cursor = "3"
                self.music()
            elif self.music_cursor == "3":
                self.redraw_win()
                self.draw_music_cursor(320, 490)
                self.draw_game_cursor(self.g_cursor_x, self.g_cursor_y)
                self.music_cursor = "off"
                self.music()
        if eventkey == pygame.K_w:
            if self.music_cursor == "off":
                self.redraw_win()
                self.draw_music_cursor(320, 447)
                self.draw_game_cursor(self.g_cursor_x, self.g_cursor_y)
                self.music_cursor = "3"
                self.music()
            elif self.music_cursor == "3":
                self.redraw_win()
                self.draw_music_cursor(320, 405)
                self.draw_game_cursor(self.g_cursor_x, self.g_cursor_y)
                self.music_cursor = "2"
                self.music()
            elif self.music_cursor == "2":
                self.redraw_win()
                self.draw_music_cursor(320, 360)
                self.draw_game_cursor(self.g_cursor_x, self.g_cursor_y)
                self.music_cursor = "1"
                self.music()
        if eventkey == pygame.K_RETURN or eventkey == pygame.K_KP_ENTER:
            self.is_start = False


    def update(self, eventkey):
        self.screen_input(eventkey)


    def music(self):
        pygame.mixer.init()
        if self.music_cursor == "1":
            pygame.mixer.music.load("assets/audio/music1.wav")
            pygame.mixer.music.play(-1)
        elif self.music_cursor == "2":
            pygame.mixer.music.load("assets/audio/music2.wav")
            pygame.mixer.music.play(-1)
        elif self.music_cursor == "3":
            pygame.mixer.music.load("assets/audio/music3.wav")
            pygame.mixer.music.play(-1)
        elif self.music_cursor == "off":
            pygame.mixer.quit()
