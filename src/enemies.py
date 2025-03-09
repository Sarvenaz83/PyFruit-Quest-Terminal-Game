from src.constants import SYMBOLS, COLS, ROWS
import random

class EnemyAI:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.symbol = SYMBOLS['enemy']

    def move_towards(self, target_x: int, target_y: int):
        dx = 1 if target_x > self.x else -1 if target_x < self.x else 0
        dy = 1 if target_y > self.y else -1 if target_y < self.y else 0

        if random.random() < 0.7:
            self.x += dx
            self.y += dy