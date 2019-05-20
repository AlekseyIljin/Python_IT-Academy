import re


class Digit:
    def __init__(self, number):
        self.number = int(number)

        self.units = {0: "", 1: "Один", 2: "Два", 3: "Три", 4: "Четыре",
                      5: "Пять", 6: "Шесть", 7: "Семь", 8: "Восемь", 9: "Девять"}

        self.teens = {10: "Десять", 11: "Одинадцать", 12: "Двенадцать",
                      13: "Тринадцать", 14: "Четырнадцать", 15: "Пятнадцать",
                      16: "Шестнадцать", 17: "Семнадцать", 18: "Восемнадцать",
                      19: "Девятнадцать"}

        self.tens = {0: "", 2: "Двадцать", 3: "Тридцать", 4: "Сорок",
                     5: "Пятьдесять", 6: "Шестьдесят", 7: "Семдесят",
                     8: "Восемдесять", 9: "Девяносто"}

        self.hundreds = {0: "", 1: "Сто", 2: "Двести", 3: "Триста", 4: "Четыреста",
                         5: "Пятьсот", 6: "Шестьсот", 7: "Семьсот",
                         8: "Восемьсот", 9: "Девятьсот"}

        self.thousands = {0: "", 1: "Одна тысяча", 2: "Две тысячи", 3: "Три тысячи",
                          4: "Четыре тысячи", 5: "Пять тысяч", 6: "Шесть тысяч",
                          7: "Семь тысяч", 8: "Восемь тысяч", 9: "Девять тысяч"}

        self.ending = "тысяч"

    def hundreds_calculation(self, number):
        last_digit = number % 10
        hundred = number // 100
        decimal = number // 10
        dec_digit = decimal % 10
        if dec_digit != 1:
            return re.sub(r'\s+', ' ', (self.hundreds.get(hundred) + " "
                                        + self.tens.get(dec_digit).lower() + " "
                                        + self.units.get(last_digit).lower()))

        else:
            full_decimal = int(str(dec_digit) + str(last_digit))
            return self.hundreds.get(hundred) + " " \
                   + self.teens.get(full_decimal).lower()

    def to_string(self):
        num = self.number
        length_of_number = len(str(num))
        if num in self.units:
            if num == 0:
                return "Ноль"
            else:
                return self.units.get(num)

        elif num in self.teens:
            return self.teens.get(num)

        elif num in self.tens:
            dec = num // 10
            return self.tens.get(dec)

        elif length_of_number == 2:
            last_digit = num % 10
            dec = num // 10
            return self.tens.get(dec) + " " \
                   + self.units.get(last_digit).lower()

        elif length_of_number == 3:
            return self.hundreds_calculation(num)

        elif length_of_number == 4:
            thousand_count = num // 1000
            return self.thousands.get(thousand_count) + " " \
                   + self.hundreds_calculation(num % 1000).lower()

        elif length_of_number == 5:
            thousand_count = num // 1000
            last_num_of_thous = thousand_count % 10
            dec_of_thous = thousand_count // 10
            if thousand_count in self.teens:
                return self.teens.get(thousand_count) + " " \
                       + self.ending + " " \
                       + self.hundreds_calculation(num % 1000).lower()

            elif dec_of_thous in self.tens and last_num_of_thous != 0:
                return self.tens.get(dec_of_thous) + " " \
                       + self.thousands.get(last_num_of_thous).lower() + " " \
                       + self.hundreds_calculation(num % 1000).lower()
            else:
                return self.tens.get(dec_of_thous) + " " \
                       + self.ending + " " \
                       + self.hundreds_calculation(num % 1000).lower()


if __name__ == "__main__":
    while True:
        number = input("Enter the number for enterpreter please:\n")
        quiting = ("q", "quit", "exit")
        if number in quiting:
            exit()
        else:
            digits = Digit(number)
            print(digits.to_string())
