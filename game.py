# for main play space and game rules 
import pygame
import random
import csv
import pieces

class game():
    def __init__(self, x: int, y: int, lvl: int) -> None:
        """need to pass the level arguement from previous screen"""
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
        self.t_count, self.j_count, self.z_count, self.o_count = 0, 0, 0, 0
        self.l_count, self.i_count, self.s_count = 0, 0, 0
        self.locked_positions = {}
        self.grid = self.create_grid(self.locked_positions)
        self.block_size = 24
        self.next_piece = pieces.Piece()
        self.current_piece = self.swap_next_with_current_piece()
        self.fall_speed = 0
        self.pause = False


    def draw_win(self) -> None:
        self.game_win.blit(self.game_bg, (0,0))
        self.draw_scores()
        self.draw_level()
        self.draw_lines()
        self.draw_grid(self.grid)
        self.update_piece_count()
        self.draw_pieces_for_counter()
        self.draw_next_piece()
        pygame.display.update()


    def pausing(self) -> None:
        if self.pause == False:
            self.pause = True
            pygame.mixer.Sound.play(pygame.mixer.Sound("assets/audio/effects/pause.wav"))
        elif self.pause == True:
            self.pause = False


    def create_random_piece(self) -> object:
        return pieces.Piece()


    def draw_next_piece(self) -> None:
        block = self.next_piece.colour
        format = self.next_piece.random_shape_choice[self.next_piece.rotation % len(self.next_piece.random_shape_choice)]

        for i, line in enumerate(format):
            row = list(line)
            for j, column in enumerate(row):
                if column == "0":
                    self.game_win.blit(block, (590 + j * self.block_size, 330 + i * self.block_size))


    def draw_current_piece(self) -> None:
        block = self.current_piece.colour
        format = self.current_piece.random_shape_choice[self.current_piece.rotation % len(self.current_piece.random_shape_choice)]

        for i, line in enumerate(format):
            row = list(line)
            for j, column in enumerate(row):
                if column == "0":
                    self.game_win.blit(block, (self.current_piece.x + j * self.block_size, self.current_piece.y + i * self.block_size))


    def count_piece(self):
        piece = self.current_piece.shapes.index(self.current_piece.random_shape_choice)

        if piece == 0:
           self.s_count = self.s_count + 1
        elif piece == 1:
           self.z_count = self.z_count + 1
        elif piece == 2:
           self.i_count = self.i_count + 1
        elif piece == 3:
           self.o_count = self.o_count + 1
        elif piece == 4:
           self.j_count = self.j_count + 1
        elif piece == 5:
           self.l_count = self.l_count + 1
        elif piece == 6:
           self.t_count = self.t_count + 1
          

    def swap_next_with_current_piece(self) -> object:
        current_piece = self.next_piece
        self.next_piece = pieces.Piece()
        current_piece.x = 335
        current_piece.y = 0

        return current_piece


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


    def change_level(self) -> None:
        """Every ten lines. sound effect. speed increase"""
        pass


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
                    self.game_win.blit(piece.chosen_colour, (x + j * self.block_size, y + i * self.block_size))


    def draw_pieces_for_counter(self) -> None:
        T = self.choose_piece_and_pos(6, 50, 230)
        J = self.choose_piece_and_pos(4, 50, 285)
        Z = self.choose_piece_and_pos(1, 50, 340)
        O = self.choose_piece_and_pos(3, 60, 395)
        S = self.choose_piece_and_pos(0, 50, 450)
        L = self.choose_piece_and_pos(5, 50, 505)
        I = self.choose_piece_and_pos(2, 45, 560)


    def draw_lines(self) -> None:
        stat_builder(self.lines, 460, 48, self, 3)


    def on_lose(self) -> None:
        '''no music. drop down alternating 4 coloured lines.
        Goes back to level select. There is a losing sound, like explosion'''
        pass


    def change_music_speed(self) -> None:
        pass


    def create_grid(self, locked_pos = {}) -> list:
        grid = [[(self.black)for _ in range(10)] for _ in range(20)]

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (j, i) in locked_pos:
                    c = locked_pos[(j,i)]
                    grid[i][j] = c
            
            return grid


    def draw_grid(self, grid: list) -> None:
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                pygame.draw.rect(self.game_win, grid[i][j], (287+j*self.block_size, 121+i*self.block_size, self.block_size, self.block_size))

        
    def screen_input(self, event: object) -> None:
        """A = move left
        D = Move right 
        S = faster downward velocity on keydown hold
        E = Rotate Piece Clockwise
        Q = Rotate Piece Counter Clockwise
        Enter = Pause
        Esc = Quit"""

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                if self.current_piece.x <= 300:
                    pass
                else:
                    self.current_piece.x -= 24
                    pygame.mixer.Sound.play(pygame.mixer.Sound("assets/audio/effects/piece_move.wav"))
            if event.key == pygame.K_d:
                if self.current_piece.x >= 500:
                    pass
                else:
                    self.current_piece.x += 24
                    pygame.mixer.Sound.play(pygame.mixer.Sound("assets/audio/effects/piece_move.wav"))
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                self.hold_current_speed = self.fall_speed
                self.fall_speed = self.fall_speed / 2
            if event.key == pygame.K_e:
                self.current_piece.rotation += 1
                pygame.mixer.Sound.play(pygame.mixer.Sound("assets/audio/effects/piece_rotate.wav"))
            if event.key == pygame.K_q:
                self.current_piece.rotation -= 1
                pygame.mixer.Sound.play(pygame.mixer.Sound("assets/audio/effects/piece_rotate.wav"))
            if event.key == pygame.K_RETURN:
                self.pausing()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                self.fall_speed = self.hold_current_speed


class stat_builder:
    def __init__(self, stat: int, x: int, y: int, obj: object, zeros: int = 6, colour: str = (255,255,255)) -> None:
        leading_0s = str(stat).zfill(zeros)
        obj.lines_surface = obj.game_text.render(leading_0s, False, colour, obj.black)
        obj.game_win.blit(obj.lines_surface, (x, y))
