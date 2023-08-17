import numpy as np

class Game:
    
    def __init__(self, player1, player2):
        self.players = [player1, player2]
        self.colors = ['yellow', 'red']
        self.current_turn = 0
        self.board = np.zeros([6,7]).astype(np.uint8)
        self.gui_board = []
        self.game_over = False

        for row in range(0, 700, 100):
            column = []
            for col in range(0, 700, 100):
                column.append('⚪')
            self.gui_board.append(column)

   
