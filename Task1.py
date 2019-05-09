class ChessDesk():

    def __init__(self, height = None, width = None):
        self.width = width
        self.height = height


    def draw(self):
        """To draw a chess desk please provide HEIGHT and WIDTH
        
Now restart an app and input the required variables
        """
        if self.width < 41 and self.height < 21:
            counter = 1
            while counter < self.height + 1:
                if counter%2==1:
                    print("* "*self.width)
                    counter += 1
                else:
                    print(" *"*self.width)
                    counter += 1
        else:
            print("Symbol limit has reached")

class Main():
    def __init__(self):
        pass
    
    def main():
        test = ChessDesk()
        if test.width and test.height:
            test.draw()
        else:
            print(test.draw.__doc__)

            
            
            
if __name__ == '__main__':
    try:
        x = Main.main()
    except KeyboardInterrupt:
        exit()
