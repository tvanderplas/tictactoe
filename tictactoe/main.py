
def main():
    Game()


class Game():

    def __init__(self):
        self.menu()


    def menu(self):
        prompt = 'Select mode:'
        print('1) Human vs. Human')
        print('2) Human vs. Computer')
        mode = input(prompt)
        while mode not in ['1', '2']:
            print('Please select 1 or 2')
            mode = input(prompt)
        return int(mode)


if __name__ == '__main__':
    main()
