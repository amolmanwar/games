"""A module to test snake and ladder board functionality """

import unittest2

from snake_n_ladder.board import Board
from snake_n_ladder.constants import DiceType, BoardMeta
from snake_n_ladder.exception import PlayerException, LadderException, \
    SnakeException, DiceException
from snake_n_ladder.board import Player
from snake_n_ladder.constants import Ladders, PlayerStatus


class TestBoard(unittest2.TestCase):
    """A test module to test snake and ladder board """
    def setUp(self):
        """A setup method to instantiate test objects """
        self.snake_n_ladder_board = Board(dice=DiceType.NORMAL.value)
        self.players = ["amol", "paras"]
        self.snake_n_ladder_board.create_players(self.players)

    def tearDown(self):
        """A tear down method to tear down the instantiated objects """

    def test_construct_board_on_success(self):
        """Test - construct board on success"""
        board = self.snake_n_ladder_board.construct_board()
        assert isinstance(board, list)
        assert len(board) == BoardMeta.END.value

    def test_create_players_on_input_error(self):
        """Test - create players on the board on input error """
        self.snake_n_ladder_board = Board(dice=DiceType.NORMAL.value)
        players = []
        self.assertRaises(PlayerException, self.snake_n_ladder_board.
                          create_players, players)

    def test_create_players_on_success(self):
        """Test - create players on board on success case """
        snake_n_ladder_board = Board(dice=DiceType.CROOKED.value)
        players = snake_n_ladder_board.create_players(self.players)
        assert isinstance(players, list)
        assert len(players) == 2
        for player in players:
            assert isinstance(player, Player)

    def test_add_ladders_on_board_on_error(self):
        """Test - add ladders on board on error """
        board = None
        self.assertRaises(LadderException, self.snake_n_ladder_board.
                          add_ladders, board)
        assert str(LadderException())

    def test_add_ladders_on_board_on_success(self):
        """Test - add ladders on board on success """
        self.snake_n_ladder_board.add_ladders(self.snake_n_ladder_board.board)
        for ladder in Ladders.LADDERS.value:
            print(ladder[0])
            assert (self.snake_n_ladder_board.board[ladder[0]-1].
                    ladder_top == ladder[1])

    def test_add_snake_on_board_on_error(self):
        """Test - add snake on board on error """
        board = None
        self.assertRaises(SnakeException, self.snake_n_ladder_board.add_snakes,
                          board)

    def test_add_snake_on_board_on_success(self):
        """Test - add snake on board on success """
        self.snake_n_ladder_board.add_snakes(self.snake_n_ladder_board.board)
        for ladder in Ladders.LADDERS.value:
            print(ladder[0])
            assert (self.snake_n_ladder_board.board[ladder[0]-1].
                    ladder_top == ladder[1])

    def test_play_dice_on_invalid_dice_type_error(self):
        """Test - play dice on invalid dice type error """
        snake_n_ladder_board = Board(dice="OddDice")
        self.assertRaises(DiceException, snake_n_ladder_board.play_dice)

    def test_play_dice_on_normal_dice_type_on_success(self):
        """Test - play dice on normal dice type on success """
        number = self.snake_n_ladder_board.play_dice()
        assert number in range(1, 7)

    def test_play_dice_on_crooked_dice_type_on_success(self):
        """Test - play dice on croked dice type on success """
        snake_n_ladder_board = Board(dice=DiceType.CROOKED.value)
        _ = snake_n_ladder_board.create_players(self.players)
        number = snake_n_ladder_board.play_dice()
        assert number in range(2, 8, 2)

    def test_move_player_step_on_invalid_player_error(self):
        """Test - move player step on invalid player error """
        player = None
        number = 2
        self.assertRaises(PlayerException,
                          self.snake_n_ladder_board.move_player_step,
                          player, number)

    def test_move_player_step_on_invalid_number_error(self):
        """Test - move player step on invalid number error """
        player = self.snake_n_ladder_board.players[0]
        number = 7
        self.assertRaises(PlayerException,
                          self.snake_n_ladder_board.move_player_step,
                          player, number)

    def test_move_player_step_on_normal_move(self):
        """Test - move player step on normal move """
        player = self.snake_n_ladder_board.players[0]
        number = 2
        player = self.snake_n_ladder_board.move_player_step(player, number)
        assert player.cell.current_step == 3

    def test_move_player_step_on_ladder_move(self):
        """Test - move player step on ladder move """
        player = self.snake_n_ladder_board.players[0]
        number = 3
        player = self.snake_n_ladder_board.move_player_step(player, number)
        assert player.cell.current_step == 25

    def test_move_player_step_on_snake_tail(self):
        """Test - move player step on snake tail """
        player = self.snake_n_ladder_board.players[0]
        player.cell.current_step = 12
        print(player.cell.current_step)
        number = 2
        player = self.snake_n_ladder_board.move_player_step(player, number)
        assert player.cell.current_step == 7

    def test_move_player_step_on_winner(self):
        """Test - move player step on winner """
        player = self.snake_n_ladder_board.players[0]
        player.cell.current_step = 98
        print(player.cell.current_step)
        number = 2
        player = self.snake_n_ladder_board.move_player_step(player, number)
        assert player.cell.current_step == 100
        assert player.status == PlayerStatus.WINNER.value

    def test_print_board(self):
        """Test - print board on success """
        self.snake_n_ladder_board.create_players(["amol", "paras"])
        self.snake_n_ladder_board.print_board()
