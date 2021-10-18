import pygame 

class main_menu:
    def __init__(self, x: int, y: int) -> None:
        self.win_x, self.win_y = x, y
        self.menu_bg = pygame.image.load("assets/pics/MainMenu2.png")
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


    def draw_music_cursor(self, x: int, y: int):
        self.music_cursor = "1"
        self.m_cursor_x, self.m_cursor_y = x, y
        self.cursor = pygame.image.load("assets/pics/Cursor.png")
        self.menu_win.blit(self.cursor, (self.m_cursor_x, self.m_cursor_y))
        self.menu_win.blit(pygame.transform.flip(self.cursor, True, False), (x+230,y))
        pygame.display.update()


def main():
    pygame.init()

    main = main_menu(800, 600)
    main.draw_main()
    clock = pygame.time.Clock()

    run = True

    main.draw_game_cursor(195, 148)
    main.draw_music_cursor(320, 360)

    while run:
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        event = pygame.event.wait()

        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_ESCAPE:
                print("ESC was pressed. Quitting....")
                pygame.quit()
            # game cursor
            if event.key == pygame.K_d:
                if main.game_cursor == "A":
                    main.redraw_win()
                    main.draw_game_cursor(495, 148)
                    main.draw_music_cursor(main.m_cursor_x, main.m_cursor_y)
                    main.game_cursor = "B"
            if event.key == pygame.K_a:
                if main.game_cursor == "B":
                    main.redraw_win()
                    main.draw_game_cursor(195, 148)
                    main.draw_music_cursor(main.m_cursor_x, main.m_cursor_y)
                    main.game_cursor = "A"
            # music cursor
            if event.key == pygame.K_s:
                if main.music_cursor == "1":
                    main.redraw_win()
                    main.draw_music_cursor(320, 405)
                    main.draw_game_cursor(main.g_cursor_x, main.g_cursor_y)
                    main.music_cursor = "2"
                elif main.music_cursor == "2":
                    main.redraw_win()
                    main.draw_music_cursor(320, 447)
                    main.draw_game_cursor(main.g_cursor_x, main.g_cursor_y)
                    main.music_cursor = "3"
                elif main.music_cursor == "3":
                    main.redraw_win()
                    main.draw_music_cursor(320, 490)
                    main.draw_game_cursor(main.g_cursor_x, main.g_cursor_y)
                    main.music_cursor = "off"
            if event.key == pygame.K_w:
                if main.music_cursor == "off":
                    main.redraw_win()
                    main.draw_music_cursor(320, 447)
                    main.draw_game_cursor(main.g_cursor_x, main.g_cursor_y)
                    main.music_cursor = "3"
                elif main.music_cursor == "3":
                    main.redraw_win()
                    main.draw_music_cursor(320, 405)
                    main.draw_game_cursor(main.g_cursor_x, main.g_cursor_y)
                    main.music_cursor = "2"
                elif main.music_cursor == "2":
                    main.redraw_win()
                    main.draw_music_cursor(320, 360)
                    main.draw_game_cursor(main.g_cursor_x, main.g_cursor_y)
                    main.music_cursor = "1"

    
    pygame.quit()

if __name__ == "__main__":
    main()