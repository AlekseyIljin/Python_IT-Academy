class ChessDesk:
    """To draw a chess desk please provide HEIGHT<21 and WIDTH<41

    Parameters:
    height (int): total height of chessdesk
    width (int): total width of chessdesk


    Returns:
    str: your resulting chessdesk


    """

    def __init__(self, height, width):
        self.height, self.width = int(height), int(width)
        self.width_limit = 41
        self.height_limit = 21

    def draw(self):
        if self.height < self.height_limit and self.width < self.width_limit:
            for i in range(self.height_limit + 1):
                if i % 2 == 1:
                    print("* " * self.width)
                else:
                    print(" *" * self.width)
        else:
            raise ValueError


def main():
    while True:
        try:
            height = input("Enter height: ")
            width = input("Enter width: ")
            test = ChessDesk(height, width)
            test.draw()
        except ValueError:
            print(ChessDesk.__doc__)


if __name__ == '__main__':
    main()
