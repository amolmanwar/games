"""A module that implements the snake n ladder board of size 100 """


import random
from dataclasses import dataclass
from snake_n_ladder.constants import BoardMeta, Ladders, Snakes, PlayerStatus, \
    StandardDice, DiceType, GreenSnakes
from snake_n_ladder.exception import PlayerException, LadderException, \
    SnakeException, DiceException


@dataclass
class Player:
    """A dataclass that represents the player details"""
    def __init__(self, name, cell=None, status=None, green_snake_bites={}):
        """A player initializer that initializes the player

        :param name: name of a player
        :type name: str
        :param cell: current position/cell of a player, defaults to None
        :type cell: Cell(dataclass), optional
        :param status: status - (PLAYING|WAITING_FOR_DICE|WINNER|LOOSER)
        :type status: str, optional
        """
        self.name = name
        self.cell = cell
        self.status = status
        self.green_snake_bites = green_snake_bites


@dataclass
class Cell:
    """A dataclass cell representing the current step, ladder-top, snake-tail
       and the player's position holding the cell
    """
    def __init__(self, current_step, ladder_top=None,
                 snake_tail=None, snake_type="Normal"):
        """A cell initializer on the board

        :param current_step: current position or the current step
                             representing the cell number
        :type current_step: int
        :param ladder_top: top of the ladder, defaults to None
        :type ladder_top: int, optional
        :param snake_tail: tail of the snake, defaults to None
        :type snake_tail: int, optional
        """
        self.current_step = current_step
        self.snake_tail = snake_tail
        self.ladder_top = ladder_top
        self.snake_type = snake_type


class Board:
    """A board that represents the snake and ladder to play """
    def __init__(self, dice=None):
        """A board initializer that initializes the snake and ladder board

        :param dice: type of dice NORMAL|CROOKED, defaults to None
        :type dice: str, optional
        """
        self.players = []
        self.board = self.construct_board()
        self.start = self.board[0]
        self.end = self.board[-1]
        self.dice = dice

    def construct_board(self):
        """A method that constructs the snake and ladder board and adds ladder
           and snakes

        :return: list of cells starting off with 1 to 100
        :rtype: list
        """
        board = []
        for cell_number in range(1, BoardMeta.SIZE.value + 1):
            cell = Cell(cell_number)
            board.append(cell)
        # add ladders
        self.add_ladders(board)
        # add snakes
        self.add_snakes(board)
        self.add_green_snakes(board)
        return board

    def create_players(self, players=None):
        """A method that creates the players

        :param players: list of player names, defaults to []
        :type players: list, optional
        :return: list of players
        :rtype: list
        """
        if not players or not isinstance(players, list):
            msg = "Player names can not be empty"
            raise PlayerException(error_message=msg)
        for name in players:
            green_snake_bites = {}
            for snake in GreenSnakes.SNAKES.value:
                green_snake_bites[snake[0]-1] = False
            player = Player(name, cell=self.start, status=PlayerStatus.
                            WAITING_FOR_DICE.value, green_snake_bites=green_snake_bites)
            self.players.append(player)
        return self.players

    @staticmethod
    def add_ladders(board):
        """A method to add ladders on the board

        :param board: a list of cells representing the entire board
        :type board: list
        """
        if not board:
            msg = "board can be empty"
            raise LadderException(error_message=msg)
        for ladder in Ladders.LADDERS.value:
            cell = board[ladder[0]-1]
            cell.ladder_top = ladder[1]

    @staticmethod
    def add_snakes(board):
        """A method to add snakes on the board

        :param board: a list of cells representing the entire board
        :type board: list
        """
        if not board:
            msg = "board can be empty"
            raise SnakeException(error_message=msg)
        for snake in Snakes.SNAKES.value:
            cell = board[snake[0]-1]
            cell.snake_tail = snake[1]

    @staticmethod
    def add_green_snakes(board):
        for snake in GreenSnakes.SNAKES.value:
            cell = board[snake[0]-1]
            cell.snake_tail = snake[1]
            cell.snake_type = "GREEN"

    def play_dice(self):
        """A player throws a dice and returns random number based
           on the tuype of dice

        :return: number
        :rtype: int
        """
        if self.dice == DiceType.NORMAL.value:
            number = random.randint(StandardDice.MIN_NUMBER.value,
                                    StandardDice.MAX_NUMBER.value)
        elif self.dice == DiceType.CROOKED.value:
            number = random.randrange(StandardDice.CROOKED_MIN_NUMBER.value,
                                      StandardDice.CROOKED_MAX_NUMBER.value,
                                      StandardDice.CROOKED_STEP.value)
        else:
            msg = "{} invalid dice type".format(self.dice)
            raise DiceException(error_message=msg)
        return number

    def move_player_step(self, player, number):
        """A method that moves the player step by a number thrown by a dice

        :param player: an instance of Player dataclass representing a player
        :type player: Player
        :param number: A number thrown by a dice
        :type number: int
        :return: the updated player details
        :rtype: Player
        """
        if not player or not isinstance(player, Player):
            msg = "Player can not be empty and must be an instance of Player"
            raise PlayerException(error_message=msg)
        if number not in range(1, 7):
            raise PlayerException("Invalid number!! Player exception")

        # Note: This can be moved to decorators as improvement
        # Decorators such as move_by_ladder, slip_by_snake_bite, is_winner etc
        current_step = player.cell.current_step
        next_step = current_step + number
        # check if player has reached to 100
        if next_step >= self.end.current_step:
            # player is winner
            player.status = PlayerStatus.WINNER.value
            player.cell = self.end
            return player
        # calculate the new cell as per the move
        new_cell = self.board[next_step-1]
        # check if the new cell has ladder
        if new_cell.ladder_top:
            player.cell = self.board[new_cell.ladder_top - 1]
            return player
        # check if new cell has a snake bite
        if new_cell.snake_tail:
            if new_cell.snake_type == "GREEN":
                is_snake_bite = player.green_snake_bites.get(new_cell.current_step)
                if is_snake_bite:
                    player.cell = new_cell
                    player.green_snake_bites.update({new_cell.current_step: True})
                    return player
            player.cell = self.board[new_cell.snake_tail - 1]
            return player
        # otherwise return the normal next new cell
        player.cell = new_cell
        return player

    def print_board(self):
        """A print utility that prints the list of cells on the board
           representing the cells, snakes and ladder
        """
        for cell in self.board:
            print("current step: {}, ladder top: {}, snake_tail: {}".
                  format(cell.current_step, cell.ladder_top, cell.snake_tail))
