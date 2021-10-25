# for main play space and game rules 
import pygame
import random
import csv
import pieces

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
        self.locked_positions = {}
        self.grid = self.create_grid(self.locked_positions)
        self.block_size = 24
        self.next_piece = self.create_random_piece()


    def draw_win(self) -> None:
        self.game_win.blit(self.game_bg, (0,0))
        self.draw_scores()
        self.draw_level()
        self.draw_lines()
        self.draw_grid(self.grid)
        self.update_piece_count()
        self.draw_next_piece()
        self.draw_pieces_for_counter()
        pygame.display.update()


    def pause(self) -> None:
        pass


    def create_random_piece(self) -> object:
        return pieces.Piece()


    def draw_next_piece(self) -> None:
        block = self.next_piece.colour
        format = self.next_piece.random_shape_choice[self.next_piece.rotation % len(self.next_piece.random_shape_choice)]

        for i, line in enumerate(format):
            row = list(line)
            for j, column in enumerate(row):
                if column == "0":
                    self.game_win.blit(block, (560 + j * 25, 300 + i * 25))


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
        T_count = stat_builder(self.t_count, 155, 240, self, 3, (216,40,0))
        J_count = stat_builder(self.j_count, 155, 290, self, 3, (216,40,0))
        Z_count = stat_builder(self.z_count, 155, 345, self, 3, (216,40,0))
        O_count = stat_builder(self.o_count, 155, 400, self, 3, (216,40,0))
        S_count = stat_builder(self.s_count, 155, 450, self, 3, (216,40,0))
        L_count = stat_builder(self.l_count, 155, 510, self, 3, (216,40,0))
        I_count = stat_builder(self.i_count, 155, 560, self, 3, (216,40,0))


    def choose_piece_and_pos(self, choice: int, x: int, y: int) -> None:
        piece = pieces.Piece(choice)
        format = piece.chosen_shape[piece.rotation % len(piece.chosen_shape)]

        for i, line in enumerate(format):
            row = list(line)
            for j, column in enumerate(row):
                if column == "0":
                    self.game_win.blit(piece.chosen_colour, (x + j * 25, y + i * 25))


    def draw_pieces_for_counter(self) -> None:
        T = self.choose_piece_and_pos(6, 35, 170)
        J = self.choose_piece_and_pos(4, 35, 225)
        Z = self.choose_piece_and_pos(1, 35, 280)
        O = self.choose_piece_and_pos(3, 25, 335)
        S = self.choose_piece_and_pos(0, 35, 390)
        L = self.choose_piece_and_pos(5, 35, 445)
        I = self.choose_piece_and_pos(2, 50, 510)


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
    def __init__(self, stat: int, x: int, y: int, obj: object, zeros: int = 6, colour: str = (255,255,255)) -> None:
        leading_0s = str(stat).zfill(zeros)
        obj.lines_surface = obj.game_text.render(leading_0s, False, colour, obj.black)
        obj.game_win.blit(obj.lines_surface, (x, y))


if __name__== "__main__":
    Tetris = game(768, 672, 0).main()
    Tetris
    