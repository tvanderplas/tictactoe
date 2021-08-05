
import context
import tictactoe # pylint: disable=import-error
import unittest

class TwoPlayerTest(unittest.TestCase):

    def test_starting_game_gets_empty_board(self):
        expected = '\n'.join([
            '   |   |   ',
            '---+---+---',
            '   |   |   ',
            '---+---+---',
            '   |   |   ',
        ])
        self.assertEqual(tictactoe.Tictactoe().view, expected)


if __name__ == '__main__':
    unittest.main()
