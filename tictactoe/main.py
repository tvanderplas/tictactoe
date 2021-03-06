
from itertools import cycle
from random import choice

class Game():

    def __init__(self):
        input('\n'.join([
            r'___________.__         ___________               ___________            ',
            r'\__    ___/|__| ____   \__    ___/____    ____   \__    ___/___   ____  ',
            r'  |    |   |  |/ ___\    |    |  \__  \ _/ ___\    |    | /  _ \_/ __ \ ',
            r'  |    |   |  \  \___    |    |   / __ \\  \___    |    |(  <_> )  ___/ ',
            r'  |____|   |__|\___  >   |____|  (____  /\___  >   |____| \____/ \___  >',
            r'                   \/                 \/     \/                      \/ ',
            '\t\tTo play, use keypad or numbers to select move.',
            '\t\t\t\t 7 | 8 | 9 ',
            '\t\t\t\t---+---+---',
            '\t\t\t\t 4 | 5 | 6 ',
            '\t\t\t\t---+---+---',
            '\t\t\t\t 1 | 2 | 3 ',
            '',
        ]))
        self.menu()

    def menu(self):
        prompt = 'Select mode:'
        print('\t1) Human vs. Human')
        print('\t2) Human vs. Computer')
        mode = input(prompt)
        while mode not in ['1', '2']:
            print('Please select 1 or 2')
            mode = input(prompt)
        if mode == '1':
            self.human()
        if mode == '2':
            self.comp_easy()


    def human(self):
        game = Tictactoe()
        while not game.is_complete:
            move = input(f"{game.turn}'s move:")
            while move not in [str(i) for i in range(1, 10)]:
                print('Please enter a valid move')
                move = input(f"{game.turn}'s move:")
            game.mark(int(move))
            print(game.view)
        print(f'{game.winner} wins!' if game.winner is not None else 'Draw!')
        again = input('Play again? (y/n):')
        while again not in ['y', 'n']:
            print('Please select y or n')
            again = input('Play again? (y/n):')
        if again == 'y':
            self.human()
        else:
            raise SystemExit


    def comp_easy(self):
        game = Tictactoe()
        while not game.is_complete:
            move = input(f"{game.turn}'s move:")
            while move not in [str(i) for i in range(1, 10)]:
                print('Please enter a valid move')
                move = input(f"{game.turn}'s move:")
            game.mark(int(move))
            game.comp_easy_move()
            print(game.view)
        print(f'{game.winner} wins!' if game.winner is not None else 'Draw!')
        again = input('Play again? (y/n):')
        while again not in ['y', 'n']:
            print('Please select y or n')
            again = input('Play again? (y/n):')
        if again == 'y':
            self.comp_easy()
        else:
            raise SystemExit


    def not_implemented(self):
        print("This mode isn't available yet!")
        print('\ty) Return to menu')
        print('\tn) Exit')
        prompt = 'Try a different one?'
        mode = input(prompt)
        while mode not in ['y', 'n']:
            print('Please select y or n')
            mode = input(prompt)
        if mode == 'y':
            self.menu()
        else:
            raise SystemExit


class Tictactoe(object):

    def __init__(self):
        self.cells = [None] + [' '] * 9
        self._turn = cycle(['X', 'O'])


    @property
    def turn(self):
        turn = next(self._turn)
        next(self._turn)
        return turn


    @property
    def is_complete(self):
        # if all cells are full
        if all([i in ['X', 'O'] for i in self.cells[1::]]):
            return True
        if self.winner is not None:
            return True
        return False


    @property
    def winner(self):
        matches = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
            [1, 4, 7],
            [2, 5, 8],
            [3, 6, 9],
            [1, 5, 9],
            [3, 5, 7],
        ]
        for match in matches:
            if all([self.cells[i] == 'O' for i in match]):
                return 'O'
            if all([self.cells[i] == 'X' for i in match]):
                return 'X'
        return None


    @property
    def view(self):
        view = '\n'.join([
            f' {self.cells[7]} | {self.cells[8]} | {self.cells[9]} ',
            '---+---+---',
            f' {self.cells[4]} | {self.cells[5]} | {self.cells[6]} ',
            '---+---+---',
            f' {self.cells[1]} | {self.cells[2]} | {self.cells[3]} ',
        ])
        return view


    def mark(self, cell:int):
        if cell not in range(1, 10):
            raise ValueError(f'expected integer 1-9, got {cell}')
        if not self.is_complete and self.cells[cell] not in ['X', 'O']:
            self.cells[cell] = next(self._turn)

    def comp_easy_move(self):
        # get empty cells
        empty_cells = [i for i, c in enumerate(self.cells) if c == ' ']
        # print(empty_cells)
        # mark one at random
        self.mark(choice(empty_cells))


if __name__ == '__main__':
    Game()
