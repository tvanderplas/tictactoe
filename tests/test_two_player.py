
import context
import tictactoe # pylint: disable=import-error
import unittest

class TwoPlayerTest(unittest.TestCase):

    def test_starting_game_gets_empty_board(self):
        empty_board = '\n'.join([
            '   |   |   ',
            '---+---+---',
            '   |   |   ',
            '---+---+---',
            '   |   |   ',
        ])
        self.assertEqual(tictactoe.Tictactoe().view, empty_board)


if __name__ == '__main__':
    unittest.main()
