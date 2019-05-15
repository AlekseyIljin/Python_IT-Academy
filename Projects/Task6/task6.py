class LuckyTicket:
    def __init__(self, ticket):
        self.ticket = str(ticket)
        


    def piter(self):
        sum_even = 0
        sum_odd = 0
        for num in self.ticket:
            if int(num) % 2 == 1:
                sum_odd += int(num)
            else:
                sum_even += int(num)

        
        if sum_even == sum_odd:
            return "Lucky ticket!"
        else:
            return "Not lucky ticket"

        
    def moscow(self):
        sum_first = 0
        sum_second = 0
        print(self.ticket[:3])
        for num in self.ticket[:3]:
            sum_first += int(num)
        for num in self.ticket[3:]:
            sum_second += int(num)

        if sum_first == sum_second:
            return "Lucky ticket!"
        else:
            return "Not lucky ticket"

if __name__ == '__main__':
    ticket = LuckyTicket(876678)
    print(ticket.piter())
    print(ticket.moscow())
                
