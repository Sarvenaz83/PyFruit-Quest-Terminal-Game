import random

from src.constants import  SYMBOLS

class Grid:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [[SYMBOLS['empty']]* cols for _ in range(rows)]
        self.generate_walls()

    def generate_walls(self):
        for x in range(self.cols):
            self.grid[0][x] = SYMBOLS['wall']
            self.grid[self.rows - 1][x] = SYMBOLS['wall']
        for y in range(self.rows):
            self.grid[y][0] = SYMBOLS['wall']
            self.grid[y][self.cols - 1] = SYMBOLS['wall']
        for y in range(1, self.cols - 1, 2):
            if y % 2 == 0:
                self.grid[y][self.rows - 1] = SYMBOLS['wall']

        for _ in range(10):
            x, y = random.randint(2, self.cols - 3), random.randint(1, self.rows - 2)
            self.grid[y][x] = SYMBOLS['wall']


    def is_within_bounds(self, x, y):
        return 0 <= x < self.cols and 0 <= y < self.rows

    def is_empty(self, x, y):
        return self.grid[y][x] == SYMBOLS['empty']

    def place_item(self, x, y, item):
        if self.is_within_bounds(x, y):
            self.grid[y][x] = item

    def remove_item(self, x, y):
        if self.is_within_bounds(x, y):
            self.grid[y][x] = SYMBOLS['empty']

    def get_item(self, x, y):
        if self.is_within_bounds(x, y):
            return self.grid[y][x]
        return None


    def move_entity(self, entity, new_x, new_y):
        if self.is_within_bounds(new_x, new_y) and self.is_empty(new_x, new_y):
            self.remove_item(entity.x, entity.y)
            entity.x = new_x, entity.y = new_y
            self.place_item(new_x, new_y, entity.symbol)

    def render(self):
        for row in self.grid:
            print("".join(
                str(cell) if isinstance(cell, str) else SYMBOLS.get(cell.__class__.__name__.lower(), "?")
                for cell in row
            ))
