class Fibonacci:
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

    def presentation(self):
        return "".join(str(self.fib_list))\
            .replace("[","")\
            .replace("]","")


if __name__ == '__main__':
    start = input("Enter the start value: ")
    end = input("Enter the end for sequence: ")
    try:
        if int(start) > 0 and int(start) > 0:
            test = Fibonacci(int(start), int(end))
            test.fib_seq()
            print(test.presentation())
        else:
            raise ValueError
    except:
        print("Enter positive values, which are digits!")

