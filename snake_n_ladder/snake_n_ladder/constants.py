"""A module that holds the constants required for snake n ladder """

from enum import Enum


class BoardMeta(Enum):
    """An enum to represent the constants for board """
    SIZE = 100
    START = 1
    END = 100
    TOTAL_TURNS = 10


class Ladders(Enum):
    """An enum to represent the ladders on the board """
    LADDER1 = (4, 25)
    LADDER2 = (10, 40)
    LADDER3 = (45, 65)
    LADDER4 = (75, 90)
    LADDER5 = (28, 58)

    LADDERS = [LADDER1, LADDER2, LADDER3, LADDER4, LADDER5]


class Snakes(Enum):
    """An enum to represent the snakes on the board """
    SNAKE1 = (14, 7)
    SNAKE2 = (20, 5)
    SNAKE3 = (35, 4)
    SNAKE4 = (65, 35)

    SNAKES = [SNAKE1, SNAKE2, SNAKE3, SNAKE4]


class GreenSnakes(Enum):
    SNAKE1 = (31, 11) # 29
    SNAKE2 = (21, 6)

    SNAKES = [SNAKE1, SNAKE2]


class PlayerStatus(Enum):
    """An enum to represent the status of the players """
    ACTIVE = "PLAYING"
    WAITING_FOR_DICE = "WAITING_FOR_DICE"
    WINNER = "WINNER"
    LOSSER = "LOSSER"


class StandardDice(Enum):
    """An enum to repesent the standard dice """
    MIN_NUMBER = 1
    MAX_NUMBER = 6
    CROOKED_MIN_NUMBER = 2
    CROOKED_MAX_NUMBER = 8
    CROOKED_STEP = 2


class DiceType(Enum):
    """An enum to represent the dice type """
    NORMAL = "NORMAL"
    CROOKED = "CROOKED"
