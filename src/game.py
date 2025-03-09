import random
from src.grid import Grid
from src.constants import SYMBOLS, ROWS, COLS, ENEMY_COUNT, WIN_MESSAGE, \
    LOSE_MESSAGE, INITIAL_SCORE
from src.player import Player

from src.pickups import randomize, Spade, Key, Chest
from src.enemies import EnemyAI


class Game:

    def __init__(self):
        self.score = INITIAL_SCORE
        self.grid = Grid(ROWS, COLS)
        self.player = Player()
        self.grid.place_item(self.player.x, self.player.y, SYMBOLS['player'])
        self.enemies = self._spawn_enemies()
        randomize(self.grid)

    def _spawn_enemies(self):
        enemies = []
        while len(enemies) < ENEMY_COUNT:
            x, y = random.randint(0, COLS - 1), random.randint(0, ROWS - 1)
            if self.grid.is_empty(x, y) and (abs(x - self.player.x) + abs(y - self.player.y) > 5):
                enemies.append(EnemyAI(x, y))
                self.grid.place_item(x, y, SYMBOLS['enemy'])
        return enemies

    def play_turn(self, dx, dy):
        new_x, new_y = self.player.x + dx, self.player.y + dy
        if not self.grid.is_within_bounds(new_x, new_y):
            print("Cannot move outside the grid!")
            return
        item = self.grid.get_item(new_x, new_y)
        if item:
            self.handle_item(item)
        self.grid.move_entity(self.player, new_x, new_y)
        self.player.move(dx, dy)
        for enemy in self.enemies:
            enemy.move_towards(self.player.x, self.player.y)
            self.grid.move_entity(enemy, enemy.x, enemy.y)

        self.check_game_status()

    def handle_item(self, item):
        if item == SYMBOLS['fruit']:
            self.player.score +=20
        elif item == SYMBOLS['trap']:
            self.player.score -= 10
        elif item == SYMBOLS['enemy']:
            self.player.score -= 20
        elif item == SYMBOLS['chest']:
            self.player.score += 100
        elif item == SYMBOLS['exit']:
            self.win_game()
        self.grid.remove_item(self.player.x, self.player.y)

    def check_game_status(self):
        if self.player.score <= 0:
            self.lose_game()

    @staticmethod
    def win_game():
        print(WIN_MESSAGE)
        exit()

    @staticmethod
    def lose_game():
        print(LOSE_MESSAGE)
        exit()

    @staticmethod
    def run():
        print("Game started!")

    def display(self):
        self.grid.render()
        print(f"🎯Player Position: {self.player.x}, {self.player.y}")
        print(f"💰Score: {self.player.score}")

    def handle_input(self, cmd: str):
        dx, dy = 0, 0
        if cmd == "W":
            dy = -1
        elif cmd == "A":
            dx = -1
        elif cmd == "S":
            dy = 1
        elif cmd == "D":
            dx = 1
        elif cmd =="I":
            self.show_inventory()
            return

        new_x, new_y = self.player.x + dx, self.player.y + dy

        if self.grid.is_within_bounds(new_x, new_y):
            cell = self.grid.get_item(new_x, new_y)
            if cell == SYMBOLS['wall']:
                if any(isinstance(item, Spade) for item in self.player.inventory):
                    print("⛏ You used a spade to break the wall!")
                    self.player.inventory = [item for item in self.player.inventory if not isinstance(item, Spade)]
                    self.grid.remove_item(new_x, new_y)
                    self.grid.place_item(new_x, new_y, SYMBOLS['empty'])
                else:
                    print("🚧 You hit a wall! Movement blocked.")
                    return
            elif cell == SYMBOLS['fruit']:
                self.player.score += 20
                print("🍏 You collected a fruit! (+20 points)")
                self.grid.remove_item(new_x, new_y)
            elif cell == SYMBOLS['trap']:
                self.player.score -= 10
                print("⚡ You stepped on a trap! (-10 points)")
                self.grid.remove_item(new_x, new_y)
            elif cell == SYMBOLS['enemy']:
                self.player.score -= 20
                print("👾 You were caught by an enemy! (-20 points)")
            elif cell == SYMBOLS['key']:
                self.player.inventory.append(Key())
                print("🔑 You picked up a key!")
                self.grid.remove_item(new_x, new_y)
            elif cell == SYMBOLS['chest']:
                if any(isinstance(item, Key) for item in self.player.inventory):
                    chest = Chest()
                    chest.locked = False
                    self.player.inventory.append(chest)
                    self.player.inventory = [item for item in self.player.inventory if not isinstance(item, Key)]
                    self.player.score += 100
                    print("📦 You opened a chest and collected treasure!")
                    self.grid.remove_item(new_x, new_y)
                else:
                    print("❌ You need a key to open the chest!")
            elif cell == SYMBOLS['spade']:
                self.player.inventory.append(Spade())
                print("⛏ You picked up a spade! (Can break walls)")
                self.grid.remove_item(new_x, new_y)
            self.grid.remove_item(self.player.x, self.player.y)
            self.player.move(dx, dy)
            self.grid.place_item(self.player.x, self.player.y, SYMBOLS['player'])
            self.display()
    def show_inventory(self):
        print("\n📦 --- Inventory ---")
        if not self.player.inventory:
            print("🔹 Inventory is empty!")
            return

        for item in self.player.inventory:
            if isinstance(item, Spade):
                print(f"- {item.name}: ⛏ Can break walls! (One-time use)")
            elif isinstance(item, Chest) and not item.locked:
                print(f"- {item.name}: Opened! 🎉 (Contains treasure)")
            else:
                print(f"- {item.name}: {item.description}")
            print("-----------------------")

if __name__ == '__main__':
    game = Game()
    while True:
        move = input("Enter move (WASD): ").upper()
        if move == "W":
            game.play_turn(0, -1)
        elif move == "S":
            game.play_turn(0,1)
        elif move == "A":
            game.play_turn(-1,0)
        elif move == "D":
            game.play_turn(1,0)


