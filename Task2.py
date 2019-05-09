import math
class Envelope():
    def __init__(self, a, b):
        self.a= a
        self.b= b
        self.perimetr = self.a*2 + self.b*2

    def comparation(self, envelope):
        p1 = self.perimetr
        p2 = envelope.perimetr
        side_A = self.a
        side_B = self.b
        side_C = envelope.a
        side_D = envelope.b
        diagonal_of_secondary_envelope = math.sqrt(side_C**2 + side_D**2)
        if p1 > p2:
            if side_A > side_C and side_B > side_D:
                print("You could put that Envelope inside")
            elif side_A > side_D and side_B > side_C:
                print("Rotate your Envelope at 90 dergrees and put inside")
            elif (side_A > side_C and side_B < side_D)\
                 or (side_A < side_D and side_B > side_C):
                if diagonal_of_secondary_envelope < side_A and side_B:
                    print("Somehow you can put it in of course, but be careful in future")
                else:
                    print("No, you can't put that envelope inside, try another one")
        elif p1==p2:
            print("They are the equal")
        else:
            print("You can't put inside that envelope")
                    

class Main():
    def __init__(self):
        pass
    
    def main():
        first_envelope = Envelope(7,3)
        second_envelope = Envelope(7,3)

        print(first_envelope.perimetr)
        print(second_envelope.perimetr)

        first_envelope.comparation(second_envelope)

if __name__ == '__main__':
    try:
        x = Main.main()
    except KeyboardInterrupt:
        exit()
