import math
class Triangle:

    def __init__(self, name, a, b, c):
        self.name = name.lower().title()
        
        if a + b > c and a + c > b and b + c > a:
            self.a = float(a.replace(",", "."))
            self.b = float(b.replace(",", "."))
            self.c = float(c.replace(",", "."))
        else:
            self.a = 0
            self.b = 0
            self.c = 0


    def square_calc(self):
            half_perim = (self.a + self.b + self.c)/2
            a = self.a
            b = self.b
            c = self.c
            to_sqrt = half_perim*(half_perim-a)*(half_perim-b)*(half_perim-c)
            square = math.sqrt(to_sqrt)
            return square

        
    def to_string(self):
            return "[{0}]: {1} cm".format(self.name, round(self.square_calc(),2))


class ListOfTriangles:
    
    def __init__(self, trian):
        self.triangles = trian


    def to_string(self):
        sorting_key = Triangle.square_calc
        self.triangles = sorted(self.triangles, key = sorting_key, reverse = True)
        for triangle in self.triangles:
            print(str(self.triangles.index(triangle)+1)+". "+triangle.to_string())



class Main:
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
                list_for_sort = ListOfTriangles(list_of_triangles)
                list_for_sort.to_string()
                
            elif wishing in stop:
                print("quiting...")
                return False

                
if __name__ == '__main__':
        Main.main()
