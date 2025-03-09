from src.constants import INITIAL_SCORE, ROWS, COLS


class Player:

    def __init__(self):
        self.reset(self)

    @staticmethod
    def reset(self):
        self.x = COLS // 2
        self.y = ROWS // 2
        self.score = INITIAL_SCORE
        self.inventory = []
        self.steps = 0
        self.active_bombs = []

    def move(self, dx: int, dy: int):
       self.x += dx
       self.y += dy
       self.steps += 1


