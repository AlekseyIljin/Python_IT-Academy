class Fibonachi:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.fib_list = []

    def fib_seq(self):
        element = 0
        next = 1
        while element < self.end:
            if  element > self.start:
                self.fib_list.append(element)
            element, next = next, element + next


    def __str__(self):
        print(self.fib_list)

if __name__ == '__main__':
    test = Fibonachi(44, 250)
    test.fib_seq()
    test.__str__()
