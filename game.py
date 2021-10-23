# for main play space and game rules 
import pygame
import random




class game:
    def __init__(self) -> None:
        pass


    def pause(self) -> None:
        pass


    def random_piece(self) -> None:
        pass


    def wating_piece(self) -> None:
        pass
    

    def update_score(self) -> None:
        pass


    def update_piece_count(self) -> None:
        pass

    
    def update_level(self) -> None:
        pass


    def update_line(self) -> None:
        pass


    def top_score(self) -> None:
        pass


    def on_lose(self) -> None:
        '''no music. drop down alternating 4 coloured lines.
        Goes back to level select. There is a losing sound, like explosion'''
        pass


    def change_music_speed(self) -> None:
        pass


    def screen_input(self) -> None:
        pass





    def main(self) -> None:
        game_running = True
        clock = pygame.time.Clock()

        while game_running:
            clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False

            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_ESCAPE:
                    print("ESC was pressed. Quitting....")
                    game_running = False




if __name__== "__main__":
    Tetris = game().main()
    Tetris