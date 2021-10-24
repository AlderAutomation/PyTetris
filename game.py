# for main play space and game rules 
import pygame
import random
import csv

pygame.init()

class game():
    def __init__(self, x: int, y: int, lvl: int) -> None:
        self.game_x, self.game_y = x, y
        self.lvl = lvl
        self.game_bg = pygame.image.load("assets/pics/playfield.png")
        self.game_bg = pygame.transform.scale(self.game_bg, (self.game_x, self.game_y))
        self.game_win = pygame.display.set_mode((self.game_x, self.game_y))
        self.game_text = pygame.font.Font("assets/Tetris.ttf", 24)
        self.white = (255,255,255)
        self.black = (0,0,0)
        self.score = 0
        self.load_hi_scores()
        self.lines = 0
        self.t_count = 0
        self.j_count = 0
        self.z_count = 0
        self.o_count = 0
        self.s_count = 0
        self.l_count = 0
        self.i_count = 0
        # self.play_width, self.play_height = 250, 500
        self.grid = self.create_grid()
        self.block_size = 24


    def draw_win(self) -> None:
        self.game_win.blit(self.game_bg, (0,0))
        self.draw_scores()
        self.draw_level()
        self.draw_lines()
        self.draw_grid(self.grid)
        self.update_piece_count()
        pygame.display.update()


    def pause(self) -> None:
        pass


    def random_piece(self) -> None:
        pass


    def waiting_piece(self) -> None:
        pass
    

    def draw_scores(self) -> None:
        score = stat_builder(self.score, 578, 170, self)
        hiscore = stat_builder(self.hi_score_1, 578, 98, self)


    def load_hi_scores(self) -> None:
        scores = []
        with open("assets/hi-scores.csv") as csv_file:
            lines = csv.reader(csv_file, delimiter=",")
            for row in lines:
                scores.append(int(row[2]))
        
        self.hi_score_1 = (scores[0])


    def draw_level(self) -> None:
        stat_builder(self.lvl, 625, 480, self, 2)


    def update_piece_count(self) -> None:
        T_count = stat_builder(self.t_count, 150, 240, self, 3)
        J_count = stat_builder(self.j_count, 150, 280, self, 3)
        Z_count = stat_builder(self.z_count, 150, 320, self, 3)
        O_count = stat_builder(self.o_count, 150, 360, self, 3)
        S_count = stat_builder(self.s_count, 150, 400, self, 3)
        L_count = stat_builder(self.l_count, 150, 440, self, 3)
        I_count = stat_builder(self.i_count, 150, 480, self, 3)


    def display_pieces_for_count(self) -> None:
        pass


    def draw_lines(self) -> None:
        stat_builder(self.lines, 460, 48, self, 3)


    def on_lose(self) -> None:
        '''no music. drop down alternating 4 coloured lines.
        Goes back to level select. There is a losing sound, like explosion'''
        pass


    def change_music_speed(self) -> None:
        pass


    def create_grid(self, locked_pos = {}) -> object:
        grid = [[(self.white)for _ in range(10)] for _ in range(20)]

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (j, i) in locked_pos:
                    c = locked_pos[(j,i)]
                    grid[i][j] = c
            
            return grid


    def draw_grid(self, grid: object) -> None:
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                pygame.draw.rect(self.game_win, grid[i][j], (287+j*self.block_size, 121+i*self.block_size, self.block_size, self.block_size), 1)


        
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


class stat_builder:
    def __init__(self, stat: int, x: int, y: int, obj: object, zeros: int = 6) -> None:
        leading_0s = str(stat).zfill(zeros)
        obj.lines_surface = obj.game_text.render(leading_0s, False, obj.white, obj.black)
        obj.game_win.blit(obj.lines_surface, (x, y))



if __name__== "__main__":
    Tetris = game(768, 672, 0).main()
    Tetris
    