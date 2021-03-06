import math


class Triangle:

    def __init__(self, name, a, b, c):
        self.name = name.lower().title()
        self.a = int(a)
        self.b = int(b)
        self.c = int(c)
        self.square = 0

    def square_calc(self):
        half_perim = (self.a + self.b + self.c) / 2
        to_sqrt = half_perim \
                  * (half_perim - self.a) \
                  * (half_perim - self.b) \
                  * (half_perim - self.c)
        self.square = round(math.sqrt(to_sqrt), 2)
        return self.square

    def __str__(self):
        return "[{0}]: {1} cm".format(self.name, self.square)


def main():
    list_of_triangles = []

    while True:
        wishing = input("Would you like to add a new triangle? [y/n]\n")
        agreeing = ("y", "yes", "yep")
        dening = ("n", "no", "nope")
        stop = ("q", "quit", "stop", "exit")

        if wishing.lower() in agreeing:
            name = input("Name of Triangle is?\n")
            sidea = input("a = ")
            sideb = input("b = ")
            sidec = input("c = ")
            try:
                a = float(sidea.replace(",", "."))
                b = float(sideb.replace(",", "."))
                c = float(sidec.replace(",", "."))
                if a + b > c and b + c > a and a + c > b:
                    triangle = Triangle(name, sidea, sideb, sidec)
                    triangle.square_calc()
                    list_of_triangles.append(triangle)
                else:
                    raise TypeError
            except ValueError:
                print("Invalid data type")
            except TypeError:
                print("Triangle '{}' can't exist".format(name))

        elif wishing in dening:
            if len(list_of_triangles) != 0:

                print("=" * 15 + "Triangle List" + "=" * 15 + "\n")
                list_of_triangles = sorted(list_of_triangles, key=lambda x: x.square, reverse=True)
                for triangle in list_of_triangles:
                    print(str(list_of_triangles.index(triangle) + 1) + ". " + str(triangle))
            else:
                print("Empty list")

        elif wishing in stop:
            print("quiting...")
            return False


if __name__ == '__main__':
    main()
