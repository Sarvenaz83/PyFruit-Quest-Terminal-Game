ROWS = 12
COLS = 36
INITIAL_SCORE = 100
GRACE_STEPS = 5
BOMB_DELAY = 3
ENEMY_COUNT = 3
MIN_ENEMY_DISTANCE = 5

SYMBOLS = {
    'player': '◎',
    'wall': '■',
    'fruit': 'F',
    'trap': '⚡',
    'spade': '⛏',
    'key': '🔑',
    'chest': '📦',
    'exit': '🚪',
    'enemy': '👾',
    'bomb': '💣',
    'empty': ' '
}

TRAP_PENALTY = -10
ENEMY_PENALTY = -20
FRUIT_VALUE = 20
CHEST_VALUE = 100

WIN_MESSAGE = "Congratulations! You won!"
LOSE_MESSAGE = "Game Over! you lost!"