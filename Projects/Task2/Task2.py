import math
class Envelope():
    def __init__(self, a, b):
        self.a= int(a)
        self.b= int(b)

    def comparation(self, envelope):
        side_A = self.a
        side_B = self.b
        side_C = envelope.a
        side_D = envelope.b
        diagonal_of_secondary_envelope = math.sqrt(side_C**2 + side_D**2)
        
        if side_A > side_C and side_B > side_D:
            return "You could put that Envelope inside"
        elif side_A > side_D and side_B > side_C:
            return "Rotate your Envelope at 90 dergrees and put inside"
        elif (side_A > side_C and side_B < side_D)\
             or (side_A < side_D and side_B > side_C):
            if diagonal_of_secondary_envelope < side_A and side_B:
                return "Somehow you can put it in of course, but be careful in future"
            else:
                return "No, you can't put that envelope inside, try another one"
        elif (side_A == side_C and side_B == side_D)\
             or (side_A == side_D and side_B == side_C):
            return "They are equal. Try again"
        else:
            return "You can't put inside that envelope"
                    

class Main:
    def main():
        while True:
            decision = input("Would you like to compare envelopes?\n")
            agreeing = ("y", "yes", "yep")
            denying = ("no","nope","n", "q", "exit", "quit")
            if decision in agreeing:
                a = input("Side a = ")
                b = input("Side b = ")
                c = input("Side c = ")
                d = input("Side d = ")
                
                first_envelope = Envelope(a,b)
                second_envelope = Envelope(c,d)
                print(first_envelope.comparation(second_envelope))
            elif decision in denying:
                print("quiting...")
                return False
        
if __name__ == '__main__':
    
        Main.main()
                   
