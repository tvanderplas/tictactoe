
from itertools import cycle

def main():
    Game()


class Game():

    def __init__(self):
        mode = self.menu()
        if mode == 1:
            self.human()
        if mode == 2:
            self.comp_easy()


    def menu(self):
        prompt = 'Select mode:'
        print('1) Human vs. Human')
        print('2) Human vs. Computer')
        mode = input(prompt)
        while mode not in ['1', '2']:
            print('Please select 1 or 2')
            mode = input(prompt)
        return int(mode)


    def human(self):
        self.not_implemented()


    def comp_easy(self):
        self.not_implemented()


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
            self.__init__()
        else:
            raise SystemExit


class Tictactoe(object):

    def __init__(self):
        self.cells = [' '] * 9
        self.turn = cycle(['X', 'O'])


    @property
    def view(self):
        view = '\n'.join([
            f' {self.cells[6]} | {self.cells[7]} | {self.cells[8]} ',
            '---+---+---',
            f' {self.cells[3]} | {self.cells[4]} | {self.cells[5]} ',
            '---+---+---',
            f' {self.cells[0]} | {self.cells[1]} | {self.cells[2]} ',
        ])
        return view


    def mark(self, cell):
        self.cells[cell - 1] = next(self.turn)


if __name__ == '__main__':
    main()
