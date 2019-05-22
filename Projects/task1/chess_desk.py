class ChessDesk:

    def __init__(self, height, width):
        self.height, self.width = int(height), int(width)
        self.width_limit = 41
        self.height_limit = 21

    def draw(self):
        """To draw a chess desk please provide HEIGHT<21 and WIDTH<41


        Parameters:
        heigth (int): total heigth of chessdesk
        width (int): total width of chessdesk


        Returns:
        str: your resulting chessdesk


        """

        if self.height < self.height_limit and self.width < self.width_limit:
            counter = 1
            while counter < self.height + 1:
                if counter % 2 == 1:
                    print("* " * self.width)
                    counter += 1
                else:
                    print(" *" * self.width)
                    counter += 1
        else:
            raise ValueError("Symbol limit has reached")


def main():
    while True:
        height = input("enter heigth: ")
        width = input("enter width: ")
        test = ChessDesk(height, width)
        try:
            test.draw()
        except:
            print(test.draw.__doc__)


if __name__ == '__main__':
    main()