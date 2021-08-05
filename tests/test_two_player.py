
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


    def test_x_in_bottom_right_when_mark_one(self):
        setup = tictactoe.Tictactoe()
        setup.mark(1)
        expected = '\n'.join([
            '   |   |   ',
            '---+---+---',
            '   |   |   ',
            '---+---+---',
            ' X |   |   ',
        ])
        self.assertEqual(setup.view, expected)


    def test_x_in_bottom_right_when_mark_nine(self):
        setup = tictactoe.Tictactoe()
        setup.mark(9)
        expected = '\n'.join([
            '   |   | X ',
            '---+---+---',
            '   |   |   ',
            '---+---+---',
            '   |   |   ',
        ])
        self.assertEqual(setup.view, expected)


    def test_o_on_alternate_moves(self):
        setup = tictactoe.Tictactoe()
        setup.mark(9)
        setup.mark(7)
        setup.mark(6)
        setup.mark(4)
        expected = '\n'.join([
            ' O |   | X ',
            '---+---+---',
            ' O |   | X ',
            '---+---+---',
            '   |   |   ',
        ])
        self.assertEqual(setup.view, expected)


if __name__ == '__main__':
    unittest.main()
