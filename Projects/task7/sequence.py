class SequenceAnalize:
    def __init__(self, n):
        self.n = n
        self.row = []

    def calc_sequence(self):
        counter = 0
        squad = 0
        while squad < self.n:
            self.row.append(str(counter))
            counter += 1
            squad = counter ** 2

    def presentation(self):
        return ", ".join(self.row)


if __name__ == '__main__':
    try:
        limit = input("Please enter the limit for the natural sequence:\n")
        seq = SequenceAnalize(int(limit))
        seq.calc_sequence()
        print(seq.presentation())
    except:
        print("Invalid data, inter not symbols")
