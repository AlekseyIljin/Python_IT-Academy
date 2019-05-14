import re

class Digit:
    def __init__ (self, number):
        self.number = number
        self.digits = {0:"", 1:"Один", 2:"Два", 3:"Три", 4:"Четыре", \
                       5:"Пять", 6:"Шесть", 7:"Семь", 8:"Восемь", 9:"Девять"}
        
        self.dec_digits = {10:"Десять", 11:"Одинадцать",12:"Двенадцать",\
                      13:"Тринадцать", 14:"Четырнадцать", 15:"Пятнадцать",\
                      16:"Шестнадцать", 17:"Семнадцать", 18:"Восемнадцать",\
                      19:"Девятнадцать"}
        
        self.decimals = {0:"", 2:"Двадцать", 3:"Тридцать", 4:"Сорок",\
                         5:"Пятьдесять", 6:"Шестьдесят", 7:"Семдесят",\
                         8:"Восемдесять", 9:"Девяносто"}
        
        self.hundreds = {0:"", 1:"Сто", 2:"Двести", 3:"Триста", 4:"Четыреста",\
                         5:"Пятьсот", 6:"Шестьсот", 7:"Семьсот",\
                         8:"Восемьсот", 9:"Девятьсот"}

        self.thousands = {0:"", 1:"Одна тысяча", 2:"Две тысячи", 3:"Три тысячи",\
                          4:"Четыре тысячи", 5:"Пять тысяч", 6:"Шесть тысяч",\
                          7:"Семь тысяч", 8:"Восемь тысяч", 9:"Девять тысяч"}

        self.ending = "тысяч"
        

    def hundreds_calculation(self, number):
        last_digit = number % 10
        hund = number // 100
        dec = number // 10
        count_of_dec = dec % 10
        if count_of_dec != 1:
            return re.sub(r'\s+', ' ',(str(self.hundreds.get(hund)) + " " \
                   + str(self.decimals.get(count_of_dec)).lower()+ " "\
                   + str(self.digits.get(last_digit)).lower()))
        
        else:
            return str(self.hundreds.get(hund)) + " " \
                   + str(self.dec_digits.get(int(str(count_of_dec)+str(last_digit)))).lower()



    def to_string(self):
        length_of_number = len(str(self.number))
        if self.number in self.digits:
            if self.number == 0:
                print("Ноль")
            else:
                print(self.digits.get(int(self.number)))
            
        elif self.number in self.dec_digits:
            print(self.dec_digits.get(self.number))
            
        elif self.number in self.decimals:
            dec = self.number // 10
            print(self.decimals.get(dec))
            
        elif length_of_number == 2:
            last_digit = self.number % 10
            dec = self.number // 10
            print(str(self.decimals.get(dec))+" "\
                  + str(self.digits.get(last_digit)).lower())

        elif length_of_number == 3:
            print(self.hundreds_calculation(self.number))
            
        elif length_of_number == 4:
            thous = self.number // 1000
            print(self.thousands.get(thous) + " "\
                  + self.hundreds_calculation(self.number % 1000).lower())
        elif length_of_number == 5:
            thous = self.number // 1000
            last_num_of_thous = thous % 10
            dec_of_thous = thous // 10
            if thous in self.dec_digits:
                print(str(self.dec_digits.get(thous))+ " " \
                      + self.ending + " " \
                      + self.hundreds_calculation(self.number % 1000).lower())
            elif dec_of_thous in self.decimals and last_num_of_thous != 0:
                print(self.decimals.get(dec_of_thous)+ " " \
                      + self.thousands.get(last_num_of_thous).lower() + " "\
                      + self.hundreds_calculation(self.number % 1000).lower())
            else:
                print(self.decimals.get(dec_of_thous)+ " " \
                      + self.ending + " " \
                      + self.hundreds_calculation(self.number % 1000).lower())


       

if __name__ == "__main__":
    digits = Digit(0)
    digits.to_string()
