import random
from src.constants import SYMBOLS, FRUIT_VALUE, TRAP_PENALTY, CHEST_VALUE
from dataclasses import dataclass

@dataclass
class Item:
    def __init__(self, name, value, description):
        self.name = name
        self.value = value
        self.description = description

    def __str__(self):
        return SYMBOLS.get(self.name.lower(), "?")

class Fruit(Item):
    def __init__(self, value=FRUIT_VALUE):
        super().__init__(
            name="Fruit",
            value=value,
            description="A delicious fruit worth points"
        )

class Trap(Item):
    def __init__(self):
        super().__init__(
            name="Trap",
            value=TRAP_PENALTY,
            description="Dangerous floor trap that damages you"
        )

class Spade(Item):
    def __init__(self):
        super().__init__(
            name="Spade",
            value=0,
            description="Dig through walls"
        )

class Key(Item):
    def __init__(self):
        super().__init__(
            name="Key",
            value=0,
            description="Used to open chests"
        )

class Chest(Item):
    def __init__(self, value=CHEST_VALUE):
        super().__init__(
            name="Chest",
            value=value,
            description="Contains treasure"
        )
        self.locked = True

class Bomb(Item):
    def __init__(self):
        super().__init__(
            name="Bomb",
            value=-50,
            description="Explodes after 3 turns"
        )

def randomize(grid, num_fruits=8, num_traps=5, num_spades=1, num_keys=1, num_chests=1):
    items= (
        [Fruit() for _ in range(num_fruits)] +
        [Trap() for _ in range(num_traps)] +
        [Spade() for _ in range(num_spades)] +
        [Key() for _ in range(num_keys)] +
        [Chest() for _ in range(num_chests)]
    )

    for item in items:
        while True:
            x = random.randint(0, grid.cols-1)
            y = random.randint(0, grid.rows-1)
            if grid.is_empty(x, y):
                grid.place_item(x, y, str(item))
                break
