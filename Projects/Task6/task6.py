class LuckyTicket:
    def __init__(self, mode = 'piter'):
        self.mode = mode
        self.counter = 0
        
    def read_file(self, url):
        file = open(url)
        for line in file:
            if self.mode == 'piter':
                self.piter(line.rstrip())
            elif self.mode == 'moscow':
                self.moscow(line.rstrip())
        file.close()
        return "Count of lucky tickets = " + str(self.counter)

    def piter(self, number):
        even_list = number[1::2]
        odd_list = number[0::2]
        sum_even = 0
        sum_odd = 0

        for num in even_list:
            sum_even += int(num)

        for num in odd_list:
            sum_odd += int(num)

        if sum_even == sum_odd:
            self.counter += 1

        else:
            pass

        
    def moscow(self, number):
        sum_first = 0
        sum_second = 0
        for num in number[:3]:
            sum_first += int(num)
        for num in number[3:]:
            sum_second += int(num)

        if sum_first == sum_second:
            self.counter += 1

        else:
            pass

class Main:
    def main():
        mode = input("Choose mode [moscow/piter]\n")
        ticket = LuckyTicket(mode.lower())
        url = input("Enter path to file with tickets\n")
        print(ticket.read_file(url))

if __name__ == '__main__':
    Main.main()
