from ursina import *
import tetrimos

app = Ursina(title="PyTetris", vsync=False, fullscreen=False)

tetrimos.tetris_board()

app.run()