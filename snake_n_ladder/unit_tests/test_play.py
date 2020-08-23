"""An unit testing module to test play class """

import builtins
from unittest.mock import MagicMock
import unittest2
from mock import patch, Mock
from snake_n_ladder.play import PlaySnakeNLadder
from snake_n_ladder.exception import DiceException
from snake_n_ladder.board import Board


class TestPlay(unittest2.TestCase):
    """A class to test play class """
    def setUp(self):
        """A setup method to instantiate PlaySnakeNLadder """
        self.play = PlaySnakeNLadder()

    def test_play_game_on_invalid_dice_type_choice(self):
        """Test - play game on invalid dice type choice """
        # invalid dice with choice input as 3
        mock = MagicMock(return_value=3)
        builtins.input = mock
        exit_code = self.play.play()
        assert exit_code == 1

    def test_play_game_on_invalid_dice_type_error(self):
        """Test - play game on invalid dice type error """
        # invalid dice with choice input as 3
        mock = MagicMock(return_value="fgg")
        builtins.input = mock
        exit_code = self.play.play()
        assert exit_code == 1

    @patch("builtins.input", side_effect=[1, "sdgfgf"])
    def test_play_game_on_invalid_no_of_players(self, mock_input):
        """Test - Play game on invalid no of players """
        _ = mock_input
        exit_code = self.play.play()
        assert exit_code == 1

    @patch("builtins.input", side_effect=[1, 1, "Amol"]*100)
    def test_play_game_on_success_with_normal_dice(self, mock_input):
        """Test - play game on success """
        _ = mock_input
        exit_code = self.play.play()
        assert exit_code == 0

    @patch("builtins.input", side_effect=[2, 1, "Amol"]*100)
    def test_play_game_on_success_with_crooked_dice(self, mock_input):
        """Test - play game on success """
        _ = mock_input
        exit_code = self.play.play()
        assert exit_code == 0
        assert str(self.play)

    @patch("builtins.input", side_effect=[2, 1, "Amol"]*100)
    def test_exception(self, mock_input):
        """Test - exception """
        _ = mock_input
        mock = Mock(side_effect=DiceException("fake"))
        play_dice = Board.play_dice
        Board.play_dice = mock
        self.play.play()
        Board.play_dice = play_dice
