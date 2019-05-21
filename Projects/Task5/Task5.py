import re

UNITS = {0: "", 1: "Один", 2: "Два", 3: "Три", 4: "Четыре",
         5: "Пять", 6: "Шесть", 7: "Семь", 8: "Восемь", 9: "Девять"}

TEENS = {10: "Десять", 11: "Одинадцать", 12: "Двенадцать",
         13: "Тринадцать", 14: "Четырнадцать", 15: "Пятнадцать",
         16: "Шестнадцать", 17: "Семнадцать", 18: "Восемнадцать",
         19: "Девятнадцать"}

TENS = {0: "", 2: "Двадцать", 3: "Тридцать", 4: "Сорок",
        5: "Пятьдесять", 6: "Шестьдесят", 7: "Семдесят",
        8: "Восемдесять", 9: "Девяносто"}

HUNDREDS = {0: "", 1: "Сто", 2: "Двести", 3: "Триста", 4: "Четыреста",
            5: "Пятьсот", 6: "Шестьсот", 7: "Семьсот",
            8: "Восемьсот", 9: "Девятьсот"}

THOUSANDS = {0: "", 1: "Одна тысяча", 2: "Две тысячи", 3: "Три тысячи",
             4: "Четыре тысячи", 5: "Пять тысяч", 6: "Шесть тысяч",
             7: "Семь тысяч", 8: "Восемь тысяч", 9: "Девять тысяч"}

ENDING = ["", "тыс", "млн", "млрд"]


class Digit:
    def __init__(self, number):

        self.number = number

    def hundreds_calculation(self, number):
        last_digit = number % 10
        hundred = number // 100
        decimal = number // 10
        dec_digit = decimal % 10
        if dec_digit != 1:
            return re.sub(r'\s+', ' ', (HUNDREDS.get(hundred).lower() + " "
                                        + TENS.get(dec_digit).lower() + " "
                                        + UNITS.get(last_digit).lower()))

        else:
            full_decimal = int(str(dec_digit) + str(last_digit))
            return HUNDREDS.get(hundred).lower() + " " + TEENS.get(full_decimal).lower()

    def to_string(self):
        digits = re.findall('.{1,3}', ''.join(self.number[-1::-1]))
        digits.reverse()
        interpretation = []
        for num in digits:
            interpretation.append(str(self.hundreds_calculation(int(''.join(num[-1::-1])))))
        result = ""
        if len(interpretation) == 2:
            interpretation.insert(-1, " " + ENDING[1] + " ")
        elif len(interpretation) == 3:
            interpretation.insert(-1, " " + ENDING[1] + " ")
            interpretation.insert(-3, " " + ENDING[2] + " ")
        elif len(interpretation) == 4:
            interpretation.insert(-1, " " + ENDING[1] + " ")
            interpretation.insert(-3, " " + ENDING[2] + " ")
            interpretation.insert(-5, " " + ENDING[3] + " ")

        for element in interpretation:
            result += element

        return re.sub(r"\s+", ' ', result.strip().capitalize())
        # num = self.number
        # length_of_number = len(str(num))
        # if num in UNITS:
        #     if num == 0:
        #         return "Ноль"
        #     else:
        #         return UNITS.get(num)
        #
        # elif num in TEENS:
        #     return TEENS.get(num)
        #
        # elif num in TENS:
        #     dec = num // 10
        #     return TENS.get(dec)
        #
        # elif length_of_number == 2:
        #     last_digit = num % 10
        #     dec = num // 10
        #     return TENS.get(dec) + " " \
        #            + UNITS.get(last_digit).lower()
        #
        # elif length_of_number == 3:
        #     return self.hundreds_calculation(num)
        #
        # elif length_of_number == 4:
        #     thousand_count = num // 1000
        #     return THOUSANDS.get(thousand_count) + " " \
        #            + self.hundreds_calculation(num % 1000).lower()
        #
        # elif length_of_number == 5:
        #     thousand_count = num // 1000
        #     last_num_of_thous = thousand_count % 10
        #     dec_of_thous = thousand_count // 10
        #     if thousand_count in TEENS:
        #         return TEENS.get(thousand_count) + " " \
        #                + ENDING + " " \
        #                + self.hundreds_calculation(num % 1000).lower()
        #
        #     elif dec_of_thous in TENS and last_num_of_thous != 0:
        #         return TENS.get(dec_of_thous) + " " \
        #                + THOUSANDS.get(last_num_of_thous).lower() + " " \
        #                + self.hundreds_calculation(num % 1000).lower()
        #     else:
        #         return TENS.get(dec_of_thous) + " " \
        #                + ENDING + " " \
        #                + self.hundreds_calculation(num % 1000).lower()
        # else:
        #     return "Too much symbols"


def main():
    while True:
        number = input("Enter the number for enterpreter please:\n")
        quiting = ("q", "quit", "exit")
        # try:
        if number in quiting:
            return False
        else:
            digits = Digit(number)
            print(digits.to_string())
        # except:
            # print("Invalid data it must be positive numbers and no more than 5 character")


if __name__ == "__main__":
    main()
