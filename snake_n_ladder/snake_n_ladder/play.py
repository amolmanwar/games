"""A main module that runs the game by taking the input from
   player to begin the game """

import inflect
from snake_n_ladder.board import Board

from snake_n_ladder.constants import PlayerStatus, DiceType
from snake_n_ladder.exception import LadderException, SnakeException, \
    PlayerException, DiceException, GameException


class PlaySnakeNLadder:
    """A main class to start the game
    """
    name = "PlaySnakeNLadder"

    def __init__(self):
        self.board = None
        self.dice = None
        self.number_of_players = None
        self.players = []

    def __str__(self):
        """string representation """
        return self.name

    class InputValidator:
        """A static Input validator class """
        @staticmethod
        def input_dice_type(func):
            """A decorator function to validate dice type """
            def wrapper(cls, *args, **kwargs):
                try:
                    # select the dice type
                    print("1: Normal Dice\n2: Crooked Dice\n")
                    cls.dice = input("Select the dice ")
                    if int(cls.dice) == 1:
                        # instantiate board with normal dice
                        cls.board = Board(dice=DiceType.NORMAL.value)
                    elif int(cls.dice) == 2:
                        # instantiate board with crooked dice
                        cls.board = Board(dice=DiceType.CROOKED.value)
                    # input the number of players
                    else:
                        msg = "Dice must be of type Normal|CROOKED"
                        print(msg)
                        return 1
                    return func(cls, *args, **kwargs)
                except ValueError as _:
                    print("Please input valid choice for the dice ")
                    return 1
            return wrapper

        @staticmethod
        def input_players(func):
            """A  decorator function to validate players input """
            def wrapper(cls, *args, **kwargs):
                try:
                    cls.number_of_players = input("Enter number of players ")
                    players = []
                    for number in range(int(cls.number_of_players)):
                        name = input("Enter the name of {} player ".
                                     format(inflect.engine().
                                            ordinal(number+1)))
                        players.append(name)
                        # instantiate players on the board
                    cls.players = cls.board.create_players(players)
                    return func(cls, *args, **kwargs)
                except ValueError as _:
                    print("Enter valid number of players...")
                    return 1
            return wrapper

    @InputValidator.input_dice_type
    @InputValidator.input_players
    def play(self):
        """A method that accepts the input from player and begins the game
           until one of the player becomes the winner
        """
        try:
            # play the game until the player reaches to 100
            print("\nStarting a game with players: {}".
                  format(" ".join([player.name for player in self.players])))
            while True:
                # pop the player from the list and throw a dice
                # one by one in FIFO fashion
                player = self.board.players.pop(0)
                input("\n{} Hit enter to throw a dice ".format(player.name))
                dice_number = self.board.play_dice()
                print("{} got {} on the dice".format(player.name, dice_number))
                # move a player by number
                player = self.board.move_player_step(player, dice_number)
                # dismiss the game if player is a winner
                if player.status == PlayerStatus.WINNER.value:
                    print("Congratulation: {}!!. You are the winner ".
                          format(player.name))
                    break
                # update player status and add a player into the queue
                player.status = PlayerStatus.WAITING_FOR_DICE.value
                self.board.players.append(player)
                print("{} you are at current cell: {}".
                      format(player.name, player.cell.current_step))
        except (LadderException, SnakeException, DiceException,
                PlayerException, GameException) as error:
            print(error.error_message)
            return 1
        return 0
