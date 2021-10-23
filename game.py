# for main play space and game rules 
import pygame
import random
import csv


pygame.init()
pygame.font.init()


class game():
    def __init__(self, x: int, y: int, lvl: int) -> None:
        self.game_x, self.game_y = x, y
        self.lvl = lvl
        self.game_bg = pygame.image.load("assets/pics/playfield.png")
        self.game_bg = pygame.transform.scale(self.game_bg, (self.game_x, self.game_y))
        self.game_win = pygame.display.set_mode((self.game_x, self.game_y))
        self.game_text = pygame.font.Font("assets/Tetris.ttf", 25)
        self.white = (255,255,255)
        self.black = (0,0,0)
        self.score = 0
        self.load_hi_scores()
        self.lines = 0
    

    def draw_win(self) -> None:
        self.game_win.blit(self.game_bg, (0,0))
        self.draw_score()
        self.draw_hi_score()
        self.draw_level()
        self.draw_lines()
        pygame.display.update()


    def pause(self) -> None:
        pass


    def random_piece(self) -> None:
        pass


    def waiting_piece(self) -> None:
        pass
    

    def draw_score(self) -> None:
        leading_0s = str(self.score).zfill(6)
        self.score_surface = self.game_text.render(leading_0s, False, self.white, self.black)
        self.game_win.blit(self.score_surface, (600,150))


    def draw_hi_score(self) -> None:
        leading_0s = str(self.hi_score_1).zfill(6)
        self.hi_score_surface = self.game_text.render(leading_0s, False, self.white, self.black)
        self.game_win.blit(self.hi_score_surface, (600,90))


    def load_hi_scores(self) -> None:
        scores = []
        with open("assets/hi-scores.csv") as csv_file:
            lines = csv.reader(csv_file, delimiter=",")
            for row in lines:
                scores.append(int(row[2]))
        
        self.hi_score_1 = (scores[0])


    def draw_level(self) -> None:
        leading_0s = str(self.lvl).zfill(2)
        self.lvl_surface = self.game_text.render(leading_0s, False, self.white, self.black)
        self.game_win.blit(self.lvl_surface, (650,430))


    def update_piece_count(self) -> None:
        pass


    def display_pieces_for_count(self) -> None:
        pass


    def draw_lines(self) -> None:
        leading_0s = str(self.lines).zfill(3)
        self.lines_surface = self.game_text.render(leading_0s, False, self.white, self.black)
        self.game_win.blit(self.lines_surface, (475, 42))



    def on_lose(self) -> None:
        '''no music. drop down alternating 4 coloured lines.
        Goes back to level select. There is a losing sound, like explosion'''
        pass


    def change_music_speed(self) -> None:
        pass


    def screen_input(self) -> None:
        pass


    def main(self) -> None:
        self.draw_win()

        game_running = True

        clock = pygame.time.Clock()

        self.load_hi_scores()


        while game_running:
            clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_running = False

                if event.type == pygame.KEYDOWN :
                    if event.key == pygame.K_ESCAPE:
                        print("ESC was pressed. Quitting....")
                        game_running = False

            self.draw_win()



if __name__== "__main__":
    Tetris = game(800, 600, 0).main()
    Tetris
    