
def main():
    Game()


class Game():

    def __init__(self):
        self.menu()


    def menu(self):
        print('1) Human vs. Human')
        print('2) Human vs. Computer')
        mode = input('Select mode:')
        while mode not in ['1', '2']:
            print('Please select 1 or 2')
            mode = input('Select mode')
        return int(mode)


if __name__ == '__main__':
    main()
