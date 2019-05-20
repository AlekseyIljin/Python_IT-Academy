import math

class Triangle:

    def __init__(self, name, a, b, c):
        self.name = name.lower().title()
        a = float(a.replace(",", "."))
        b = float(b.replace(",", "."))
        c = float(c.replace(",", "."))
        
        if a + b > c and a + c > b and b + c > a:
            self.a = a
            self.b = b
            self.c = c
        else:
            return "Invalid data"

    def square_calc(self):
            half_perim = (self.a + self.b + self.c)/2
            to_sqrt = half_perim\
                      *(half_perim-self.a)\
                      *(half_perim-self.b)\
                      *(half_perim-self.c)
            square = math.sqrt(to_sqrt)
            return square

        
    def __str__(self):
            return "[{0}]: {1} cm".format(self.name, round(self.square_calc(),2))



def main():
    list_of_triangles = []

    while True:
        wishing = input("Would you like to add a new triangle? [y/n]\n")
        agreeing = ("y","yes","yep")
        dening = ("n", "no", "nope")
        stop = ("q", "quit", "stop", "exit")

        if wishing.lower() in agreeing:
            name = input("Name of Triangle is?\n")

            if name.lower in stop:
                print("quiting...")
                return False

            else:
                sidea = input("a = ")
                sideb = input("b = ")
                sidec = input("c = ")
                triangle = Triangle(name, sidea, sideb, sidec)
                list_of_triangles.append(triangle)

        elif wishing in dening:
            print("="*15 + "Triangle List" + "="*15 + "\n")
            sorting_key = Triangle.square_calc
            list_of_triangles = sorted(list_of_triangles, key=sorting_key, reverse=True)
            for triangle in list_of_triangles:
                print(str(list_of_triangles.index(triangle) + 1) + ". " + triangle.__str__())

        elif wishing in stop:
            print("quiting...")
            return False

                
if __name__ == '__main__':
        main()
