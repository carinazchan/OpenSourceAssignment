import unittest
from unittest.mock import MagicMock, patch
from tic_tac_toe import TicTacToeGame, TicTacToeBoard, Player, Move


class TestTicTacToe(unittest.TestCase):
    def setUp(self):
        self.players = (
            Player(label="X", color="blue"),
            Player(label="O", color="green")
        )
        self.game = TicTacToeGame(players=self.players)

    def test_initialization(self):
        self.assertEqual(self.game.board_size, 3)
        self.assertEqual(self.game.current_player, self.players[0])
        self.assertFalse(self.game.has_winner())
        self.assertFalse(self.game.is_tied())

    def test_valid_move(self):
        move = Move(row=0, col=0)
        self.assertTrue(self.game.is_valid_move(move))

    def test_process_move(self):
        move = Move(row=0, col=0, label=self.players[0].label)
        self.game.process_move(move)
        self.assertFalse(self.game.has_winner())
        self.assertFalse(self.game.is_tied())

    def test_toggle_player(self):
        current_player = self.game.current_player
        self.game.toggle_player()
        self.assertNotEqual(current_player, self.game.current_player)

    def test_reset_game(self):
        self.game.process_move(Move(row=0, col=0, label=self.players[0].label))
        self.game.reset_game()
        self.assertFalse(self.game.has_winner())
        self.assertFalse(self.game.is_tied())
        self.assertEqual(self.game.current_player, self.players[0])


class TestTicTacToeBoard(unittest.TestCase):
    def setUp(self):
        self.game_mock = MagicMock(spec=TicTacToeGame)
        self.game_mock.board_size = 3
        self.game_mock.current_player = Player(label="X", color="blue")
        self.board = TicTacToeBoard(self.game_mock)

    def test_update_button(self):
        with patch('tkinter.Button') as button_mock:
            self.board._update_button(button_mock)
            button_mock.config.assert_called_once_with(
                text=self.board._game.current_player.label,
                fg=self.board._game.current_player.color
            )


def test_update_display(self):
    with patch.object(self.board.display, 'config') as config_mock:
        self.board._update_display("Test Message", "red")
        print(config_mock.call_args_list)
        config_mock.assert_called_once_with(text="Test Message", fg="red")


if __name__ == '__main__':
    unittest.main()
