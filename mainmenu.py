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
        self.cursor = pygame.image.load("assets/pics/Cursor.png")
        self.menu_win.blit(self.cursor, (x,y))
        self.menu_win.blit(pygame.transform.flip(self.cursor, True, False), (x+180,y))
        pygame.display.update()




def main():
    pygame.init()

    main = main_menu(800, 600)
    main.draw_main()
    game_cursor = "A"

    run = True

    main.draw_game_cursor(195, 148)

    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        event = pygame.event.wait()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                print("ESC was pressed. Quitting....")
                pygame.quit()
            if event.key == pygame.K_d:
                if game_cursor == "A":
                    main.redraw_win()
                    main.draw_game_cursor(495, 148)
                    game_cursor = "B"
            if event.key == pygame.K_a:
                if game_cursor == "B":
                    main.redraw_win()
                    main.draw_game_cursor(195, 148)
                    game_cursor = "A"

    
    pygame.quit()

if __name__ == "__main__":
    main()