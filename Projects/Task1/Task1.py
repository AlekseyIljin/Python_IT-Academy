class ChessDesk:

    def __init__(self, height = None, width = None):
        self.height, self.width = height, width


    def draw(self):
        """To draw a chess desk please provide HEIGHT and WIDTH
        
Now restart an app and input the required variables
        """
        width_limit = 41
        heigth_limit = 21
        if self.height < heigth_limit and self.width < width_limit:
            counter = 1
            while counter < self.height + 1:
                if counter % 2 == 1:
                    print("* "*self.width)
                    counter += 1
                else:
                    print(" *"*self.width)
                    counter += 1
        else:
            print("Symbol limit has reached")
            
            
            
if __name__ == '__main__':
    test = ChessDesk(20,40)
        if test.width and test.height:
            test.draw()
        else:
            print(test.draw.__doc__)
